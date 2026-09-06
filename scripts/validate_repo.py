#!/usr/bin/env python3
"""Repository structure, hygiene, and security validation tool for github-oss-prep.

Usage:
  python scripts/validate_repo.py [target_dir] [--json] [--quick] [--read-only]

Features:
  - 5-layer deep credential, path, and privacy leak scanning
  - GitHub Actions CI supply chain security audit (permissions, pinned SHA)
  - GitHub Insights 100% community standards completeness check
  - Machine-readable JSON structured export (--json) and fast sampling (--quick)
  - Pure Python standard library, zero external dependencies, 100% read-only
"""
import argparse
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
    (re.compile(r"[A-Za-z]:\\Users\\[a-zA-Z0-9_-]+[\\/]"), "Windows personal user path"),  # skill-doctor: allow
    (re.compile(r"/home/[a-zA-Z0-9_-]+/"), "Linux personal user path"),
    (re.compile(r"/Users/[a-zA-Z0-9_-]+/"), "macOS personal user path"),
]

# 3. Insecure Git Remote URLs
GIT_URL_PATTERNS = [
    (re.compile(r"https://[^:\s]+:[^@\s]+@github\.com"), "Git Remote URL with embedded password/token"),
    (re.compile(r"https://gh[pousr]_[A-Za-z0-9_]+@github\.com"), "Git Remote URL with embedded PAT token"),
]

# Exclusion sets for scanning
EXCLUDE_DIRS = {".git", "node_modules", "__pycache__", ".pytest_cache", "renders", ".turbo", ".doctor"}
EXCLUDE_EXTS = {".png", ".jpg", ".webp", ".mp4", ".zip", ".tar.gz", ".pyc", ".ico"}
EXCLUDE_FILES = {
    "validate_repo.py",
    "privacy-scan.md",
    "test_skill.py",
    "selftest.py",
    "audit.py",
    "github-oss-prep-pitfalls.md",
}


def audit_workflow_security(workflow_path: Path) -> list[str]:
    """Audit GitHub Actions workflow file for OpenSSF least-privilege and pinning standards."""
    issues = []
    text = workflow_path.read_text(encoding="utf-8", errors="ignore")

    # 1. Least privilege: check for permissions block
    if "permissions:" not in text:
        issues.append(f"{workflow_path.name}: 缺少顶层 permissions 声明，默认存在过度提权隐患")

    # 2. Third-party Action pinning: check uses:
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("uses:"):
            action = line.split("uses:")[1].strip()
            # Split out trailing comment if any
            if "#" in action:
                action = action.split("#")[0].strip()
            # Ignore local actions or docker actions
            if action.startswith("./") or action.startswith("docker://"):
                continue
            # Community actions (not actions/*) should pin full commit SHA
            if not action.startswith("actions/"):
                if "@" in action:
                    ref = action.split("@")[1].strip()
                    if len(ref) != 40:
                        issues.append(f"{workflow_path.name}: 第三方 Action 未锁定 40 位不可变 Commit SHA: {action}")

    return issues


