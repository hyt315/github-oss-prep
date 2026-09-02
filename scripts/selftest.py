#!/usr/bin/env python3
"""Regression test runner for github-oss-prep skill.

Usage: python scripts/selftest.py
Runs positive validation and negative security assertions.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_positive_and_negative() -> list[str]:
    failures: list[str] = []

    # 1. Positive: Core files present
    required_files = [
        ROOT / "SKILL.md",
        ROOT / "README.md",
        ROOT / "README.en.md",
        ROOT / "manifest.json",
        ROOT / "references" / "readme-template.md",
        ROOT / "references" / "privacy-scan.md",
        ROOT / "references" / "community-templates.md",
        ROOT / "references" / "release-and-distribution.md",
        ROOT / "scripts" / "validate_repo.py",
    ]
    for rf in required_files:
        if not rf.exists():
            failures.append(f"Missing required file: {rf.name}")

    # 2. Positive: Frontmatter length & token health
    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if len(skill_text.splitlines()) > 200:
        failures.append(f"SKILL.md line count too high ({len(skill_text.splitlines())}), should be < 200")

    # 3. Negative assertions (ensure checkers reject invalid inputs)
    secret_pat = re.compile(r"ghp_[A-Za-z0-9]{36}")
    if not secret_pat.search("ghp_123456789012345678901234567890123456"):
        failures.append("Negative test: secret pattern failed to catch dummy classic PAT")

    personal_pat = re.compile(r"C:\\Users\\[a-zA-Z0-9_-]+\\")  # skill-doctor: allow
    if not personal_pat.search("C:\\Users\\alice\\Desktop\\test"):  # skill-doctor: allow
        failures.append("Negative test: personal path pattern failed to catch dummy Windows path")

    return failures


def main() -> int:
    failures = test_positive_and_negative()
    if failures:
        print("FAIL: Selftest failed with errors:", file=sys.stderr)
        for f in failures:
            print(f" - {f}", file=sys.stderr)
        return 1

    # Run validate_repo.py
    proc = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_repo.py"), str(ROOT)], capture_output=True, text=True)
    sys.stdout.write(proc.stdout)
    sys.stderr.write(proc.stderr)
    if proc.returncode != 0:
        return proc.returncode

    print("SELFTEST PASS (all positive and negative checks passed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
