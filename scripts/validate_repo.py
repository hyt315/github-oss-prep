#!/usr/bin/env python3
"""Dependency-free repository checks.

Usable on this skill's own repository (default) or on any target directory:

    python scripts/validate_repo.py [TARGET_DIR] [--json] [--format text|json|md] [--strict] [--history]

Rules (secrets, private paths, blocked filenames) live in scripts/secret-rules.json
and are the single source of truth — tests import them from here, docs must not
re-list regexes.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
RULES_PATH = Path(__file__).resolve().parent / "secret-rules.json"

REQUIRED = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "references/pr-and-release-workflow.md",
    "references/discovery-and-promotion.md",
]

UNRESOLVED_RE = re.compile(r"\{(owner|repo)\}")
SUPPRESSION_RE = re.compile(
    r"<!--\s*(?:scan-ignore:\s*([a-z0-9,\-\s]+?)\s*(?:\(([^)]*)\))?\s*|skill-doctor:\s*allow[^>]*)-->"
)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
INSTRUCTION_RE = re.compile(r"(说明|描述|填写|此处嵌入|给出|列出)")
CRITERIA_MARK = "<!-- 判据"

TEMPLATE_FILE = "references/readme-template.md"
TEMPLATE_DIR = "references/readme-templates"
TOP_LEVEL_DOCS = ["README.md", "README.en.md", "SECURITY.md", "SUPPORT.md", "CONTRIBUTING.md", "CHANGELOG.md"]


def _slug(text: str) -> str:
    """Approximate GitHub's heading anchors: lowercase, spaces -> '-', drop punctuation/emoji."""
    return re.sub(r"[^a-z0-9_\u4e00-\u9fff-]+", "", text.strip().lower().replace(" ", "-"))


def _outside_fences(text: str):
    inside = False
    for lineno, line in enumerate(text.splitlines(), 1):
        if FENCE_RE.match(line):
            inside = not inside
            continue
        if not inside:
            yield lineno, line


def check_template_quality(root: Path, findings: list[dict]) -> None:
    """Judgement-quality gates for the README template library (this skill only)."""
    index = root / TEMPLATE_FILE
    if not index.is_file():
        return
    files = [index] + sorted((root / TEMPLATE_DIR).glob("*.md"))
    has_real_output = False
    for tpl in files:
        text = _read(tpl)
        lines = text.splitlines()
        has_real_output = has_real_output or bool(re.search(r"^\$ ", text, re.M))
        for idx, line in enumerate(lines, 1):
            s = INLINE_CODE_RE.sub("", line).strip()
            if not s or s.startswith(("|", "#", "```", "<!--", ">")) or not INSTRUCTION_RE.search(s):
                continue
            if CRITERIA_MARK not in "\n".join(lines[max(0, idx - 4):idx]):
                _finding(findings, "tpl-guidance-density", "P1", tpl, idx,
                         "instruction blank without a <!-- 判据 --> above it", s[:60])
        for idx, line in enumerate(lines, 1):
            if "badge/License-MIT" in line:
                _finding(findings, "tpl-hardcoded-license", "P1", tpl, idx,
                         "license badge hard-codes MIT; derive it from category-map", line.strip()[:60])
            if "](" in line and "![Platform" in line and "](SKILL.md)" in line:
                _finding(findings, "tpl-badge-semantics", "P2", tpl, idx,
                         "platform badge should link to the compatibility section, not SKILL.md")
    if not has_real_output:
        _finding(findings, "tpl-real-output", "P1", index, 0,
                 "no real terminal output sample (a line starting with '$ ') in the template library")


def check_placeholders_and_anchors(root: Path, findings: list[dict]) -> None:
    """Placeholders must be resolved in shipped docs, and in-page anchors must exist."""
    for name in TOP_LEVEL_DOCS:
        path = root / name
        if not path.is_file():
            continue
        text = _read(path)
        for lineno, line in _outside_fences(text):
            stripped = INLINE_CODE_RE.sub("", line)
            for m in UNRESOLVED_RE.finditer(stripped):
                _finding(findings, "placeholder-unresolved", "P0", path, lineno,
                         "unresolved placeholder in shipped doc", m.group(0))
        headings = {_slug(h) for _, h in re.findall(r"^(#{1,6})\s+(.+)$", text, re.M)}
        for lineno, line in _outside_fences(text):
            for target in LINK_RE.findall(line):
                if target.startswith("#") and len(target) > 1 and _slug(target[1:]) not in headings:
                    _finding(findings, "anchor-missing", "P1", path, lineno,
                             "in-page anchor has no matching heading", target)



