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


def test_ci_pin_check() -> None:
    """CI-PIN: tag-pinned actions and a missing permissions block are reported; SHA pins are not."""
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        wf = Path(tmp) / ".github" / "workflows"
        wf.mkdir(parents=True)
        (wf / "bad.yml").write_text("on: push\njobs:\n  a:\n    steps:\n      - uses: actions/checkout@v4\n", encoding="utf-8")
        (wf / "good.yml").write_text(
            "on: push\npermissions:\n  contents: read\njobs:\n  a:\n    steps:\n"
            "      - uses: actions/checkout@" + "a" * 40 + " # v4\n      - uses: ./local-action\n", encoding="utf-8")
        found = {(Path(f["file"]).name, f["id"]) for f in validate_repo.scan_tree(Path(tmp))}
    assert ("bad.yml", "ci-pin-sha") in found, found
    assert ("bad.yml", "ci-pin-permissions") in found, found
    assert not {i for n, i in found if n == "good.yml" and i.startswith("ci-pin")}, found


def test_crlf_and_metadata_version() -> None:
    """A CRLF SKILL.md (Windows checkout) with metadata.version must parse and match manifest."""
    import shutil
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for rel in validate_repo.REQUIRED + ["manifest.json", "CHANGELOG.md"]:
            dst = root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(ROOT / rel, dst)
        skill = (root / "SKILL.md").read_text(encoding="utf-8")
        (root / "SKILL.md").write_bytes(skill.replace("\n", "\r\n").encode("utf-8"))
        findings = []
        validate_repo.check_skill_profile(root, findings)
    bad = [f for f in findings if f["id"] in {"frontmatter", "version-mismatch"}]
    assert not bad, bad


def test_anchor_slug_matches_github() -> None:
    assert validate_repo._slug("📖 这是什么？") == "-这是什么"
    assert validate_repo._slug("Quick Start") == "quick-start"
    assert validate_repo._slug("#快速开始-quick-start".lstrip("#")) == validate_repo._slug("快速开始 Quick Start")


def test_scanner_regressions() -> None:
    """v3.3.2 fixes: target under build/, sk- word boundary, local proxy, .env variants, .git/config."""
    import tempfile
    rules = validate_repo.load_rules()
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "build" / "proj"  # a target that itself lives under a skip_dirs name
        (root / ".git").mkdir(parents=True)
        aws = "AKIA" + "Q3EGRJ7XNZ5VW2LM"
        (root / "a.txt").write_text(aws + "\n", encoding="utf-8")
        (root / "b.md").write_text("risk-assessment-framework-tools and task-runner-for-continuous-work\n", encoding="utf-8")
        (root / "c.md").write_text("git -c http.proxy=http://127.0.0.1:" + "7897 push\n", encoding="utf-8")
        (root / ".env.local").write_text("X=1\n", encoding="utf-8")
        tok = "ghp_" + "Zq8" * 12
        (root / ".git" / "config").write_text('[remote "origin"]\n\turl = https://' + tok + "@github.com/o/r.git\n", encoding="utf-8")
        found = {(Path(f["file"]).name, f["id"]) for f in validate_repo.scan_tree(root, rules)}
    assert ("a.txt", "aws-access-key-id") in found, found
    assert not {i for n, i in found if n == "b.md"}, found
    assert ("c.md", "local-proxy-config") in found and ("c.md", "loopback-proxy-port") in found, found
    assert ("config", "github-classic-pat") in found or ("config", "credential-in-url") in found, found
    assert ("a.txt", "blocked-file") not in found and (".env.local", "blocked-file") in found, found


def test_history_scan_finds_removed_leak() -> None:
    """A leak deleted in a later commit is still reported by --history."""
    import shutil
    import tempfile
    if not shutil.which("git"):
        return
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        run = lambda *a: subprocess.run(["git", "-C", tmp, *a], check=True, capture_output=True)  # noqa: E731
        run("init", "-q")
        run("config", "user.name", "t")
        run("config", "user.email", "t@users.noreply.github.com")
        (root / "x.md").write_text("proxy 127.0.0.1:" + "7897\n", encoding="utf-8")
        run("add", ".")
        run("commit", "-qm", "a")
        (root / "x.md").write_text("clean\n", encoding="utf-8")
        run("commit", "-qam", "b")
        ids = {f["id"] for f in validate_repo.scan_history(root)}
    assert "loopback-proxy-port" in ids, ids
    assert "history-author-email" not in ids, ids


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
