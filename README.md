# 📦 GitHub 开源准备 / github-oss-prep

<div align="center">

**将任意项目美化为适合 GitHub 发布的专业级开源版本，补齐全套社区健康文件与 CI 自动化，构建专属针对性门面与全生态分发。**

**Turn any project into a polished, GitHub-ready open-source repository with full community health files, CI automation, and tailored multi-channel distribution.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/hyt315/github-oss-prep?sort=semver)](CHANGELOG.md)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1f6feb)](SKILL.md)
[![GitHub Stars](https://img.shields.io/github/stars/hyt315/github-oss-prep?style=social)](https://github.com/hyt315/github-oss-prep/stargazers)

[English](./README.en.md) | [中文](./README.md)

**30 秒上手**：`gh skill install hyt315/github-oss-prep github-oss-prep --agent claude-code --scope user`

**最小示例**：对你的项目说一句「用 github-oss-prep 扫描这个项目，只输出定位卡和缺失清单」

</div>

```text
$ 用 github-oss-prep 扫描当前项目

[Step 0] 定位  →  定位卡：目标用户 / 核心承诺 / 最小示例 / 本次边界
[Step 1] 扫描  →  项目品类 + 缺失清单（对照 Community 七件套）
[Step 2] 整理  →  补齐社区健康文件（经你确认后写入）
[Step 3] 验证  →  五重隐私扫描 + 干净环境复现
[Step 4] 门面  →  README / Description / Topics / 社交预览
[Step 5] 发布  →  分支 / PR（默认）或直推（需授权）
[Step 6] 分发  →  Release + 多平台发版 + 版本一致性
[Step 7] 增长  →  Launch Kit + 定向渠道 + 反馈闭环
```

---

## 📖 这是什么？

把代码、智能体或知识库项目推送到 GitHub 开源时，作者往往被同一批琐事绊住：缺少合规的 `LICENSE`、`CODE_OF_CONDUCT.md`、`SECURITY.md` 与现代 YAML 格式的 Issue 表单，GitHub Insights → Community 健康度始终到不了 100%；README 千篇一律，讲不清 AI 技能、MCP Server、大模型/GGUF、系统 CLI、浏览器扩展或全栈应用的独特价值；也拿不到 `uvx`、`bunx`、`pnpm dlx`、Hugging Face、Chrome Web Store 等真实可用的发版指令。

更隐蔽的风险是泄露：本地绝对路径、私有 Agent 会话标记、API 密钥与 Git 凭据，常常在不知不觉中被一并推进公共仓库。

**`github-oss-prep`** 是一个专为 AI Agent（与开源作者）打造的专业级 GitHub 开源准备技能。它遵循 **渐进式披露原则**，内置 **十大品类专属 README 模板库**、**全生态发版实操指南**、**五重深度隐私安全审计网** 与 **GitHub 2026 社区与 CI 自动化文件库**，覆盖定位、扫描、整理、验证、门面、发布、分发与增长的完整闭环；且每一步的授权边界相互独立——本地整理、远程推送、发布 Release、对外推广分别确认，绝不越权连带执行。

## ✨ 核心特性

| 核心特性 | 功能说明 | 带来价值 |
|---|---|---|
| **十大全景品类 README 引擎** | 覆盖 AI Skill、MCP Server、AI 模型/GGUF、CLI 工具、多媒体、SDK、浏览器扩展、IaC 配置、Web 应用、Awesome 清单 | 告别泛化概念，直接复制填空，精准呈现各类项目核心卖点 |
| **渐进式披露执行铁律** | 依据品类判定结果定向调阅专属规范，严格隔离无关品类 | 杜绝上下文膨胀与跨品类交叉污染，生成质量 100% 聚焦 |
| **五重深度隐私安全网** | 拦截 API Key、私有路径指纹、内部会话 ID、Git Remote Token、构建缓存，附带**真伪泄露案例比对表** | 100% 杜绝敏感凭据与个人开发环境泄露 |
| **2026 社区与 CI 自动化库** | 交互式 YAML Issue Forms、PR 模板、`SECURITY.md`、**Node/Python 矩阵 CI** 与 **Dependabot** | 轻松获得 GitHub Community Profile 100% 满分并实现依赖自动安全更新 |
| **全生态分发与发版实操** | **uv/PyPI、npm、Hugging Face、Chrome Web Store、Docker、Homebrew、Crates.io** 具体发版指南与 Release Checksums | 提供从本地代码到全球各大分发中心的全流程发版指令 |
| **轻量规范化工程架构** | 主干精简，单层 Reference Map 直达，配齐自动化回归自测 | 严守工程纪律，`skill-doctor` 37 项审查 100% PASS |

---

## 🚀 快速开始

### 方式 A：把一句话发给任意 Agent（最推荐、最通用）

> 请安装 github-oss-prep 技能：克隆 `https://github.com/hyt315/github-oss-prep` 到你的 skills 目录（如 `~/.claude/skills/github-oss-prep` 或 `~/.agents/skills/github-oss-prep`），并确认安装成功。

### 方式 B：GitHub CLI 2.90+（一行命令）

```bash
gh skill install hyt315/github-oss-prep github-oss-prep --agent claude-code --scope user
```

### 方式 C：多平台手动安装

| 平台 | 安装命令 |
|---|---|
| **Claude Code** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.claude/skills/github-oss-prep` |
| **Codex** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.codex/skills/github-oss-prep` |
| **Cursor** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.cursor/skills/github-oss-prep` |
| **通用 Agents** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.agents/skills/github-oss-prep` |

### 使用示例（最小可运行）

安装完成后，在你的项目目录里说一句：

> 用 github-oss-prep 扫描这个项目，只输出定位卡和缺失清单，不要改任何文件。

预期产出：

| 产出 | 内容 |
|---|---|
| **定位卡** | 目标用户、核心承诺、最小示例、本次边界 |
| **缺失清单** | 对照 Insights → Community 七件套，逐项列出缺什么、哪项薄弱 |
| **事实卡** | L1 隐私 / L2 社区 / L3 供应链，三层逐项判定 |

---

## 🔒 安全与隐私原则

- **纯只读 / 先审后改**：本地整理默认只读扫描并输出差异报告，修改任何已有文件前先展示理由与 diff；不扫描用户主目录、编辑器配置或 MCP 配置去寻找 Token。
- **零 Token 本地运行**：扫描、隐私审计、社区文件生成、README 撰写与源码打包全部本地完成，无需任何凭据，也不产生额外 API 消耗。

## 📥 下载与获取

| 方式 | 命令 / 链接 |
|---|---|
| **HTTPS** | `git clone https://github.com/hyt315/github-oss-prep.git` |
| **SSH** | `git clone git@github.com:hyt315/github-oss-prep.git` |
| **ZIP** | [下载 ZIP](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.zip) |
| **单文件 (SKILL.md)** | `curl -O https://raw.githubusercontent.com/hyt315/github-oss-prep/main/SKILL.md` |

## 📄 开源协议

本项目采用 [MIT 许可证](LICENSE) 开源。