USES_RE = re.compile(r"^\s*-?\s*uses:\s*['\"]?([^'\"\s#]+)")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def check_ci_pinning(root: Path, findings: list[dict]) -> None:
    """CI-PIN: workflows declare top-level permissions and pin external actions to a full commit SHA."""
    wf_dir = root / ".github" / "workflows"
    if not wf_dir.is_dir():
        return
    for wf in sorted(list(wf_dir.glob("*.yml")) + list(wf_dir.glob("*.yaml"))):
        text = _read(wf)
        if not re.search(r"^permissions:", text, re.M):
            _finding(findings, "ci-pin-permissions", "P1", wf, 0,
                     "workflow has no top-level permissions: block (default token may be read-write)")
        for lineno, line in enumerate(text.splitlines(), 1):
            m = USES_RE.match(line)
            if not m:
                continue
            ref = m.group(1)
            if ref.startswith(("./", "docker://")):
                continue
            if "@" not in ref or not SHA_RE.match(ref.rsplit("@", 1)[1]):
                _finding(findings, "ci-pin-sha", "P1", wf, lineno,
                         "external action not pinned to a full 40-char commit SHA", ref)


def load_rules() -> dict:
    return json.loads(RULES_PATH.read_text(encoding="utf-8"))


def _skip(path: Path, root: Path, rules: dict) -> bool:
    scope = rules["scan_scope"]
    try:
        parts = path.relative_to(root).parts
    except ValueError:
        parts = path.parts
    # only directories *inside* the target count; a target that itself lives under build/ or venv/ is still scanned
    if set(parts[:-1]) & set(scope["skip_dirs"]):
        return True
    if path.suffix.lower() in set(scope["skip_extensions"]):
        return True
    try:
        relative = path.relative_to(root).as_posix()
    except ValueError:
        relative = path.as_posix()
    return any(relative == p or relative.startswith(p.rstrip("/") + "/") for p in scope["skip_paths"])


def _iter_files(root: Path, rules: dict):
    for path in sorted(root.rglob("*")):
        if not path.is_file() or _skip(path, root, rules):
            continue
        yield path


def _read(path: Path) -> str:
    # utf-8-sig strips a BOM; newline normalisation keeps CRLF files (Windows checkouts) parseable
    return path.read_text(encoding="utf-8-sig", errors="replace").replace("\r\n", "\n")


def _finding(findings, fid, severity, path, line, message, evidence=""):
    findings.append(
        {
            "id": fid,
            "severity": severity,
            "file": str(path),
            "line": line,
            "message": message,
            "evidence": evidence[:120],
        }
    )


def _report_tracked_artifacts(root: Path, rules: dict, findings: list[dict]) -> None:
    import shutil
    import subprocess

    if not shutil.which("git") or not (root / ".git").exists():
        return
    tracked = subprocess.run(["git", "-C", str(root), "ls-files"], capture_output=True, text=True,
                             encoding="utf-8", errors="replace").stdout.splitlines()
    skip = set(rules["scan_scope"]["skip_dirs"]) - {".git"}
    seen = set()
    for rel in tracked:
        hit = next((part for part in rel.split("/")[:-1] if part in skip), None)
        if hit and hit not in seen:
            seen.add(hit)
            _finding(findings, "tracked-artifact", "P1", root / rel, 0,
                     f"build/cache directory '{hit}/' is committed; remove it from git and add it to .gitignore")


