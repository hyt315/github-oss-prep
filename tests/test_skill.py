#!/usr/bin/env python3
"""Stdlib-only test entry (no third-party test runner required).

The real checks live in scripts/selftest.py (fixture regressions + repository
validation). This module keeps a stable `python -m unittest discover -s tests`
entry for CI without duplicating scanner rules or assertions.
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SkillTests(unittest.TestCase):
    def test_selftest_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "selftest.py")],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        self.assertEqual(result.returncode, 0, f"selftest failed:\n{result.stdout}\n{result.stderr}")
        self.assertIn("SELFTEST PASS", result.stdout)

    def test_leaked_fixture_is_rejected(self) -> None:
        """The validator must FAIL on the leaked fixture (P0 present)."""
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "validate_repo.py"),
                str(ROOT / "tests" / "fixtures" / "leaked-repo"),
                "--json",
            ],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        self.assertEqual(result.returncode, 1, "validator must fail on the leaked fixture")
        self.assertIn('"status": "FAIL"', result.stdout)

    def test_clean_fixture_is_accepted(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "validate_repo.py"),
                str(ROOT / "tests" / "fixtures" / "clean-repo"),
                "--json",
            ],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        self.assertEqual(result.returncode, 0, f"validator must pass on the clean fixture:\n{result.stdout}")


if __name__ == "__main__":
    unittest.main()
