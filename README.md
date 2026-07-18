# 🚀 GitHub 开源准备 / GitHub OSS Prep

<div align="center">

**一键将任意项目美化为专业级 GitHub 开源仓库，自动补全全套社区健康文件**

**One-click polish any project into a professional GitHub open-source repo with full community health files**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.4.0-green.svg)](https://github.com/hyt315/github-oss-prep/releases/tag/v1.4.0)
[![SKILL.md](https://img.shields.io/badge/Agent%20Skill-SKILL.md-green)](SKILL.md)

[English](#english) | [中文](#中文)

</div>

---

## 中文

## 📖 这是什么？

**GitHub 开源准备** 是一个 AI Agent Skill，专为即将开源的项目设计。它会自动扫描项目结构、识别类型、补齐缺失的社区健康文件（LICENSE、README、Issue 模板等），并通过隐私扫描确保无敏感信息泄露，最后支持一键推送到 GitHub。

### ✨ 核心特性

| 特性 | 说明 |
|------|------|
| 🔍 **智能扫描** | 自动识别项目类型（Skill/代码/文档），逐项检查 GitHub Community Profile 考核项 |
| 📝 **审计与改进** | 补齐缺失文件，也会识别过时、残缺或不可运行的已有文档，经确认后改进 |
| 🛡️ **隐私保护** | 自动扫描 API Key、邮箱、私网 IP、真实路径等敏感信息，推送前二次验证 |
| ✅ **采用性验证** | 用干净 clone 验证安装、最小示例、测试、构建、来源许可与版本一致性 |
| 📤 **灵活交付** | 无认证也能完成整理并导出 ZIP；发布时支持官方 GitHub 连接器或 `gh` CLI |
| 🔀 **安全发布** | 公开项目默认走分支、Draft PR、CI 与人工合并；单人低风险改动可选择直推 |
| 📣 **发现与推广** | 生成 Topics、社交预览、演示素材、Launch Kit、渠道计划和反馈闭环 |
| 🌐 **中英双语** | 所有生成文件支持中英双语，符合 GitHub 全球社区最佳实践 |
| 📦 **多平台分发** | 代码项目支持 npm、PyPI、crates.io、Docker Hub、Homebrew 等多渠道发布 |

---

## 🚀 快速开始

这是一个 AI Agent Skill，安装到任意 AI 编程助手后即可使用。

### 它能做什么？

一句话：**把任意本地项目变成专业的 GitHub 开源仓库。** 自动补全 LICENSE、README、Issue/PR 模板等全套社区健康文件，隐私扫描确保无敏感信息泄露，最后推送到 GitHub。

### 典型使用场景

- 你写了个工具/脚本，想开源但不知道怎么"包装" — 它帮你补齐所有标准文件
- 你的项目 README 太简陋 — 它生成中英双语专业版
- 你不确定有没有忘记删 API Key — 它自动扫描并提醒
- 你不想手动创建 Issue 模板、PR 模板 — 它一键生成

### 怎么用

安装后直接告诉 AI 助手你的意图，Skill 会自动执行 **定位 → 扫描 → 整理 → 验证 → 仓库门面 → PR/发布 → Release → 发现与增长**。整理和 ZIP 交付不需要 GitHub 认证；远程发布、Release 和外部推广分别确认。

---

## 📥 安装 / Installation

### 一行命令安装

| 平台 | 安装命令 |
|------|----------|
| **Claude Code** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.claude/skills/github-oss-prep` |
| **Codex** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.codex/skills/github-oss-prep` |
| **Cursor** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.cursor/skills/github-oss-prep` |

> 安装后即可完成扫描、整理、隐私检查和 ZIP 交付，无需 GitHub Token。只有最终发布需要 GitHub 授权。

### GitHub 发布认证

推荐顺序：

1. 使用 AI 平台提供的官方 GitHub 连接器；
2. 或在受信任终端运行 `gh auth login --web`；
3. 两者均不可用时，Skill 仍会输出完整源码目录、ZIP、Description 和 Topics，供网页手动上传。

不要把 PAT 写进公开仓库、聊天记录或 Git remote URL。需要 MCP 时，请使用 GitHub 当前维护的 [`github/github-mcp-server`](https://github.com/github/github-mcp-server)；旧的 `@modelcontextprotocol/server-github` npm 包已停止维护。

---

## 📥 下载 / Download

### 源码下载

| 方式 | 命令 / 链接 |
|------|------------|
| **HTTPS** | `git clone https://github.com/hyt315/github-oss-prep.git` |
| **SSH** | `git clone git@github.com:hyt315/github-oss-prep.git` |
| **GitHub CLI** | `gh repo clone hyt315/github-oss-prep` |
| **ZIP 源码** | [下载 ZIP](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.zip) |
| **Tar 源码** | [下载 Tar](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.tar.gz) |

---

## 💡 核心理念

- **先审后改**：保留有效内容；已有文件存在质量或安全问题时，展示差异后再修改
- **按类型适配**：Skill 项目、代码项目、文档项目各有侧重
- **可运行优先**：Community Profile 只是底线，干净环境可安装、可运行、可贡献才算完成
- **PR 默认**：公开维护项目走分支、Draft PR、CI 和人工复核
- **分步授权**：推送、Release、包发布和对外推广互不默认包含

---

## 📁 文件结构

```
github-oss-prep/
├── SKILL.md                          # Skill 核心定义
├── README.md                         # 本文件
├── LICENSE                           # MIT 协议
├── .gitignore                        # Git 忽略规则
├── CONTRIBUTING.md                   # 贡献指南
├── CODE_OF_CONDUCT.md                # 行为准则
├── SECURITY.md                       # 安全策略
├── .github/
│   ├── pull_request_template.md      # PR 模板
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.yml            # Bug 报告表单
│       ├── feature_request.yml       # 功能建议表单
│       └── doc_improvement.yml       # 文档改进表单
└── references/                       # 参考文件
    ├── readme-template.md            # README 模板
    ├── description-guide.md          # Description 编写指南
    ├── privacy-scan.md               # 隐私扫描规则
    ├── mcp-push-guide.md             # 推送方案指南
    ├── templates-and-formats.md      # 模板与格式合集
    ├── release-and-distribution.md   # Release 与分发指南
    ├── pr-and-release-workflow.md    # PR、CI、验证和发布门禁
    ├── discovery-and-promotion.md    # 可发现性、Launch Kit 与推广闭环
    ├── github-pat-setup.md           # PAT 配置教程
    └── github-pat-comparison.md      # PAT 类型对比
```

---

## 📚 端到端示例

假设有一个本地 Markdown 文档项目，想开源到 GitHub：

1. **安装**：克隆本仓库到 AI 助手的 skills 目录
2. **扫描**：识别为文档项目 → 发现缺少 LICENSE、README、.gitignore
3. **补齐**：生成对应文件，内容适配文档项目特性
4. **审查**：隐私扫描通过，文件内容确认无误
5. **交付**：确认仓库名和 Topics → 连接器/`gh` 发布，或输出 ZIP 手动上传
6. **完成**：本地开源包一定可交付；授权可用时同步发布到 GitHub

---

## 🤝 贡献

请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 📄 许可

[MIT](LICENSE)

版本变化见 [CHANGELOG.md](CHANGELOG.md)。

---

## English

## 📖 What is this?

**GitHub OSS Prep** is an AI Agent Skill that transforms any local project into a professional GitHub open-source repository. It auto-detects project type, fills in missing community health files, scans for sensitive data, and pushes to GitHub — all in one workflow.

### ✨ Core Features

| Feature | Description |
|---------|-------------|
| 🔍 **Smart Scanning** | Identifies project type (Skill / Code / Docs) and checks against GitHub Community Profile standards |
| 📝 **Auto-Fill Files** | Generates LICENSE, README, .gitignore, CONTRIBUTING, Issue/PR templates, and more |
| 🛡️ **Privacy Protection** | Scans for API keys, emails, private IPs, real paths — with pre-push verification |
| 📤 **Flexible Delivery** | Always produces a local ZIP; publishes through an official GitHub connector or authenticated `gh` CLI when available |
| 🌐 **Bilingual Support** | All generated files support Chinese/English bilingual output |
| 📦 **Multi-Platform** | Code projects support npm, PyPI, crates.io, Docker Hub, Homebrew distribution |

---

## 🚀 Quick Start

This is an AI Agent Skill — install it in any AI coding assistant and it's ready to use.

### What it does

In one sentence: **turn any local project into a professional GitHub open-source repo.** It auto-generates LICENSE, README, Issue/PR templates and other community health files, runs privacy scans to catch sensitive data, and pushes everything to GitHub.

### Common use cases

- You built a tool/script and want to open-source it but don't know how to "package" it — it fills in all the standard files
- Your project's README is too bare — it generates a bilingual professional version
- You're not sure if you forgot to remove an API key — it scans and alerts you
- You don't want to manually create Issue templates and PR templates — it generates them in one shot

### How to use

Once installed, tell your AI assistant what you want. The Skill runs an adoption-focused workflow: **Position → Scan → Improve → Validate → Repository Surface → PR/Publish → Release → Discover**. Preparation and ZIP delivery never require GitHub authentication. Public projects default to a reviewable branch and Draft PR; remote publication, releases and external promotion require separate approval.

---

## 📁 File Structure

```
github-oss-prep/
├── SKILL.md                          # Core skill definition
├── README.md                         # This file
├── LICENSE                           # MIT License
├── .gitignore                        # Git ignore rules
├── CONTRIBUTING.md                   # Contribution guide
├── CODE_OF_CONDUCT.md                # Code of conduct
├── SECURITY.md                       # Security policy
├── .github/
│   ├── pull_request_template.md      # PR template
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.yml            # Bug report form
│       ├── feature_request.yml       # Feature request form
│       └── doc_improvement.yml       # Docs improvement form
└── references/                       # Reference documents
```

---

## 📚 Examples

Here's a real workflow: a local Markdown document project wants to go open-source:

1. **Install**: Clone this repo into your AI assistant's skills directory
2. **Scan**: Detected as docs project → Missing LICENSE, README, .gitignore
3. **Fill**: Generated files tailored to the project
4. **Review**: Privacy scan clean, content confirmed
5. **Deliver**: Confirm repo name and Topics → connector/`gh` publish, or manual ZIP handoff
6. **Done**: Open-source package is always delivered; GitHub publication follows when authentication is available

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📄 License

[MIT](LICENSE)

See [CHANGELOG.md](CHANGELOG.md) for version history.