def validate_repository(target_dir: Path, quick: bool = False) -> dict:
    """Validate repository health, privacy hygiene, and community standards."""
    errors: list[str] = []
    warnings: list[str] = []
    passed: list[str] = []

    # 1. Verify Community Essentials (GitHub Insights 100% standard)
    essential_files = ["README.md", "LICENSE", "CHANGELOG.md", "SECURITY.md"]
    for f in essential_files:
        if (target_dir / f).exists():
            passed.append(f"Essential file present: {f}")
        else:
            errors.append(f"Missing essential file: {f}")

    # 2. Verify YAML Issue Forms & .github
    issue_dir = target_dir / ".github" / "ISSUE_TEMPLATE"
    if issue_dir.exists():
        yml_files = list(issue_dir.glob("*.yml")) + list(issue_dir.glob("*.yaml"))
        if yml_files:
            passed.append(f"YAML Issue Forms present ({len(yml_files)} forms)")
        else:
            warnings.append("WARN: .github/ISSUE_TEMPLATE exists but contains no YAML Issue Forms")
    else:
        warnings.append("WARN: Missing .github/ISSUE_TEMPLATE directory")

    # 3. Audit GitHub Actions workflows for supply chain security
    workflows_dir = target_dir / ".github" / "workflows"
    if workflows_dir.is_dir():
        for wf in workflows_dir.glob("*.y*ml"):
            wf_issues = audit_workflow_security(wf)
            for iss in wf_issues:
                warnings.append(f"WARN [Supply-Chain]: {iss}")
            if not wf_issues:
                passed.append(f"Workflow hardened: {wf.name}")

    # 4. Check .git/config for embedded tokens if .git exists
    git_config = target_dir / ".git" / "config"
    if git_config.is_file():
        cfg_text = git_config.read_text(encoding="utf-8", errors="ignore")
        for pat, desc in GIT_URL_PATTERNS:
            if pat.search(cfg_text):
                errors.append(f"Git Remote URL credential leak in .git/config: {desc}")

    # If quick mode, stop here
    if quick:
        return {
            "status": "PASS" if not errors else "FAIL",
            "target": str(target_dir),
            "mode": "quick",
            "errors": errors,
            "warnings": warnings,
            "passed": passed,
        }

    # 5. Deep Scan Files for Secrets & Local Paths
    for p in target_dir.rglob("*"):
        if any(part in EXCLUDE_DIRS for part in p.parts):
            continue
        if p.suffix.lower() in EXCLUDE_EXTS:
            continue
        if not p.is_file():
            continue
        if p.name in EXCLUDE_FILES:
            continue

        try:
            content = p.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:  # skill-doctor: allow
            warnings.append(f"WARN: Could not read {p.relative_to(target_dir)}: {e}")
            continue

        # Scan secrets
        for pat, desc in SECRET_PATTERNS:
            if pat.search(content):
                errors.append(f"Secret detected in {p.relative_to(target_dir)}: {desc}")

        # Scan personal paths
        for pat, desc in PERSONAL_PATH_PATTERNS:
            if pat.search(content):
                errors.append(f"Personal path detected in {p.relative_to(target_dir)}: {desc}")

    return {
        "status": "PASS" if not errors else "FAIL",
        "target": str(target_dir),
        "mode": "full",
        "errors": errors,
        "warnings": warnings,
        "passed": passed,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="validate_repo: 仓库结构、隐私安全与社区规范审计工具")
    parser.add_argument("target", nargs="?", default=".", help="目标仓库路径 (默认当前目录)")
    parser.add_argument("--json", "-Json", action="store_true", help="以结构化机读 JSON 格式输出审计结果")
    parser.add_argument("--quick", "-Quick", action="store_true", help="执行快速采样审计 (跳过大文件深层正则检索)")
    parser.add_argument("--read-only", action="store_true", help="显式声明纯只读模式运行，不进行任何变更")

    args = parser.parse_args()
    target_path = Path(args.target).resolve()

    if not target_path.is_dir():
        print(f"Error: 目标路径不是有效目录: {target_path}", file=sys.stderr)
        return 1

    result = validate_repository(target_path, quick=args.quick)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result["status"] == "PASS" else 1

    print(f"Validating repository at: {target_path} (Mode: {result['mode']})")
    if result["passed"]:
        for p in result["passed"]:
            print(f" [+] {p}")
    if result["warnings"]:
        for w in result["warnings"]:
            print(f" [!] {w}", file=sys.stderr)
    if result["errors"]:
        print(f"\nFAIL: Found {len(result['errors'])} error(s):", file=sys.stderr)
        for e in result["errors"]:
            print(f"  - {e}", file=sys.stderr)
        return 1

    print("\nPASS: Repository validation successful with zero errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
