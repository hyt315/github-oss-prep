#!/usr/bin/env python3
"""Dependency-free repository audit and release-gate validator.

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
import shutil
import subprocess
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
RULES_PATH = Path(__file__).resolve().parent / "secret-rules.json"

SELF_REQUIRED = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "CHANGELOG.md",
    "manifest.json",
    "references/readme-and-archetypes.md",
    "references/security-and-pitfalls.md",
    "references/community-and-ci.md",
    "references/publishing-and-release.md",
]

BASELINE_FILES = ["README.md", "LICENSE", ".gitignore"]
OPTIONAL_COMMUNITY_FILES = [
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    ".github/ISSUE_TEMPLATE",
    ".github/pull_request_template.md",
]
ALLOWED_SKILL_FRONTMATTER_KEYS = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
    "compatibility",
}

UNRESOLVED_RE = re.compile(r"\{(owner|repo)\}")
SUPPRESSION_RE = re.compile(
    r"<!--\s*(?:scan-ignore:\s*([a-z0-9,\-\s]+?)\s*(?:\(([^)]*)\))?\s*|skill-doctor:\s*allow[^>]*)-->"
)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
USES_RE = re.compile(r"^\s*-?\s*uses:\s*['\"]?([^'\"\s#]+)")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
WRITE_ALL_RE = re.compile(r"^permissions:\s*write-all\b", re.M)
PR_TARGET_RE = re.compile(r"\bpull_request_target\b")
UNTRUSTED_EXPR_RE = re.compile(
    r"\$\{\{\s*github\.event\.(?:issue|pull_request|comment|review|discussion|head_commit|commits)\."
)
DUMMY_RE = re.compile(r"(?i)example|test|dummy|fake|placeholder|x{4,}|1234567890|abcdef")

TOP_LEVEL_DOCS = ["README.md", "README.en.md", "SECURITY.md", "SUPPORT.md", "CONTRIBUTING.md", "CHANGELOG.md"]
PATTERN_GROUPS = ("credential_patterns", "path_patterns", "private_ip_patterns", "local_env_patterns", "personal_patterns")
HISTORY_SKIP_NAMES = {
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "uv.lock",
    "poetry.lock",
    "Cargo.lock",
    "Gemfile.lock",
    "composer.lock",
}
MAX_HISTORY_LINE_LEN = 4096


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


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace").replace("\r\n", "\n")


def _finding(findings: list[dict], fid: str, severity: str, path: Path, line: int, message: str, evidence: str = "") -> None:
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


def load_rules() -> dict:
    return json.loads(RULES_PATH.read_text(encoding="utf-8"))


def _is_self_repo(root: Path) -> bool:
    return (root / "SKILL.md").is_file() and (root / "scripts" / "secret-rules.json").is_file()


def _effective_skip_paths(root: Path, rules: dict, include_self_fixtures: bool | None = None) -> list[str]:
    paths = list(rules["scan_scope"].get("skip_paths", []))
    is_self = _is_self_repo(root) if include_self_fixtures is None else include_self_fixtures
    if is_self and "tests/fixtures" not in paths:
        paths.append("tests/fixtures")
    return paths


def _skip(path: Path, root: Path, rules: dict, skip_paths: list[str]) -> bool:
    scope = rules["scan_scope"]
    try:
        parts = path.relative_to(root).parts
    except ValueError:
        parts = path.parts
    if set(parts[:-1]) & set(scope["skip_dirs"]):
        return True
    if path.suffix.lower() in set(scope["skip_extensions"]):
        return True
    try:
        relative = path.relative_to(root).as_posix()
    except ValueError:
        relative = path.as_posix()
    return any(relative == p or relative.startswith(p.rstrip("/") + "/") for p in skip_paths)


def _iter_files(root: Path, rules: dict, skip_paths: list[str]):
    for path in sorted(root.rglob("*")):
        if not path.is_file() or _skip(path, root, rules, skip_paths):
            continue
        yield path


def _compiled(rules: dict, groups: tuple[str, ...] = PATTERN_GROUPS):
    out = []
    for key in groups:
        out += [(p["id"], p["severity"], re.compile(p["regex"]), p["label"]) for p in rules.get(key, [])]
    return out


def _match_line(text: str, patterns, suppressed: set[str]):
    """Single matcher shared by tree, .git/config, and history scans."""
    for fid, sev, rx, label in patterns:
        if fid in suppressed or "all" in suppressed:
            continue
        hit = rx.search(text)
        if hit:
            yield fid, sev, label, hit.group(0)


def check_placeholders_and_anchors(root: Path, findings: list[dict]) -> None:
    """Placeholders must be resolved in shipped top-level docs, and in-page anchors must exist."""
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


def check_ci_pinning(root: Path, findings: list[dict]) -> None:
    """CI supply-chain checks: permissions, SHA pinning, pull_request_target, and script injection."""
    wf_dir = root / ".github" / "workflows"
    if not wf_dir.is_dir():
        return
    for wf in sorted(list(wf_dir.glob("*.yml")) + list(wf_dir.glob("*.yaml"))):
        text = _read(wf)
        if not re.search(r"^permissions:", text, re.M):
            _finding(findings, "ci-pin-permissions", "P1", wf, 0,
                     "workflow has no top-level permissions: block (default token may be overly broad)")
        elif WRITE_ALL_RE.search(text):
            _finding(findings, "ci-permissions-write-all", "P1", wf, 0,
                     "workflow declares 'permissions: write-all'; use read-only defaults and narrow per job")
        if PR_TARGET_RE.search(text):
            _finding(findings, "ci-pull-request-target", "P1", wf, 0,
                     "workflow uses pull_request_target; avoid checking out untrusted fork code with secrets")
        in_run_block = False
        run_indent = 0
        for lineno, line in enumerate(text.splitlines(), 1):
            m = USES_RE.match(line)
            if m:
                ref = m.group(1)
                if not ref.startswith(("./", "docker://")):
                    if "@" not in ref or not SHA_RE.match(ref.rsplit("@", 1)[1]):
                        _finding(findings, "ci-pin-sha", "P1", wf, lineno,
                                 "external action not pinned to a full 40-char commit SHA", ref)
            stripped = line.lstrip()
            indent = len(line) - len(stripped)
            if re.match(r"^-?\s*run:\s*", stripped):
                in_run_block = stripped.rstrip().endswith(("|", ">", "|-", ">-"))
                run_indent = indent
                if UNTRUSTED_EXPR_RE.search(line):
                    _finding(findings, "ci-script-injection", "P1", wf, lineno,
                             "untrusted github.event expression interpolated in run:; bind via env: first", stripped[:80])
            elif in_run_block:
                if stripped and indent <= run_indent:
                    in_run_block = False
                elif UNTRUSTED_EXPR_RE.search(line):
                    _finding(findings, "ci-script-injection", "P1", wf, lineno,
                             "untrusted github.event expression interpolated in run:; bind via env: first", stripped[:80])


def check_community_baseline(root: Path, findings: list[dict]) -> dict[str, list[str]]:
    """Report presence of baseline and optional community files for any repository."""
    present: list[str] = []
    missing_baseline: list[str] = []
    missing_optional: list[str] = []
    for name in BASELINE_FILES:
        exists = (root / name).exists()
        if name == "README.md" and not exists:
            exists = any((root / alt).is_file() for alt in ("README.md", "readme.md", "README.rst"))
        if name == "LICENSE" and not exists:
            exists = any((root / alt).is_file() for alt in ("LICENSE", "LICENSE.md", "LICENSE.txt"))
        if exists:
            present.append(name)
        else:
            missing_baseline.append(name)
            _finding(findings, "missing-baseline-file", "P2", root / name, 0,
                     f"baseline open-source file missing ({name})")
    for name in OPTIONAL_COMMUNITY_FILES:
        exists = (root / name).exists() or (root / ".github" / name).exists() or (root / "docs" / name).exists()
        if exists:
            present.append(name)
        else:
            missing_optional.append(name)
    return {
        "present": present,
        "missing_baseline": missing_baseline,
        "missing_optional": missing_optional,
    }


def check_skill_frontmatter(root: Path, findings: list[dict]) -> str | None:
    """Validate SKILL.md frontmatter against agentskills.io spec on any repo containing SKILL.md."""
    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        return None
    skill = _read(skill_path)
    if not re.match(r"^---\n(?s:.*?)\n---\n", skill):
        _finding(findings, "frontmatter", "P0", skill_path, 1, "SKILL.md frontmatter missing or malformed")
        return None
    front = skill.split("---", 2)[1]
    for key in ("name:", "description:"):
        if not re.search(rf"^{key}", front, re.M):
            _finding(findings, "frontmatter", "P0", skill_path, 1, f"frontmatter missing {key[:-1]}")
    fm_version = None
    in_meta = False
    for line in front.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line.startswith((" ", "\t")):
            in_meta = bool(re.match(r"^metadata:\s*$", line))
            top_key = line.split(":", 1)[0].strip()
            if top_key == "version":
                fm_version = fm_version or line.split(":", 1)[1].strip().strip("'\"")
                _finding(findings, "frontmatter-nonstandard", "P2", skill_path, 1,
                         "top-level version: is not an Agent Skills field; move it to metadata.version")
            elif top_key not in ALLOWED_SKILL_FRONTMATTER_KEYS:
                _finding(findings, "frontmatter-nonstandard", "P2", skill_path, 1,
                         f"top-level '{top_key}:' is outside the agentskills.io spec; place custom keys under metadata:")
        elif in_meta and re.match(r"^\s+version:", line):
            fm_version = line.split(":", 1)[1].strip().strip("'\"")
    return fm_version


def check_self_profile(root: Path, findings: list[dict], fm_version: str | None) -> str | None:
    """Self-checks for github-oss-prep itself (required files and version consistency)."""
    for relative in SELF_REQUIRED:
        if not (root / relative).is_file():
            _finding(findings, "missing-required-file", "P0", root / relative, 0, "required skill file missing")
    manifest_path = root / "manifest.json"
    if not manifest_path.is_file():
        return None
    try:
        manifest = json.loads(_read(manifest_path))
    except json.JSONDecodeError as exc:
        _finding(findings, "manifest-invalid", "P0", manifest_path, exc.lineno, f"manifest.json is not valid JSON: {exc.msg}")
        return None
    version = manifest.get("version")
    if version and fm_version != version:
        _finding(findings, "version-mismatch", "P0", root / "SKILL.md", 1,
                 f"SKILL.md frontmatter version ({fm_version or 'missing'}) != manifest.json ({version})")
    changelog = root / "CHANGELOG.md"
    if version and changelog.is_file() and f"## [{version}]" not in _read(changelog):
        _finding(findings, "version-mismatch", "P0", changelog, 0, f"CHANGELOG has no section for {version}")
    return version


def _report_tracked_artifacts(root: Path, rules: dict, findings: list[dict]) -> None:
    if not shutil.which("git") or not (root / ".git").exists():
        return
    tracked = subprocess.run(
        ["git", "-C", str(root), "ls-files"],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    ).stdout.splitlines()
    skip = set(rules["scan_scope"]["skip_dirs"]) - {".git"}
    seen = set()
    for rel in tracked:
        hit = next((part for part in rel.split("/")[:-1] if part in skip), None)
        if hit and hit not in seen:
            seen.add(hit)
            _finding(findings, "tracked-artifact", "P1", root / rel, 0,
                     f"build/cache directory '{hit}/' is committed; remove it from git and add it to .gitignore")


def scan_tree(root: Path, rules: dict | None = None, *, skip_self_fixtures: bool | None = None) -> list[dict]:
    """Scan a directory tree for secrets, privacy leaks, broken links, placeholders, and CI issues."""
    rules = rules or load_rules()
    findings: list[dict] = []
    skip_paths = _effective_skip_paths(root, rules, include_self_fixtures=skip_self_fixtures)

    cred = _compiled(rules, ("credential_patterns",))
    patterns = _compiled(rules)
    allow = set(rules.get("filename_allowlist", []))
    max_bytes = rules["scan_scope"].get("max_file_bytes", 0)

    for path in _iter_files(root, rules, skip_paths):
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

    git_config = root / ".git" / "config"
    if git_config.is_file():
        for lineno, line in enumerate(_read(git_config).splitlines(), 1):
            for fid, sev, label, hit in _match_line(line, cred, set()):
                _finding(findings, fid, sev, git_config, lineno, label + " (in .git/config)", hit)

    _report_tracked_artifacts(root, rules, findings)

    for path in _iter_files(root, rules, skip_paths):
        if path.suffix.lower() not in {".md", ".markdown"}:
            continue
        for lineno, line in _outside_fences(_read(path)):
            cleaned = INLINE_CODE_RE.sub("", line)
            for target in LINK_RE.findall(cleaned):
                if target.startswith(("http://", "https://", "mailto:", "#", "tel:")):
                    continue
                clean = target.split("#", 1)[0]
                if not clean:
                    continue
                resolved = (path.parent / clean).resolve()
                if not resolved.exists():
                    _finding(findings, "broken-link", "P1", path, lineno, "relative link target missing", target)

    check_placeholders_and_anchors(root, findings)
    check_ci_pinning(root, findings)
    return findings


def scan_history(root: Path, rules: dict | None = None) -> list[dict]:
    """Stream git history diffs line-by-line to detect secrets and non-noreply commit emails."""
    rules = rules or load_rules()
    findings: list[dict] = []
    if not shutil.which("git") or not (root / ".git").exists():
        _finding(findings, "history-unscanned", "P2", root, 0, "git history not scanned (no git or not a repository)")
        return findings

    patterns = _compiled(rules)
    skip = tuple(_effective_skip_paths(root, rules))
    skip_exts = set(rules["scan_scope"].get("skip_extensions", []))
    commit, current, seen = "?", "?", set()
    skip_current_file = False
    noreply = re.compile(r"(?:@users\.noreply\.github\.com|^noreply@github\.com)$")

    proc = subprocess.Popen(
        ["git", "-C", str(root), "log", "--all", "-p", "--no-color", "--no-ext-diff", "--format=@@COMMIT %h %ae %ce"],
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, encoding="utf-8", errors="replace",
    )
    assert proc.stdout is not None
    try:
        for raw_line in proc.stdout:
            line = raw_line.rstrip("\r\n")
            if line.startswith("@@COMMIT "):
                parts = line.split()
                commit = parts[1] if len(parts) > 1 else "?"
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
                cur_path = Path(current)
                skip_current_file = (
                    current.startswith(skip)
                    or cur_path.name in HISTORY_SKIP_NAMES
                    or cur_path.suffix.lower() in skip_exts
                )
                continue
            if skip_current_file or not line.startswith("+") or line.startswith("+++"):
                continue
            if len(line) > MAX_HISTORY_LINE_LEN:
                continue
            text = line[1:]
            suppressed = {r.strip() for m in SUPPRESSION_RE.finditer(text) for r in (m.group(1) or "").split(",") if r.strip()}
            for fid, sev, label, hit in _match_line(text, patterns, suppressed):
                if (fid, hit) in seen:
                    continue
                seen.add((fid, hit))
                if sev == "P0" and DUMMY_RE.search(hit):
                    sev = "P2"
                _finding(findings, fid, sev, Path(f"history:{commit}:{current}"), 0,
                         label + " (in git history; removing it now does not erase it)", hit)
    finally:
        proc.stdout.close()
        proc.wait()
    return findings


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    parser = argparse.ArgumentParser(description="Repository audit and release-gate validator")
    parser.add_argument("target", nargs="?", default=None, help="directory to check (default: this skill)")
    parser.add_argument("--json", action="store_true", help="output as JSON (shortcut for --format json)")
    parser.add_argument("--format", choices=["text", "json", "md"], default=None)
    parser.add_argument("--strict", action="store_true",
                        help="treat P1 findings in the current tree as failures; history P1 stays report-only")
    parser.add_argument("--history", action="store_true", help="also scan git commit history and commit emails")
    args = parser.parse_args()

    root = Path(args.target).resolve() if args.target else SKILL_ROOT
    fmt = args.format or ("json" if args.json else "text")

    findings: list[dict] = []
    fm_version = check_skill_frontmatter(root, findings)
    version = check_self_profile(root, findings, fm_version) if _is_self_repo(root) else fm_version
    community = check_community_baseline(root, findings)
    findings.extend(scan_tree(root))
    if args.history:
        findings.extend(scan_history(root))

    blocking = [f for f in findings if f["severity"] == "P0"]
    strict_hits = [f for f in findings if f["severity"] == "P1" and not str(f["file"]).startswith("history:")]
    failed = bool(blocking) or (args.strict and bool(strict_hits))

    for f in findings:
        f["file"] = str(Path(f["file"]).relative_to(root)) if str(f["file"]).startswith(str(root)) else f["file"]

    if fmt == "json":
        print(json.dumps({
            "status": "FAIL" if failed else "PASS",
            "version": version,
            "community_files": community,
            "findings": findings,
        }, ensure_ascii=False))
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
