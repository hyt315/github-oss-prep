#!/usr/bin/env python3
"""Dependency-free repository checks for github-oss-prep."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".py", ".txt"}
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


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> int:
    parser = argparse.ArgumentParser(description="Repository validation tool")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()
    
    # Use ROOT directly, no need for positional argument
    errors = []
    
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")
    
    if errors:
        if args.json:
            print(json.dumps({"status": "FAIL", "errors": errors}, ensure_ascii=False))
            return 1
        else:
            for e in errors:
                print(f"ERROR: {e}", file=sys.stderr)
            return 1
    
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not re.match(r"^---\n(?s:.*?)\n---\n", skill):
        fail("SKILL.md frontmatter is missing or malformed")
    frontmatter = skill.split("---", 2)[1]
    for key in ("name:", "description:"):
        if key not in frontmatter:
            fail(f"SKILL.md frontmatter is missing {key[:-1]}")
    
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    version = manifest["version"]
    # README may use either a static version badge (version-x.y.z-) or a dynamic
    # release badge (github/v/release); the manifest is the single source of truth.
    if f"## [{version}]" not in changelog:
        fail(f"CHANGELOG does not contain manifest version {version}")
    badge = re.search(r"version-([0-9]+\.[0-9]+\.[0-9]+)-", readme)
    if badge and badge.group(1) != version:
        fail("README static badge version does not match manifest.json")
    
    secret_patterns = {
        "GitHub classic PAT": re.compile(r"ghp_[A-Za-z0-9]{30,}"),
        "GitHub fine-grained PAT": re.compile(r"github_pat_[A-Za-z0-9_]{30,}"),
        "OpenAI-style key": re.compile(r"sk-[A-Za-z0-9]{32,}"),
    }
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix not in TEXT_SUFFIXES:
            continue
        # Skip test files that contain dummy secrets for testing
        if path.name in ("selftest.py", "test_skill.py"):
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in secret_patterns.items():
            if pattern.search(content):
                errors.append(f"possible {label} in {path.relative_to(ROOT)}")
    
    for placeholder in ("<owner>", "<repo>"):
        if placeholder in readme:
            errors.append(f"unresolved README placeholder: {placeholder}")
    
    if errors:
        if args.json:
            print(json.dumps({"status": "FAIL", "errors": errors}, ensure_ascii=False))
            return 1
        else:
            for e in errors:
                print(f"ERROR: {e}", file=sys.stderr)
            return 1
    
    if args.json:
        print(json.dumps({"status": "PASS", "version": version}, ensure_ascii=False))
    else:
        print(f"OK: repository checks passed for v{version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
