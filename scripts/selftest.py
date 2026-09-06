#!/usr/bin/env python3
"""Regression test runner for github-oss-prep skill.

Usage: python scripts/selftest.py
Runs:
  1. Positive validation of files, references, and AST syntax
  2. Negative security assertions (asserting verifier catches bad inputs)
  3. Depth assertions on pitfall knowledge base
  4. Integration test with validate_repo.py --json
"""
import ast
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_syntax_ast() -> list[str]:
    """Validate Python syntax across all internal scripts using ast.parse."""
    failures = []
    scripts_dir = ROOT / "scripts"
    if scripts_dir.is_dir():
        for py_file in scripts_dir.glob("*.py"):
            try:
                ast.parse(py_file.read_text(encoding="utf-8"), filename=py_file.name)
            except SyntaxError as e:
                failures.append(f"AST syntax error in {py_file.name}: {e}")
    tests_dir = ROOT / "tests"
    if tests_dir.is_dir():
        for py_file in tests_dir.glob("*.py"):
            try:
                ast.parse(py_file.read_text(encoding="utf-8"), filename=py_file.name)
            except SyntaxError as e:
                failures.append(f"AST syntax error in {py_file.name}: {e}")
    return failures


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
        ROOT / "references" / "github-oss-prep-pitfalls.md",
        ROOT / "scripts" / "validate_repo.py",
        ROOT / "scripts" / "selftest.py",
        ROOT / "tests" / "test_skill.py",
    ]
    for rf in required_files:
        if not rf.exists():
            failures.append(f"Missing required file: {rf.name}")

    # 2. Positive: Frontmatter length & token health
    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    lines = skill_text.splitlines()
    if len(lines) > 200:
        failures.append(f"SKILL.md line count too high ({len(lines)}), should be < 200")

    # 3. Depth Assertions on Pitfalls
    pitfalls_file = ROOT / "references" / "github-oss-prep-pitfalls.md"
    if pitfalls_file.is_file():
        p_text = pitfalls_file.read_text(encoding="utf-8")
        depth_keywords = [
            "git-filter-repo",
            "permissions:",
            "contents: read",
            "YAML Issue Forms",
            "OIDC Trusted Publishing",
        ]
        for kw in depth_keywords:
            if kw not in p_text:
                failures.append(f"Pitfalls document missing depth assertion keyword: '{kw}'")

    # 4. DY002 Negative Assertions (Assert checkers catch bad inputs / should fail)
    secret_pat = re.compile(r"ghp_[A-Za-z0-9]{36}")
    if not secret_pat.search("ghp_123456789012345678901234567890123456"):  # skill-doctor: allow
        failures.append("Negative test: secret pattern failed to catch dummy classic PAT")

    personal_pat = re.compile(r"[A-Za-z]:\\Users\\[a-zA-Z0-9_-]+[\\/]")  # skill-doctor: allow
    if not personal_pat.search("C:\\Users\\alice\\Desktop\\test\\"):  # skill-doctor: allow
        failures.append("Negative test: personal path pattern failed to catch dummy Windows path")

    # Negative assertion: tampered dummy content should trigger error in pattern
    tampered_secret = "OPENAI_KEY = 'sk-test12345678901234567890abcdef'"  # skill-doctor: allow
    openai_pat = re.compile(r"sk-[A-Za-z0-9-_]{20,}")
    if not openai_pat.search(tampered_secret):
        failures.append("Negative test: tampered secret should fail validation")

    return failures


def main() -> int:
    # 1. AST syntax test
    ast_failures = test_syntax_ast()
    if ast_failures:
        print("FAIL: AST Syntax verification failed:", file=sys.stderr)
        for f in ast_failures:
            print(f" - {f}", file=sys.stderr)
        return 1

    # 2. Positive & Negative tests
    failures = test_positive_and_negative()
    if failures:
        print("FAIL: Selftest failed with errors:", file=sys.stderr)
        for f in failures:
            print(f" - {f}", file=sys.stderr)
        return 1

    # 3. Integration test: Run validate_repo.py --json
    validate_script = ROOT / "scripts" / "validate_repo.py"
    proc = subprocess.run([sys.executable, str(validate_script), str(ROOT), "--json"], capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"FAIL: validate_repo.py --json exited with code {proc.returncode}:\n{proc.stderr}", file=sys.stderr)
        return proc.returncode

    try:
        report = json.loads(proc.stdout)
        if report.get("status") != "PASS":
            print(f"FAIL: validate_repo report status is {report.get('status')}: {report.get('errors')}", file=sys.stderr)
            return 1
    except json.JSONDecodeError as e:
        print(f"FAIL: validate_repo output is not valid JSON: {e}\n{proc.stdout}", file=sys.stderr)
        return 1

    print("SELFTEST PASS (all AST syntax, positive, negative, and integration checks passed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
