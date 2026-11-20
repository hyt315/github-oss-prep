#!/usr/bin/env python3
"""Unified stdlib unittest suite for github-oss-prep.

Single test entry (`python -m unittest discover -s tests -v`). Imports rules from
scripts/secret-rules.json via validate_repo rather than duplicating regexes.
"""

from __future__ import annotations

import ast
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_repo  # noqa: E402

FIXTURE_LEAK = ROOT / "tests" / "fixtures" / "leaked-repo"
FIXTURE_CLEAN = ROOT / "tests" / "fixtures" / "clean-repo"


class SkillValidationTests(unittest.TestCase):
    def test_syntax_ast(self) -> None:
        for pattern in ("scripts/*.py", "tests/*.py"):
            for path in ROOT.glob(pattern):
                ast.parse(path.read_text(encoding="utf-8"), filename=str(path))

    def test_skill_md_line_budget(self) -> None:
        lines = len((ROOT / "SKILL.md").read_text(encoding="utf-8").splitlines())
        self.assertLessEqual(lines, 180, f"SKILL.md grew to {lines} lines (>180); keep instructions concise")

    def test_rules_single_source(self) -> None:
        """Known credential regexes must exist only in scripts/secret-rules.json."""
        signatures = [
            "gh[pousr]_[A-Za-z0-9]{36",
            "AKIA|ASIA",
            "pypi-AgEIcHlwaS5vcmc",
            "BEGIN (?:[A-Z0-9]+ )?PRIVATE KEY",
        ]
        offenders = []
        for path in ROOT.rglob("*"):
            if not path.is_file() or {".git", "__pycache__"} & set(path.parts) or path.name == "secret-rules.json":
                continue
            if path.name == Path(__file__).name:
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
        self.assertEqual(offenders, [], f"duplicated scanner patterns found: {offenders}")

    def test_leaked_fixture_is_rejected(self) -> None:
        findings = validate_repo.scan_tree(FIXTURE_LEAK, skip_self_fixtures=False)
        ids = {f["id"] for f in findings if f["severity"] == "P0"}
        expected = {"openai-style-key", "aws-access-key-id", "private-key-block"}
        self.assertTrue(expected <= ids, f"scanner missed {expected - ids}; findings={sorted(ids)}")

    def test_clean_fixture_passes(self) -> None:
        findings = [f for f in validate_repo.scan_tree(FIXTURE_CLEAN, skip_self_fixtures=False) if f["severity"] == "P0"]
        self.assertEqual(findings, [], f"false positives in clean fixture: {findings}")

    def test_self_repo_validation_passes_strict(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_repo.py"), "--strict", "--json"],
            capture_output=True, text=True, cwd=ROOT,
        )
        payload = json.loads(result.stdout)
        self.assertEqual(payload["status"], "PASS", f"validate_repo failed: {payload}")
        self.assertEqual(result.returncode, 0)

    def test_user_repo_tests_fixtures_is_scanned(self) -> None:
        """v3.4.0 fix: tests/fixtures/ in a user repository must NOT be silently skipped."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "tests" / "fixtures").mkdir(parents=True)
            key = "sk-proj-" + "AbCdEfGh1234567890" * 2
            (root / "tests" / "fixtures" / "secret.txt").write_text(key + "\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "validate_repo.py"), tmp, "--strict", "--json"],
                capture_output=True, text=True,
            )
            payload = json.loads(result.stdout)
        self.assertEqual(result.returncode, 1, "secret inside user repo tests/fixtures/ was missed")
        self.assertTrue(any(f["id"] == "openai-style-key" for f in payload["findings"]), payload)

    def test_target_repo_reports_missing_baseline_files(self) -> None:
        """v3.4.0 fix: target repos report missing README/LICENSE/.gitignore as P2."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "main.py").write_text("print('hi')\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "validate_repo.py"), tmp, "--json"],
                capture_output=True, text=True,
            )
            payload = json.loads(result.stdout)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(set(payload["community_files"]["missing_baseline"]), {"README.md", "LICENSE", ".gitignore"})

    def test_ci_security_checks(self) -> None:
        """CI checks catch missing permissions, write-all, pull_request_target, script injection, and unpinned SHAs."""
        with tempfile.TemporaryDirectory() as tmp:
            wf = Path(tmp) / ".github" / "workflows"
            wf.mkdir(parents=True)
            (wf / "bad.yml").write_text(
                "on: pull_request_target\npermissions: write-all\njobs:\n  a:\n    steps:\n"
                "      - uses: actions/checkout@v4\n"
                "      - run: echo ${{ github.event.issue.title }}\n",
                encoding="utf-8",
            )
            (wf / "good.yml").write_text(
                "on: push\npermissions:\n  contents: read\njobs:\n  a:\n    steps:\n"
                "      - uses: actions/checkout@" + "a" * 40 + " # v7\n"
                "      - uses: ./local-action\n"
                "      - run: echo ok\n",
                encoding="utf-8",
            )
            found = {(Path(f["file"]).name, f["id"]) for f in validate_repo.scan_tree(Path(tmp))}
        self.assertIn(("bad.yml", "ci-pin-sha"), found)
        self.assertIn(("bad.yml", "ci-permissions-write-all"), found)
        self.assertIn(("bad.yml", "ci-pull-request-target"), found)
        self.assertIn(("bad.yml", "ci-script-injection"), found)
        self.assertEqual({i for n, i in found if n == "good.yml" and i.startswith("ci-")}, set())

    def test_crlf_and_frontmatter_spec(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_text = "---\nname: demo-skill\ndescription: Demo\nmetadata:\n  version: \"1.0.0\"\n---\n# Demo\n"
            (root / "SKILL.md").write_bytes(skill_text.replace("\n", "\r\n").encode("utf-8"))
            findings: list[dict] = []
            ver = validate_repo.check_skill_frontmatter(root, findings)
        self.assertEqual(ver, "1.0.0")
        self.assertEqual(findings, [])

    def test_anchor_slug_matches_github(self) -> None:
        self.assertEqual(validate_repo._slug("📖 这是什么？"), "-这是什么")
        self.assertEqual(validate_repo._slug("Quick Start"), "quick-start")

    def test_scanner_regressions_and_calibration(self) -> None:
        rules = validate_repo.load_rules()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "build" / "proj"
            (root / ".git").mkdir(parents=True)
            aws = "AKIA" + "Q3EGRJ7XNZ5VW2LM"
            (root / "a.txt").write_text(aws + "\n", encoding="utf-8")
            (root / "b.md").write_text("risk-assessment-framework-tools\n", encoding="utf-8")
            (root / "c.md").write_text("git -c http.proxy=http://127.0.0.1:" + "7897 push\n", encoding="utf-8")
            (root / ".env.local").write_text("X=1\n", encoding="utf-8")
            tok = "ghp_" + "Zq8" * 12
            (root / ".git" / "config").write_text('[remote "origin"]\n\turl = https://' + tok + "@github.com/o/r.git\n", encoding="utf-8")
            quiet = (
                "```bash\ngh repo clone <owner>/<repo>\n```\n"
                "Copy to C:\\Users\\<user>\\AppData and C:\\Users\\YourName\\x and C:\\Users\\%USERNAME%\\y\n"
                "System: C:\\Windows\\System32\\ and C:\\ProgramData\\Foo\\ and C:\\Users\\Public\\z\n"
                "Unix: /home/user/proj/ and /Users/you/code/ and /home/runner/work/\n"
                "Mail security@example.com or someone@users.noreply.github.com\n"
            )
            loud = (
                "C:\\Users\\" + "zhangwei\\Desktop\n"
                "/home/" + "zhangwei/proj/\n"
                "Contact zhang.san@" + "163.com or 1381234" + "5678\n"
            )
            (root / "quiet.md").write_text(quiet, encoding="utf-8")
            (root / "loud.md").write_text(loud, encoding="utf-8")
            found = validate_repo.scan_tree(root, rules)
        pairs = {(Path(f["file"]).name, f["id"]) for f in found}
        self.assertIn(("a.txt", "aws-access-key-id"), pairs)
        self.assertEqual({i for n, i in pairs if n == "b.md"}, set())
        self.assertIn(("c.md", "local-proxy-config"), pairs)
        self.assertIn((".env.local", "blocked-file"), pairs)
        self.assertTrue(("config", "github-classic-pat") in pairs or ("config", "credential-in-url") in pairs)
        noisy = [f for f in found if f["file"].endswith("quiet.md") and f["severity"] in {"P0", "P1"}]
        self.assertEqual(noisy, [])
        loud_ids = {f["id"] for f in found if f["file"].endswith("loud.md") and f["severity"] == "P1"}
        self.assertTrue({"windows-user-profile-path", "unix-home-path", "personal-email", "cn-mobile-number"} <= loud_ids)

    def test_streaming_history_scan_and_p1_report_only(self) -> None:
        if not shutil.which("git"):
            self.skipTest("git not available")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            run = lambda *a: subprocess.run(["git", "-C", tmp, *a], check=True, capture_output=True)  # noqa: E731
            run("init", "-q")
            run("config", "user.name", "t")
            run("config", "user.email", "t@users.noreply.github.com")
            (root / "x.md").write_text("see /home/" + "zhangwei/proj/\n", encoding="utf-8")
            run("add", ".")
            run("commit", "-qm", "a")
            (root / "x.md").write_text("clean\n", encoding="utf-8")
            run("commit", "-qam", "b")
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "validate_repo.py"), tmp, "--strict", "--history", "--json"],
                capture_output=True, text=True,
            )
            payload = json.loads(result.stdout)
        self.assertTrue(any(f["id"] == "unix-home-path" for f in payload["findings"]), payload)
        self.assertEqual(payload["status"], "PASS")
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