def scan_tree(root: Path, rules: dict | None = None) -> list[dict]:
    """Scan a directory tree. Returns findings (P0/P1/P2)."""
    rules = rules or load_rules()
    findings: list[dict] = []

    cred = _compiled(rules, ("credential_patterns",))
    patterns = _compiled(rules)
    allow = set(rules.get("filename_allowlist", []))

    max_bytes = rules["scan_scope"].get("max_file_bytes", 0)
    for path in _iter_files(root, rules):
        if path.name in allow:
            continue
        if max_bytes and path.stat().st_size > max_bytes:
            _finding(findings, "large-file-skipped", "P2", path, 0,
                     f"not scanned: larger than {max_bytes // 1048576} MB (check it by hand or exclude it)")
            continue
        for entry in rules.get("blocked_filenames", []):
            pattern = entry["glob"].replace("**/", "")
            if path.match(pattern) or path.name == Path(pattern).name:
                _finding(findings, "blocked-file", entry["severity"], path, 0, entry["reason"])
        try:
            text = _read(path)
        except OSError:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            if not line.strip():
                continue
            suppressed = set()
            for match in SUPPRESSION_RE.finditer(line):
                rule_ids = [r.strip() for r in (match.group(1) or "").split(",") if r.strip()]
                reason = match.group(2)
                suppressed.update(rule_ids)
                if not rule_ids:
                    suppressed.add("skill-doctor-allow")
                _finding(
                    findings,
                    "suppression-comment",
                    "P2",
                    path,
                    lineno,
                    "inline suppression for " + (",".join(rule_ids) if rule_ids else "skill-doctor")
                    + (f" ({reason})" if reason else ""),
                )
            for fid, sev, label, hit in _match_line(line, patterns, suppressed):
                _finding(findings, fid, sev, path, lineno, label, hit)

    # .git/config is skipped with .git/, but a token-bearing remote URL there leaks with any ZIP of the folder
    git_config = root / ".git" / "config"
    if git_config.is_file():
        for lineno, line in enumerate(_read(git_config).splitlines(), 1):
            for fid, sev, label, hit in _match_line(line, cred, set()):
                _finding(findings, fid, sev, git_config, lineno, label + " (in .git/config)", hit)

    # build caches and dependency folders are skipped above; report any that are actually tracked by git
    _report_tracked_artifacts(root, rules, findings)

    # markdown relative links (skip fenced code blocks)
    for path in _iter_files(root, rules):
        if path.suffix.lower() not in {".md", ".markdown"}:
            continue
        in_fence = False
        for lineno, line in enumerate(_read(path).splitlines(), 1):
            if FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            line = re.sub(r"`[^`]*`", "", line)
            for target in LINK_RE.findall(line):
                if target.startswith(("http://", "https://", "mailto:", "#", "tel:")):
                    continue
                clean = target.split("#", 1)[0]
                if not clean:
                    continue
                resolved = (path.parent / clean).resolve()
                if not resolved.exists():
                    _finding(findings, "broken-link", "P1", path, lineno, "relative link target missing", target)
    check_template_quality(root, findings)
    check_placeholders_and_anchors(root, findings)
    check_ci_pinning(root, findings)
    return findings


PATTERN_GROUPS = ("credential_patterns", "path_patterns", "private_ip_patterns", "local_env_patterns", "personal_patterns")


def _compiled(rules: dict, groups: tuple[str, ...] = PATTERN_GROUPS):
    out = []
    for key in groups:
        out += [(p["id"], p["severity"], re.compile(p["regex"]), p["label"]) for p in rules.get(key, [])]
    return out


def _match_line(text: str, patterns, suppressed: set[str]):
    """The one matcher shared by the tree, .git/config and history scans: (id, severity, label, evidence)."""
    for fid, sev, rx, label in patterns:
        if fid in suppressed or "all" in suppressed:
            continue
        hit = rx.search(text)
        if hit:
            yield fid, sev, label, hit.group(0)


DUMMY_RE = re.compile(r"(?i)example|test|dummy|fake|placeholder|x{4,}|1234567890|abcdef")


