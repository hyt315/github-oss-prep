# 🚀 GitHub 开源准备 / GitHub OSS Prep

<div align="center">

**一键将任意项目美化为专业级 GitHub 开源仓库，自动补全全套社区健康文件**

**One-click polish any project into a professional GitHub open-source repo with full community health files**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.2.1-green.svg)]()
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
| 📝 **补齐文件** | 一键生成 LICENSE、README、.gitignore、CONTRIBUTING、Issue/PR 模板等全套社区健康文件 |
| 🛡️ **隐私保护** | 自动扫描 API Key、邮箱、私网 IP、真实路径等敏感信息，推送前二次验证 |
| 📤 **一键推送** | 支持 MCP 工具和 curl+git 两种方式推送到 GitHub，自动发现 Token |
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

安装后直接告诉 AI 助手你的意图，Skill 会自动执行 **扫描 → 补齐 → 审查 → Description → 推送 → Release → 优化** 这 7 步工作流。全程不覆盖已有文件，每步确认后再继续。

---

## 📥 安装 / Installation

### 一行命令安装

| 平台 | 安装命令 |
|------|----------|
| **Claude Code** | `git clone https://github.com/<owner>/<repo>.git ~/.claude/skills/github-oss-prep` |
| **Codex** | `git clone https://github.com/<owner>/<repo>.git ~/.codex/skills/github-oss-prep` |
| **Cursor** | `git clone https://github.com/<owner>/<repo>.git ~/.cursor/skills/github-oss-prep` |

> 安装后 Skill 会自动生效，无需额外配置。

---

## 📥 下载 / Download

### 源码下载

| 方式 | 命令 / 链接 |
|------|------------|
| **HTTPS** | `git clone https://github.com/<owner>/<repo>.git` |
| **SSH** | `git clone git@github.com:<owner>/<repo>.git` |
| **GitHub CLI** | `gh repo clone <owner>/<repo>` |
| **ZIP 源码** | [下载 ZIP](https://github.com/<owner>/<repo>/archive/refs/heads/main.zip) |
| **Tar 源码** | [下载 Tar](https://github.com/<owner>/<repo>/archive/refs/heads/main.tar.gz) |

---

## 💡 核心理念

- **只补缺，不覆盖**：已有文件不修改，只补充缺失项
- **按类型适配**：Skill 项目、代码项目、文档项目各有侧重
- **对齐标准**：目标是通过 GitHub Community Profile 100% 考核
- **确认后推送**：生成内容先展示，用户确认后才创建仓库

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
5. **推送**：确认仓库名和 Topics → 自动推送
6. **完成**：项目已在 GitHub 上线，Community Profile 100% 达标

---

## 🤝 贡献

请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 📄 许可

[MIT](LICENSE)

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
| 📤 **One-Click Push** | Pushes to GitHub via MCP tools or curl+git fallback with automatic token discovery |
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

Once installed, simply tell your AI assistant what you want. The Skill runs a 7-step workflow: **Scan → Fill → Review → Description → Push → Release → Optimize**. It never overwrites existing files, and confirms with you at each step.

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
└── references/                       # Reference documents (8 files)
```

---

## 📚 Examples

Here's a real workflow: a local Markdown document project wants to go open-source:

1. **Install**: Clone this repo into your AI assistant's skills directory
2. **Scan**: Detected as docs project → Missing LICENSE, README, .gitignore
3. **Fill**: Generated files tailored to the project
4. **Review**: Privacy scan clean, content confirmed
5. **Push**: Repo name and topics confirmed → Auto-push
6. **Done**: Project live on GitHub, Community Profile 100%

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📄 License

[MIT](LICENSE)
