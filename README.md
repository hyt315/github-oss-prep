# 📦 GitHub 开源准备 / GitHub OSS Prep

<div align="center">

**轻量化 AI Agent 开源准备技能：用确定性脚本守住安全与隐私底线，按「必要项 + 锦上添花」整理 README 与仓库门面，按授权安全推送发版。**

**Lightweight AI Agent Skill for GitHub open-source prep: deterministic secret & hygiene audit, must-have vs optional polish, and approval-gated publishing.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/hyt315/github-oss-prep?sort=semver)](CHANGELOG.md)
[![Validate skill](https://github.com/hyt315/github-oss-prep/actions/workflows/validate.yml/badge.svg)](https://github.com/hyt315/github-oss-prep/actions)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1f6feb)](SKILL.md)

[English](./README.en.md) | [中文](./README.md)

</div>

## 这是什么？

开源一个项目时，现代 AI 已经很擅长写 README 和补配置文件，真正容易翻车的是**把本机路径、个人邮箱、API Key 或 `.git` 历史里的旧凭据带上网**，以及为了套重型模板塞进一堆项目根本用不上的治理文件。

`github-oss-prep` 将开源准备拆成两层：
- **确定性脚本守底线**：零第三方依赖的 `scripts/validate_repo.py` 扫描当前文件、`.git/config`、提交历史、提交邮箱、危险 CI 配置与基础文件缺失。
- **轻量化指令做整理**：不套僵硬模板，只明确「必要项（可跑通的 README、LICENSE、`.gitignore`、Description/Topics）」与「锦上添花项（社区治理文件、加固 CI、双语文档、多生态分发与推广）」，改文件前与发布前两道确认闸把关。

## 快速开始

### 方式 A：把这句话发给你的 AI 助手（最省事）

> 请帮我安装 `github-oss-prep` 技能：将 `https://github.com/hyt315/github-oss-prep` 安装到你的 skills 目录，并确认安装成功。

安装后直接对 AI 说「帮我把这个项目整理准备开源」或「检查一下有没有泄露，准备发到 GitHub」即可触发。

### 方式 B：使用 `npx skills` 一键安装（支持 90+ Agent）

```bash
# 安装到当前项目
npx skills add hyt315/github-oss-prep

# 全局安装（推荐）
npx skills add hyt315/github-oss-prep -g
```

### 方式 C：手动克隆

```bash
# Claude Code
git clone https://github.com/hyt315/github-oss-prep.git ~/.claude/skills/github-oss-prep

# Cursor
git clone https://github.com/hyt315/github-oss-prep.git ~/.cursor/skills/github-oss-prep

# Codex / 通用 Agents 目录
git clone https://github.com/hyt315/github-oss-prep.git ~/.agents/skills/github-oss-prep
```

### 本地直接运行审计脚本

```bash
# 扫描任意目标仓库（当前文件 + Git 提交历史 + CI 安全 + 基础文件检查）
python3 scripts/validate_repo.py /path/to/your-repo --strict --history

# 运行本仓库回归测试
python3 -m unittest discover -s tests -v
```

示例输出：

```text
OK: checks passed for your-repo — P0=0 P1=0 P2=0
```

## 工作流一览

1. **扫描与定边界**：运行 `validate_repo.py --strict --history`，人工复核脚本盲区，确定项目形态与本次范围 → **【闸 1：改文件前确认】**
2. **必要项整理（默认必做）**：清掉 P0/P1 风险，写清首屏价值、真实效果与最短安装/运行命令（Skill 项目默认配「一句话发给 AI + `npx skills add`」），补齐 `LICENSE`、`.gitignore` 与 Description/Topics，并在干净目录实测跑通。
3. **锦上添花（按需选用）**：仅在项目需要时补充 `SECURITY.md`、`CONTRIBUTING.md`、YAML Issue Forms、SHA 锁定 CI、Dependabot、双语 README 或多生态分发。
4. **授权发布与回读**：→ **【闸 2：对外发布前确认】** 只读探测环境（连接器 / `gh` / `GITHUB_TOKEN` / 离线 ZIP），推送后设置并回读 Description、Topics 与 Release。

## 文件结构

```text
github-oss-prep/
├── SKILL.md                             # 主入口指令（4 步流程 + 2 道确认闸）
├── scripts/
│   ├── secret-rules.json                # 隐私与凭据扫描规则唯一真相源
│   └── validate_repo.py                 # 零依赖仓库审计脚本（可扫描任意目标目录）
├── references/
│   ├── readme-and-archetypes.md         # README 必要/可选原则、6 大形态与现代安装范式
│   ├── security-and-pitfalls.md         # 扫描盲区、Git 历史洗库、CI 供应链与许可避坑
│   ├── community-and-ci.md              # 按需社区文件、YAML Issue Forms 与加固 CI
│   └── publishing-and-release.md        # 环境探测、一次性凭据推送、Release 与可选推广
├── tests/
│   ├── test_skill.py                    # 统一 stdlib unittest 回归测试
│   └── fixtures/                        # 泄露样例（必检）与干净样例（不误报）
└── .github/workflows/validate.yml       # CI 自动化校验
```

## 已知限制

- **扫描器基于规则匹配**：覆盖主流云/AI 凭据、本机路径、代理指纹、个人邮箱/手机号、`.git/config` 与流式历史扫描，不做高熵检测；高敏仓库建议额外跑 `gitleaks` 或 `trufflehog`。
- **脚本不替你跑业务测试**：干净目录安装与最小示例验证由执行技能的 Agent 或项目 CI 完成。
- **许可建议非法律意见**：复杂商业或上游模型许可链请以法务与上游条款为准。

## 开源协议

本项目采用 [MIT 许可证](LICENSE) 开源，版本演进见 [CHANGELOG.md](CHANGELOG.md)。