def scan_history(root: Path, rules: dict | None = None) -> list[dict]:
    """Scan every line ever added in reachable git history, plus commit author/committer emails.

    Deleting a leak in a new commit does not remove it from history; this is the check
    SKILL.md Step 3.3 asks for. Requires the `git` executable; reports P2 if unavailable.
    """
    import shutil
    import subprocess

    rules = rules or load_rules()
    findings: list[dict] = []
    if not shutil.which("git") or not (root / ".git").exists():
        _finding(findings, "history-unscanned", "P2", root, 0, "git history not scanned (no git or not a repository)")
        return findings
    log = subprocess.run(
        ["git", "-C", str(root), "log", "--all", "-p", "--no-color", "--no-ext-diff", "--format=@@COMMIT %h %ae %ce"],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    ).stdout
    patterns = _compiled(rules)
    skip = tuple(rules["scan_scope"]["skip_paths"])
    commit, current, seen = "?", "?", set()
    noreply = re.compile(r"(?:@users\.noreply\.github\.com|^noreply@github\.com)$")
    for line in log.splitlines():
        if line.startswith("@@COMMIT "):
            parts = line.split()
            commit = parts[1]
            for email in parts[2:]:
                if email and not noreply.search(email) and ("email", email) not in seen:
                    seen.add(("email", email))
                    personal = any(fid == "personal-email" for fid, *_ in _match_line(email, patterns, set()))
                    _finding(findings, "history-author-email", "P1" if personal else "P2", Path(f"history:{commit}"), 0,
                             "commit metadata exposes a " + ("personal mailbox" if personal else "non-noreply email")
                             + "; set user.email to your GitHub noreply address for future commits", email)
            continue
        if line.startswith("+++ b/"):
            current = line[6:]
            continue
        if not line.startswith("+") or line.startswith("+++") or current.startswith(skip):
            continue
        text = line[1:]
        suppressed = {r.strip() for m in SUPPRESSION_RE.finditer(text) for r in (m.group(1) or "").split(",") if r.strip()}
        for fid, sev, label, hit in _match_line(text, patterns, suppressed):
            if (fid, hit) in seen:
                continue
            seen.add((fid, hit))
            if sev == "P0" and DUMMY_RE.search(hit):
                sev = "P2"  # obvious placeholder (example/test/123456…): show it, don't block
            _finding(findings, fid, sev, Path(f"history:{commit}:{current}"), 0,
                     label + " (in git history; removing it now does not erase it)", hit)
    return findings


