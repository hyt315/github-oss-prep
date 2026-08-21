#!/usr/bin/env python3
"""github-oss-prep 自测：验证技能结构与 scripts/validate_repo.py 均能正常工作。

好夹具（本技能自身）：SKILL.md 存在、frontmatter 合法、references/ 完整、
validate_repo.py 对本仓库返回 0（通过）。
负向用例（临时构造）：缺核心文件 + 含未替换占位符的"坏仓库"，应被拦下。
零依赖，仅 Python 标准库。
"""
from __future__ import annotations

import importlib.util
import tempfile
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = (
    "SKILL.md", "README.md", "LICENSE", "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md", "SECURITY.md",
    "references/description-guide.md", "references/privacy-scan.md",
    "references/readme-template.md", "references/templates-and-formats.md",
    "references/release-and-distribution.md", "references/mcp-push-guide.md",
    "references/pr-and-release-workflow.md", "references/discovery-and-promotion.md",
    "references/github-pat-setup.md", "references/github-pat-comparison.md",
    "scripts/validate_repo.py",
)


def _load_validate() -> object:
    spec = importlib.util.spec_from_file_location("validate_repo", SKILL_ROOT / "scripts" / "validate_repo.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def check_good() -> None:
    for f in REQUIRED_FILES:
        if not (SKILL_ROOT / f).is_file():
            raise AssertionError(f"缺少文件: {f}")
    skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---") or "name:" not in skill.split("---")[1]:
        raise AssertionError("SKILL.md frontmatter 缺失 name/description")


def check_validate_bad(tmp: Path) -> None:
    """负向用例：validate_repo.py 在坏仓库上必须失败。"""
    import shutil
    bad = tmp / "repo"
    (bad / "scripts").mkdir(parents=True)
    # 把 validate_repo.py 复制到坏仓库的 scripts/ 下，使其 ROOT=parents[1] 指向坏仓库
    shutil.copy(SKILL_ROOT / "scripts" / "validate_repo.py", bad / "scripts" / "validate_repo.py")
    (bad / "references").mkdir(parents=True)
    (bad / "SKILL.md").write_text("---\nname: x\ndescription: 测试\n---\n", encoding="utf-8")
    (bad / "README.md").write_text("readme <owner>/<repo>", encoding="utf-8")
    (bad / "CHANGELOG.md").write_text("# Changelog\n\n## [9.9.9]\n", encoding="utf-8")
    (bad / "LICENSE").write_text("MIT", encoding="utf-8")
    (bad / "CONTRIBUTING.md").write_text("contributing", encoding="utf-8")
    (bad / "references" / "pr-and-release-workflow.md").write_text("pr", encoding="utf-8")
    (bad / "references" / "discovery-and-promotion.md").write_text("disc", encoding="utf-8")

    import subprocess
    r = subprocess.run(["python", "scripts/validate_repo.py"], cwd=bad, capture_output=True, text=True)
    if r.returncode == 0:
        raise AssertionError(f"负向夹具应 FAIL（缺文件/占位符未拦），实际 PASS。stdout={r.stdout}")


def main() -> int:
    check_good()
    with tempfile.TemporaryDirectory() as tmp_name:
        check_validate_bad(Path(tmp_name))
    print("SELFTEST PASS (2 checks: structure + validate-repo-negative)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
