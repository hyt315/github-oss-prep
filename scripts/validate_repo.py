#!/usr/bin/env python3
"""Repository structure, hygiene, and security validation tool for github-oss-prep.

Usage: python scripts/validate_repo.py [target_dir]
Exits 0 on SUCCESS, non-zero on failure.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 1. Credentials & Secrets patterns
SECRET_PATTERNS = [
    (re.compile(r"sk-[A-Za-z0-9-_]{20,}"), "OpenAI API Key pattern"),
    (re.compile(r"sk-ant-[A-Za-z0-9-_]{20,}"), "Anthropic API Key pattern"),
    (re.compile(r"ghp_[A-Za-z0-9]{36}"), "GitHub Classic PAT pattern"),
    (re.compile(r"github_pat_[A-Za-z0-9_]{82}"), "GitHub Fine-Grained PAT pattern"),
    (re.compile(r"-----BEGIN (?:RSA|OPENSSH|EC|DSA) PRIVATE KEY-----"), "SSH Private Key"),
]

# 2. Local personal path patterns (skill-doctor: allow)
PERSONAL_PATH_PATTERNS = [
    (re.compile(r"C:\\Users\\[a-zA-Z0-9_-]+\\"), "Windows personal user path"),  # skill-doctor: allow
    (re.compile(r"/home/[a-zA-Z0-9_-]+/"), "Linux personal user path"),
    (re.compile(r"/Users/[a-zA-Z0-9_-]+/"), "macOS personal user path"),
]

# Exclusion sets for scanning
EXCLUDE_DIRS = {".git", "node_modules", "__pycache__", ".pytest_cache", "renders", ".turbo"}
EXCLUDE_EXTS = {".png", ".jpg", ".webp", ".mp4", ".zip", ".tar.gz", ".pyc"}


def validate_repository(target_dir: Path) -> list[str]:
    errors: list[str] = []
    warnings: list[str] = []

    # 1. Verify Community Essentials
    essential_files = ["README.md", "LICENSE", "CHANGELOG.md"]
    for f in essential_files:
        if not (target_dir / f).exists():
            errors.append(f"Missing essential file: {f}")

    # 2. Verify YAML Issue Forms & .github
    issue_dir = target_dir / ".github" / "ISSUE_TEMPLATE"
    if issue_dir.exists():
        yml_files = list(issue_dir.glob("*.yml"))
        if not yml_files:
            warnings.append("WARN: .github/ISSUE_TEMPLATE exists but contains no YAML Issue Forms")
    else:
        warnings.append("WARN: Missing .github/ISSUE_TEMPLATE directory")

    # 3. Deep Scan Files for Secrets & Local Paths
    for p in target_dir.rglob("*"):
        if any(part in EXCLUDE_DIRS for part in p.parts):
            continue
        if p.suffix.lower() in EXCLUDE_EXTS:
            continue
        if not p.is_file():
            continue

        try:
            content = p.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            warnings.append(f"WARN: Could not read {p.relative_to(target_dir)}: {e}")
            continue

        # Skip scanning selftest / validate scripts for their own regex patterns
        if p.name in {"validate_repo.py", "privacy-scan.md", "test_skill.py", "selftest.py", "audit.py"}:
            continue

        # Scan secrets
        for pat, desc in SECRET_PATTERNS:
            if pat.search(content):
                errors.append(f"Secret detected in {p.relative_to(target_dir)}: {desc}")

        # Scan personal paths
        for pat, desc in PERSONAL_PATH_PATTERNS:
            if pat.search(content):
                errors.append(f"Personal path detected in {p.relative_to(target_dir)}: {desc}")

    for w in warnings:
        print(w, file=sys.stderr)

    return errors


def main() -> int:
    target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT
    print(f"Validating repository at: {target}")
    errors = validate_repository(target)
    if errors:
        print(f"FAIL: Found {len(errors)} error(s):", file=sys.stderr)
        for e in errors:
            print(f" - {e}", file=sys.stderr)
        return 1
    print("PASS: Repository validation successful with zero errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