def check_skill_profile(root: Path, findings: list[dict]) -> str | None:
    """Skill-specific checks. Returns manifest version if present."""
    for relative in REQUIRED:
        if not (root / relative).is_file():
            _finding(findings, "missing-required-file", "P0", root / relative, 0, "required file missing")
    manifest_path = root / "manifest.json"
    if not manifest_path.is_file():
        return None
    try:
        manifest = json.loads(_read(manifest_path))
    except json.JSONDecodeError as exc:
        _finding(findings, "manifest-invalid", "P0", manifest_path, exc.lineno, f"manifest.json is not valid JSON: {exc.msg}")
        return None
    version = manifest.get("version")
    skill = _read(root / "SKILL.md")
    front = skill.split("---", 2)[1] if skill.startswith("---") else ""
    if not re.match(r"^---\n(?s:.*?)\n---\n", skill):
        _finding(findings, "frontmatter", "P0", root / "SKILL.md", 1, "SKILL.md frontmatter missing or malformed")
    for key in ("name:", "description:"):
        if key not in front:
            _finding(findings, "frontmatter", "P0", root / "SKILL.md", 1, f"frontmatter missing {key[:-1]}")
    # Agent Skills spec: version lives under metadata (metadata.version); a top-level key is non-standard
    fm_version = None
    in_meta = False
    for line in front.splitlines():
        if re.match(r"^metadata:\s*$", line):
            in_meta = True
            continue
        if in_meta and re.match(r"^\s+version:", line):
            fm_version = line.split(":", 1)[1].strip().strip("'\"")
        elif re.match(r"^version:", line):
            fm_version = fm_version or line.split(":", 1)[1].strip().strip("'\"")
            _finding(findings, "frontmatter-nonstandard", "P2", root / "SKILL.md", 1,
                     "top-level version: is not an Agent Skills field; move it to metadata.version")
        elif line and not line.startswith((" ", "\t")):
            in_meta = False
    if version and fm_version != version:
        _finding(
            findings,
            "version-mismatch",
            "P0",
            root / "SKILL.md",
            1,
            f"SKILL.md frontmatter version ({fm_version or 'missing'}) != manifest.json ({version})",
        )
    # Reference Map sizes ("（约 9.7 KB）") must stay within 20% of the real file size
    for lineno, line in enumerate(skill.splitlines(), 1):
        m = re.search(r"\]\(((?:references|scripts)/[^)#]+)\).*?（约?\s*([\d.]+)\s*KB）", line)
        if not m:
            continue
        target = root / m.group(1)
        if target.is_file():
            actual = target.stat().st_size / 1024
            stated = float(m.group(2))
            if abs(actual - stated) > max(0.5, actual * 0.2):
                _finding(findings, "reference-size-drift", "P1", root / "SKILL.md", lineno,
                         f"Reference Map says {stated} KB but {m.group(1)} is {actual:.1f} KB")
    changelog = root / "CHANGELOG.md"
    if version and changelog.is_file() and f"## [{version}]" not in _read(changelog):
        _finding(findings, "version-mismatch", "P0", changelog, 0, f"CHANGELOG has no section for {version}")
    return version


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")  # Windows consoles/pipes default to gbk/cp1252
        except (AttributeError, ValueError):
            pass
    parser = argparse.ArgumentParser(description="Repository validation tool")
    parser.add_argument("target", nargs="?", default=None, help="directory to check (default: this skill)")
    parser.add_argument("--json", action="store_true", help="output as JSON (shortcut for --format json)")
    parser.add_argument("--format", choices=["text", "json", "md"], default=None)
    parser.add_argument("--strict", action="store_true",
                        help="treat P1 findings in the current tree as failures (use before publishing); history P1 stays report-only")
    parser.add_argument("--history", action="store_true", help="also scan every line ever committed and commit emails")
    args = parser.parse_args()

    root = Path(args.target).resolve() if args.target else SKILL_ROOT
    fmt = args.format or ("json" if args.json else "text")
    is_skill = (root / "SKILL.md").is_file() and (root / "scripts" / "secret-rules.json").is_file()

    findings: list[dict] = []
    version = check_skill_profile(root, findings) if is_skill else None
    findings.extend(scan_tree(root))
    if args.history:
        findings.extend(scan_history(root))

    blocking = [f for f in findings if f["severity"] == "P0"]
    # P1 in history is report-only: it can only be cleared by rewriting history, which is the user's call
    strict_hits = [f for f in findings if f["severity"] == "P1" and not str(f["file"]).startswith("history:")]
    failed = bool(blocking) or (args.strict and bool(strict_hits))

    for f in findings:
        f["file"] = str(Path(f["file"]).relative_to(root)) if str(f["file"]).startswith(str(root)) else f["file"]

    if fmt == "json":
        print(json.dumps({"status": "FAIL" if failed else "PASS", "version": version, "findings": findings}, ensure_ascii=False))
    elif fmt == "md":
        print("| 级别 | 规则 | 位置 | 说明 |")
        print("|---|---|---|---|")
        for f in findings:
            print(f"| {f['severity']} | `{f['id']}` | `{f['file']}:{f['line']}` | {f['message']} |")
        if not findings:
            print("| — | — | — | 无发现 |")
    else:
        for f in findings:
            print(f"[{f['severity']}] {f['id']} {f['file']}:{f['line']} — {f['message']}" + (f"  «{f['evidence']}»" if f["evidence"] else ""))
        counts = {s: sum(1 for f in findings if f["severity"] == s) for s in ("P0", "P1", "P2")}
        tally = f" — P0={counts['P0']} P1={counts['P1']} P2={counts['P2']}"
        label = root.name + (f" (v{version})" if version else "")
        if failed:
            reason = "P0 findings" if blocking else "P1 findings under --strict"
            print(f"FAIL: {label} blocked by {reason}{tally}")
        else:
            print(f"OK: checks passed for {label}{tally}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
