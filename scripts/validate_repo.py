#!/usr/bin/env python3
"""Dependency-free repository checks for github-oss-prep."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
# 扫描所有文本型后缀（含源码与 .env，覆盖真实泄漏高发区）；不满足此名单的按二进制跳过
TEXT_SUFFIXES = {
    ".md", ".yaml", ".yml", ".json", ".py", ".txt",
    ".toml", ".ini", ".cfg", ".env", ".sh", ".js", ".ts", ".jsx", ".tsx",
    ".go", ".rs", ".c", ".cpp", ".h", ".cs", ".java", ".rb", ".php", ".rb",
    ".properties", ".gitattributes", ".gitignore", ".ps1",
}
# 各项目类型的强制文件（对齐 SKILL.md 项目类型速查表）
# 文档项目 COC/SECURITY/CHANGELOG 可选，故不放进 REQUIRED
REQUIRED = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "REFERENCES_OK",  # 占位：实际校验在下方循环展开
]
# 按类型区别的必选文件（SKILL.md:182-186 速查表对齐）
TYPE_REQUIRED = {
    "skill": ["references/pr-and-release-workflow.md", "references/discovery-and-promotion.md"],
    "code": ["CHANGELOG.md"],
    "docs": [],  # 文档项目 COC/SECURITY/CHANGELOG 均可选
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def detect_type(root: Path) -> str:
    """按 SKILL.md 1.2 识别项目类型。"""
    if (root / "SKILL.md").is_file():
        return "skill"
    if any((root / f).is_file() for f in ("package.json", "setup.py", "Cargo.toml", "pyproject.toml")):
        return "code"
    return "docs"


# 1) 强制文件存在性（对自身仓库：skill 类型）
_type = detect_type(ROOT)
for relative in [r for r in REQUIRED if r != "REFERENCES_OK"]:
    if not (ROOT / relative).is_file():
        fail(f"missing required file: {relative}")
for relative in TYPE_REQUIRED[_type]:
    if not (ROOT / relative).is_file():
        fail(f"missing required file ({_type}): {relative}")

# 2) SKILL.md frontmatter
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
if not re.match(r"^---\n(?s:.*?)\n---\n", skill):
    fail("SKILL.md frontmatter is missing or malformed")
frontmatter = skill.split("---", 2)[1]
for key in ("name:", "description:"):
    if key not in frontmatter:
        fail(f"SKILL.md frontmatter is missing {key[:-1]}")

# 3) 版本一致性（README 徽章 ↔ CHANGELOG ↔ Release 链接；CHANGELOG 缺失时容错）
readme = (ROOT / "README.md").read_text(encoding="utf-8")
badge = re.search(r"version-([0-9]+\.[0-9]+\.[0-9]+)-", readme)
version = badge.group(1) if badge else ""
if not badge:
    fail("README version badge not found")
if f"releases/tag/v{version}" not in readme:
    fail("README badge link does not match badge version")
changelog_path = ROOT / "CHANGELOG.md"
if changelog_path.is_file():
    changelog = changelog_path.read_text(encoding="utf-8")
    if f"## [{version}]" not in changelog:
        fail("CHANGELOG does not contain README badge version")
elif _type in ("code", "skill"):
    fail(f"missing CHANGELOG.md ({_type} project)")

# 4) 密钥扫描：覆盖 TEXT_SUFFIXES 内全部文本 + .env（含任何后缀的单层 .env 文件）
secret_patterns = {
    "GitHub classic PAT": re.compile(r"ghp_[A-Za-z0-9]{30,}"),
    "GitHub fine-grained PAT": re.compile(r"github_pat_[A-Za-z0-9_]{30,}"),
    "OpenAI-style key": re.compile(r"sk-[A-Za-z0-9]{32,}"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "Private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "Generic .env assignment": re.compile(r"(?m)^\s*(?:[A-Z][A-Z0-9_]{2,})\s*=\s*[\"']?[A-Za-z0-9_\-]{20,}[\"']?$"),
}
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    is_text = path.suffix in TEXT_SUFFIXES or path.name == ".env"
    if not is_text:
        continue
    content = path.read_text(encoding="utf-8", errors="replace")
    for label, pattern in secret_patterns.items():
        if label == "Generic .env assignment" and path.name != ".env":
            continue  # 通用赋值只查 .env
        if pattern.search(content):
            fail(f"possible {label} in {path.relative_to(ROOT)}")

# 5) 占位符
for placeholder in ("<owner>", "<repo>"):
    if placeholder in readme:
        fail(f"unresolved README placeholder: {placeholder}")

# 6) 中文 Windows 用户名路径检测（含 ASCII/CJK）
chinese_user_path = re.compile(r"C:\\Users\\[^\\\"]+")
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        # 权限/占用导致的读失败：跳过该文件，不影响其余扫描
        continue
    m = chinese_user_path.search(content)
    if m:
        ctx = content[max(0, m.start()-30):m.end()+30]
        if not any(ph in ctx for ph in ("用户名", "YourName", "<username>")):
            fail(f"absolute Windows user path in {path.relative_to(ROOT)}: {m.group(0)}")

print(f"OK: repository checks passed for v{version}")
