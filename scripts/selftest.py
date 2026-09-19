#!/usr/bin/env python3
"""Regression self-test for github-oss-prep.

Design rule: this file must NOT re-declare scanner regexes. It imports the
single source of truth (scripts/secret-rules.json via validate_repo) and
proves that real-format credentials are actually detected.
"""

from __future__ import annotations

import ast
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_repo  # noqa: E402

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "README.en.md",
    "LICENSE",
    "SECURITY.md",
    "CHANGELOG.md",
    "manifest.json",
    "scripts/secret-rules.json",
    "scripts/validate_repo.py",
    "tests/fixtures/leaked-repo/SECURITY.md",
    "tests/fixtures/clean-repo/README.md",
    "references/readme-template.md",
    "references/privacy-scan.md",
    "references/github-oss-prep-pitfalls.md",
]

FIXTURE_LEAK = ROOT / "tests" / "fixtures" / "leaked-repo"
FIXTURE_CLEAN = ROOT / "tests" / "fixtures" / "clean-repo"


def test_syntax_ast() -> None:
    for pattern in ("scripts/*.py", "tests/*.py"):
        for path in ROOT.glob(pattern):
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def test_required_files() -> None:
    missing = [name for name in REQUIRED_FILES if not (ROOT / name).is_file()]
    assert not missing, f"missing files: {missing}"


def test_skill_md_line_budget() -> None:
    lines = len((ROOT / "SKILL.md").read_text(encoding="utf-8").splitlines())
    assert lines <= 300, f"SKILL.md grew to {lines} lines (>300); move detail into references/"


def test_rules_single_source() -> None:
    """Known credential regexes must exist only in scripts/secret-rules.json."""
    signatures = ["gh[pousr]_[A-Za-z0-9]{36", "AKIA|ASIA", "pypi-AgEIcHlwaS5vcmc", "BEGIN (?:[A-Z0-9]+ )?PRIVATE KEY"]
    offenders = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.name == "secret-rules.json":
            continue
        if path.name == Path(__file__).name:  # this test names the signatures on purpose
            continue
        if path.suffix.lower() in {".png", ".jpg", ".pdf", ".zip"}:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for sig in signatures:
            if sig in text:
                offenders.append(f"{path.relative_to(ROOT)}: {sig}")
    assert not offenders, f"duplicated scanner patterns found: {offenders}"


def test_leaked_fixture_is_detected() -> None:
    """P0 regression: real-format credentials in a repo must be caught."""
    findings = validate_repo.scan_tree(FIXTURE_LEAK)
    ids = {f["id"] for f in findings if f["severity"] == "P0"}
    expected = {"openai-style-key", "aws-access-key-id", "private-key-block"}
    missing = expected - ids
    assert not missing, f"scanner missed {missing} in leaked fixture; findings={sorted(ids)}"


def test_clean_fixture_passes() -> None:
    findings = [f for f in validate_repo.scan_tree(FIXTURE_CLEAN) if f["severity"] == "P0"]
    assert not findings, f"false positives in clean fixture: {findings}"


def test_repo_validation_integration() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_repo.py"), "--json"],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    payload = json.loads(result.stdout)
    assert payload["status"] == "PASS", f"validate_repo failed: {payload}"
    assert result.returncode == 0, f"validate_repo exited {result.returncode}"


def main() -> int:
    checks = [value for name, value in sorted(globals().items()) if name.startswith("test_") and callable(value)]
    failed = []
    for check in checks:
        try:
            check()
            print(f"PASS {check.__name__}")
        except AssertionError as exc:
            failed.append(check.__name__)
            print(f"FAIL {check.__name__}: {exc}")
        except Exception as exc:  # noqa: BLE001
            failed.append(check.__name__)
            print(f"ERROR {check.__name__}: {exc!r}")
    if failed:
        print(f"\nSELFTEST FAIL ({len(failed)}/{len(checks)} failed)")
        return 1
    print(f"\nSELFTEST PASS ({len(checks)}/{len(checks)} checks passed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
