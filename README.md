# 📦 GitHub 开源准备 / GitHub OSS Prep

<div align="center">

**将任意项目美化为适合 GitHub 发布的专业级开源版本，补齐全套社区健康文件，构建专属针对性门面。**

**Turn any project into a polished, GitHub-ready open-source repository with full community health files and tailored facade.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/hyt315/github-oss-prep?sort=semver)](CHANGELOG.md)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1f6feb)](SKILL.md)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Python)-brightgreen)](SKILL.md)
[![GitHub Stars](https://img.shields.io/github/stars/hyt315/github-oss-prep?style=social)](https://github.com/hyt315/github-oss-prep/stargazers)

[English](./README.en.md) | [中文](./README.md)

</div>

---

## 📖 这是什么？

将代码或技能项目推送到 GitHub 开源时，开发者往往面临这些繁琐痛点：
- 缺少合规的 `LICENSE`、`CODE_OF_CONDUCT.md`、`SECURITY.md` 或现代 YAML 格式的 Issue 表单，导致 GitHub Insights → Community 健康度无法达到 100%；
- README 结构泛化千篇一律，无法突出 AI 技能、系统 CLI 工具、多媒体视频工程或核心 SDK 的独特核心价值；
- 不慎把本地绝对路径（`<user_home>`）、私有 Agent 会话标记、甚至 API 密钥与 Git 凭据推送到公共仓库造成泄露。

**`github-oss-prep`** 是一个专为 AI Agent（与开源作者）打造的专业级 GitHub 开源准备技能。它内置 **六大项目品类专属 README 模板引擎**、**五重深度环境与隐私安全审计网** 与 **GitHub 2026 社区文件库**，实现一键规范化整理与安全发布。

---

## ✨ 核心特性

| 核心模块 | 覆盖功能 | 带来价值 |
|---|---|---|
| **六大品类 README 引擎** | 针对 AI Skill、CLI 工具、多媒体、SDK、全栈应用、文档定制门面 | 告别千篇一律，精准呈现各类型项目的核心卖点与安装矩阵 |
| **五重深度隐私安全网** | 拦截 API Key、私有路径指纹、内部会话 ID、Git Remote Token、构建缓存 | 100% 杜绝敏感凭据与个人开发环境泄露 |
| **2026 社区健康文件库** | 交互式 YAML Issue Forms (`bug_report.yml`)、PR 模板、`SECURITY.md` | 轻松获得 GitHub Community Profile 100% 满分认证 |
| **全渠道分发矩阵** | `gh skill install`、Agent 一句话自装、Release 预编译资产 (含 SHA-256) | 用户与下游 AI 助手秒级安装，分发体验一流 |
| **轻量规范化架构** | 主干精简，单层 Reference Map 直达，配齐自动化回归自测 | 严守工程纪律，`skill-doctor` 37 项审查 100% PASS |

---

## 🚀 快速开始

这是一个标准的 AI Agent Skill —— 安装到你的 AI 助手后即可直接使用。

### 方式 A：把一句话发给任意 Agent（最推荐、最通用）

把下面这句话直接复制发送给你的 AI 助手，它会自动识别环境并克隆到正确的技能目录：

> 请安装 github-oss-prep 技能：克隆 `https://github.com/hyt315/github-oss-prep` 到你的 skills 目录（如 `~/.claude/skills/github-oss-prep` 或 `~/.agents/skills/github-oss-prep`），并确认安装成功。

> 💡 **小模型同样适配**：安装完成后，只需对 AI 说“帮我把这个项目开源整理一下”或“准备发布到 GitHub”，即可自动触发全流程。

### 方式 B：GitHub CLI 2.90+（一行命令）

```bash
gh skill install hyt315/github-oss-prep github-oss-prep --agent claude-code --scope user
# 也可将 claude-code 替换为 codex / cursor / github-copilot 等
```

### 方式 C：多平台手动安装

| 平台 | 安装命令 |
|---|---|
| **Claude Code** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.claude/skills/github-oss-prep` |
| **Codex** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.codex/skills/github-oss-prep` |
| **Cursor** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.cursor/skills/github-oss-prep` |
| **通用 Agents 目录** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.agents/skills/github-oss-prep` |

### 方式 D：本地运行回归自测

```powershell
python scripts/selftest.py
```

---

## 🔒 安全与隐私原则

- **先审后改（Audit Before Change）**：本地整理默认只读扫描并输出差异报告，绝不擅自强行覆盖用户现有文件。
- **五重严密防御**：对代码、文档、`.git/config` 与历史提交进行全面深度扫描，阻断任何敏感信息。
- **分阶段明确授权**：本地开源整理、远程仓库创建、Release 打包分发与外部推广分别独立确认，绝不越权连带执行。

---

## 📥 下载与获取

| 方式 | 命令 / 链接 |
|---|---|
| **HTTPS** | `git clone https://github.com/hyt315/github-oss-prep.git` |
| **SSH** | `git clone git@github.com:hyt315/github-oss-prep.git` |
| **GitHub CLI** | `gh repo clone hyt315/github-oss-prep` |
| **ZIP 压缩包** | [下载 ZIP](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.zip) |
| **Tar 归档** | [下载 Tar](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.tar.gz) |
| **单文件 (SKILL.md)** | `curl -O https://raw.githubusercontent.com/hyt315/github-oss-prep/main/SKILL.md` |

---

## 📁 文件结构

```
github-oss-prep/
├── SKILL.md                          # 核心技能定义与轻量化工作流
├── README.md                         # 中文说明文档
├── README.en.md                      # 英文说明文档
├── CHANGELOG.md                      # 版本发布记录
├── LICENSE                           # MIT 开源许可证
├── .gitignore                        # Git 忽略规则
├── CONTRIBUTING.md                   # 社区贡献指南
├── CODE_OF_CONDUCT.md                # 行为准则
├── SECURITY.md                       # 安全策略
├── SUPPORT.md                        # 支持渠道
├── manifest.json                     # 技能元数据清单
├── agents/                           # 多 Agent 平台元数据
├── scripts/
│   ├── validate_repo.py              # 仓库结构、规范与隐私安全校验器
│   └── selftest.py                   # 自动化回归自测脚本
├── .github/
│   ├── CODEOWNERS                    # 代码审查者配置
│   ├── pull_request_template.md      # 标准 PR 模板
│   ├── workflows/                    # CI 自动化工作流
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.yml            # 交互式 Bug 反馈表单
│       ├── feature_request.yml       # 交互式功能建议表单
│       └── config.yml                # Issue 模板选择器配置
└── references/                       # 深度参考文档
    ├── readme-template.md            # 六大品类专属 README 模板库
    ├── privacy-scan.md               # 五重深度隐私与环境安全扫描指南
    ├── community-templates.md        # GitHub 2026 社区文件库与模板
    ├── release-and-distribution.md   # 全渠道现代分发与下载矩阵
    ├── description-guide.md          # Description 与 Topics 标签优化指南
    ├── discovery-and-promotion.md    # 开源发现、Launch Kit 与推广策略
    ├── mcp-push-guide.md             # GitHub 推送与授权指引
    ├── pr-and-release-workflow.md    # PR、CI 与发布门禁
    ├── github-pat-setup.md           # GitHub PAT 配置指南
    └── github-pat-comparison.md      # GitHub PAT 权限类型对比
```

---

## ❓ 常见问题 (FAQ)

- **Q: 整理和打包需要 GitHub Token 吗？**  
  A: 不需要。项目扫描、隐私检查、规范补齐、README 生成与源码 ZIP 打包均在本地完成，只有最终向 GitHub 推送时才需要授权。
- **Q: 它会擅自修改我的现有代码吗？**  
  A: 绝对不会。本技能坚持先审后改原则，仅在用户明确批准后才创建或修改文件。
- **Q: 我的项目不是 AI 技能，也能使用吗？**  
  A: 完全可以。内置六大品类模板引擎，对 CLI 工具、多媒体工程、核心 SDK、Web 应用与文档项目均有针对性支持。

---

## 🤝 参与贡献

欢迎提交 Issue 与 Pull Request！详见 [CONTRIBUTING.md](CONTRIBUTING.md)。如果这个技能对你有帮助，欢迎在 GitHub 上点个 [Star ⭐](https://github.com/hyt315/github-oss-prep/stargazers)！

---

## 📄 开源协议

本项目采用 [MIT 许可证](LICENSE) 开源。

详见 [CHANGELOG.md](CHANGELOG.md) 了解版本演进历史。

---

> 🌏 **English: [README.en.md](./README.en.md)**
