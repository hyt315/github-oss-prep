#!/usr/bin/env python3
"""Dependency-free repository checks.

Usable on this skill's own repository (default) or on any target directory:

    python scripts/validate_repo.py [TARGET_DIR] [--json] [--format text|json|md] [--strict]

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

PLACEHOLDER_RE = re.compile(r"<(?:owner|repo)>")
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
TOP_LEVEL_DOCS = ["README.md", "README.en.md", "SECURITY.md", "SUPPORT.md", "CONTRIBUTING.md", "CHANGELOG.md"]


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9\u4e00-\u9fff-]+", "", text.lower()).replace(" ", "-")


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
    tpl = root / TEMPLATE_FILE
    if not tpl.is_file():
        return
    text = _read(tpl)
    lines = text.splitlines()
    for idx, line in enumerate(lines, 1):
        s = INLINE_CODE_RE.sub("", line).strip()
        if not s or s.startswith(("|", "#", "```", "<!--")) or not INSTRUCTION_RE.search(s):
            continue
        if CRITERIA_MARK not in "\n".join(lines[max(0, idx - 4):idx]):
            _finding(findings, "tpl-guidance-density", "P1", tpl, idx,
                     "instruction blank without a <!-- 判据 --> above it", s[:60])
    if not re.search(r"^\$ ", text, re.M):
        _finding(findings, "tpl-real-output", "P1", tpl, 0,
                 "no real terminal output sample (a line starting with '$ ') in the template library")
    for idx, line in enumerate(lines, 1):
        if "badge/License-MIT" in line:
            _finding(findings, "tpl-hardcoded-license", "P1", tpl, idx,
                     "license badge hard-codes MIT; derive it from category-map", line.strip()[:60])
        if "](" in line and "![Platform" in line and "](SKILL.md)" in line:
            _finding(findings, "tpl-badge-semantics", "P2", tpl, idx,
                     "platform badge should link to the compatibility section, not SKILL.md")


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



def load_rules() -> dict:
    return json.loads(RULES_PATH.read_text(encoding="utf-8"))


def _skip(path: Path, root: Path, rules: dict) -> bool:
    scope = rules["scan_scope"]
    if set(path.parts) & set(scope["skip_dirs"]):
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
    return path.read_text(encoding="utf-8", errors="replace")


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


def scan_tree(root: Path, rules: dict | None = None) -> list[dict]:
    """Scan a directory tree. Returns findings (P0/P1/P2)."""
    rules = rules or load_rules()
    findings: list[dict] = []

    cred = [(p["id"], p["severity"], re.compile(p["regex"]), p["label"]) for p in rules["credential_patterns"]]
    paths = [(p["id"], p["severity"], re.compile(p["regex"]), p["label"]) for p in rules.get("path_patterns", [])]
    ips = [(p["id"], p["severity"], re.compile(p["regex"]), p["label"]) for p in rules.get("private_ip_patterns", [])]
    allow = set(rules.get("filename_allowlist", []))

    for path in _iter_files(root, rules):
        if path.name in allow:
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
            for fid, sev, rx, label in cred + paths + ips:
                if fid in suppressed or "all" in suppressed:
                    continue
                hit = rx.search(line)
                if hit:
                    _finding(findings, fid, sev, path, lineno, label, hit.group(0))
            for match in PLACEHOLDER_RE.finditer(line):
                _finding(findings, "unresolved-placeholder", "P0", path, lineno, "unresolved placeholder", match.group(0))

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
    return findings


def check_skill_profile(root: Path, findings: list[dict]) -> str | None:
    """Skill-specific checks. Returns manifest version if present."""
    for relative in REQUIRED:
        if not (root / relative).is_file():
            _finding(findings, "missing-required-file", "P0", root / relative, 0, "required file missing")
    manifest_path = root / "manifest.json"
    if not manifest_path.is_file():
        return None
    manifest = json.loads(_read(manifest_path))
    version = manifest.get("version")
    skill = _read(root / "SKILL.md")
    front = skill.split("---", 2)[1] if skill.startswith("---") else ""
    if not re.match(r"^---\n(?s:.*?)\n---\n", skill):
        _finding(findings, "frontmatter", "P0", root / "SKILL.md", 1, "SKILL.md frontmatter missing or malformed")
    for key in ("name:", "description:"):
        if key not in front:
            _finding(findings, "frontmatter", "P0", root / "SKILL.md", 1, f"frontmatter missing {key[:-1]}")
    fm_version = None
    for line in front.splitlines():
        if line.strip().startswith("version:"):
            fm_version = line.split(":", 1)[1].strip()
    if version and fm_version != version:
        _finding(
            findings,
            "version-mismatch",
            "P0",
            root / "SKILL.md",
            1,
            f"SKILL.md frontmatter version ({fm_version or 'missing'}) != manifest.json ({version})",
        )
    changelog = root / "CHANGELOG.md"
    if version and changelog.is_file() and f"## [{version}]" not in _read(changelog):
        _finding(findings, "version-mismatch", "P0", changelog, 0, f"CHANGELOG has no section for {version}")
    return version


def main() -> int:
    parser = argparse.ArgumentParser(description="Repository validation tool")
    parser.add_argument("target", nargs="?", default=None, help="directory to check (default: this skill)")
    parser.add_argument("--json", action="store_true", help="output as JSON (shortcut for --format json)")
    parser.add_argument("--format", choices=["text", "json", "md"], default=None)
    parser.add_argument("--strict", action="store_true", help="treat P1 findings as failures")
    args = parser.parse_args()

    root = Path(args.target).resolve() if args.target else SKILL_ROOT
    fmt = args.format or ("json" if args.json else "text")
    is_skill = (root / "SKILL.md").is_file() and (root / "scripts" / "secret-rules.json").is_file()

    findings: list[dict] = []
    version = check_skill_profile(root, findings) if is_skill else None
    findings.extend(scan_tree(root))

    blocking = [f for f in findings if f["severity"] == "P0"]
    strict_hits = [f for f in findings if f["severity"] == "P1"]
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
        if not failed:
            counts = {s: sum(1 for f in findings if f["severity"] == s) for s in ("P0", "P1", "P2")}
            print(f"OK: checks passed for {root.name}" + (f" (v{version})" if version else "") + f" — P0={counts['P0']} P1={counts['P1']} P2={counts['P2']}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
