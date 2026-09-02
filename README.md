# 📦 GitHub 开源准备 / GitHub OSS Prep

<div align="center">

**将任意项目美化为适合 GitHub 发布的专业级开源版本，补齐全套社区健康文件与 CI 自动化，构建专属针对性门面与全生态分发。**

**Turn any project into a polished, GitHub-ready open-source repository with full community health files, CI automation, and tailored multi-channel distribution.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/hyt315/github-oss-prep?sort=semver)](CHANGELOG.md)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1f6feb)](SKILL.md)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Python)-brightgreen)](SKILL.md)
[![GitHub Stars](https://img.shields.io/github/stars/hyt315/github-oss-prep?style=social)](https://github.com/hyt315/github-oss-prep/stargazers)

[English](./README.en.md) | [中文](./README.md)

</div>

---

## 📖 这是什么？

将代码、智能体或知识库项目推送到 GitHub 开源时，开发者往往面临这些繁琐痛点：
- 缺少合规的 `LICENSE`、`CODE_OF_CONDUCT.md`、`SECURITY.md` 或现代 YAML 格式的 Issue 表单，导致 GitHub Insights → Community 健康度无法达到 100%；
- README 结构泛化千篇一律，无法突出 AI 技能、MCP Server、大模型/GGUF、系统 CLI、浏览器扩展或全栈 Web 应用的独特核心价值；
- 缺少 `uvx`、`bunx`、`pnpm dlx`、Hugging Face、Chrome Web Store 的具体发版指令与 CI 矩阵测试；
- 不慎把本地绝对路径（`<user_home>`）、私有 Agent 会话标记、甚至 API 密钥与 Git 凭据推送到公共仓库造成泄露。

**`github-oss-prep`** 是一个专为 AI Agent（与开源作者）打造的专业级 GitHub 开源准备技能。它确立了 **渐进式披露原则（Progressive Disclosure）**，内置 **十大全景项目品类专属 README 完整模板库**、**全生态发版实操指南**、**五重深度环境与隐私安全审计网** 与 **GitHub 2026 社区与 CI 自动化文件库**，实现一键规范化整理与安全发布。

---

## ✨ 核心特性

| 核心模块 | 覆盖功能 | 带来价值 |
|---|---|---|
| **十大全景品类 README 引擎** | 覆盖 AI Skill、MCP Server、AI 模型/GGUF、CLI 工具、多媒体、SDK、浏览器扩展、IaC 配置、Web 应用、Awesome 清单 | 告别泛化概念，直接复制填空，精准呈现各类项目核心卖点 |
| **渐进式披露执行铁律** | 依据品类判定结果定向调阅专属规范，严格隔离无关品类 | 杜绝上下文膨胀与跨品类交叉污染，生成质量 100% 聚焦 |
| **五重深度隐私安全网** | 拦截 API Key、私有路径指纹、内部会话 ID、Git Remote Token、构建缓存，附带**真伪泄露案例比对表** | 100% 杜绝敏感凭据与个人开发环境泄露 |
| **2026 社区与 CI 自动化库** | 交互式 YAML Issue Forms、PR 模板、`SECURITY.md`、**Node/Python 矩阵 CI** 与 **Dependabot** | 轻松获得 GitHub Community Profile 100% 满分并实现依赖自动安全更新 |
| **全生态分发与发版实操** | **uv/PyPI、npm、Hugging Face、Chrome Web Store、Docker、Homebrew、Crates.io** 具体发版指南与 Release Checksums | 提供从本地代码到全球各大分发中心的全流程发版指令 |
| **轻量规范化工程架构** | 主干精简，单层 Reference Map 直达，配齐自动化回归自测 | 严守工程纪律，`skill-doctor` 37 项审查 100% PASS |

---

## 📊 开源准备全流程架构

```
[输入: 本地任意待开源项目 / 目录]
                 │
      [Step 0: 十大全景品类识别与定位]
      精准判定: AI Skill / MCP Server / 模型权重 / CLI 工具 / 浏览器扩展 / IaC / ...
                 │
      [Step 1: 五重深度安全扫描]
      拦截 API 密钥 / 私有路径指纹 / 内部会话 ID / Git URL 污染 / 垃圾缓存
                 │
      [Step 2: 2026 社区与 CI 补齐]
      生成交互式 YAML Issue Forms / PR 模板 / SECURITY.md / CI / Dependabot
                 │
      [Step 3: 渐进式专属 README 门面渲染]
      遵循渐进式披露，定向调阅专属品类完整骨架 (含动态 Shields 徽章)
                 │
      [Step 4: 全生态分发与包管理配置]
      配置 uvx / bunx / HuggingFace / ChromeStore / gh skill / Checksums
                 │
      [Step 5: 干净环境回归自测]
      运行 scripts/selftest.py，确保 100% 满分通过质量门禁
                 │
      [Step 6: 分阶段授权发布]
      经用户明确确认后推送 GitHub、打 Tag 并发布 GitHub Release
```

---

## 🚀 快速开始

这是一个标准的 AI Agent Skill —— 安装到你的 AI 助手后即可直接使用。

### 方式 A：把一句话发给任意 Agent（最推荐、最通用）

把下面这句话直接复制发送给你的 AI 助手，它会自动识别环境并克隆到正确的技能目录：

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
| **通用 Agents 目录** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.agents/skills/github-oss-prep` |

### 方式 D：本地运行回归自测

```powershell
python scripts/selftest.py
```

---

## 🔒 安全与隐私原则

- **先审后改（Audit Before Change）**：本地整理默认只读扫描并输出差异报告，绝不擅自强行覆盖用户现有文件。
- **渐进式隔离（Progressive Isolation）**：处理特定项目时仅读取专属模板，杜绝上下文冗余与环境参数污染。
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

## 📖 深度参考文档导读

| 参考文档 | 核心内容 | 推荐阅读时机 | 预估耗时 |
|---|---|---|---|
| 📑 [**十大品类完整 README 模板库 (`readme-template.md`)**](references/readme-template.md) | 10 大软件形态完整开箱即用 Markdown 骨架与现代终端运行器表 | 为项目生成或重构 README 时 | 4 分钟 |
| 🛡️ [**五重隐私与安全扫描 (`privacy-scan.md`)**](references/privacy-scan.md) | 5 重扫描防御网、真伪泄露实战比对表与脱敏规则 | 执行本地安全自检与脱敏排查时 | 3 分钟 |
| 🏛️ [**社区健康文件与 CI 模板 (`community-templates.md`)**](references/community-templates.md) | 现代交互式 YAML Issue Forms、Node/Python 矩阵 CI 工作流与 Dependabot | 补齐 GitHub 社区文件与持续集成时 | 3 分钟 |
| 🚀 [**全渠道分发与发版指南 (`release-and-distribution.md`)**](references/release-and-distribution.md) | uv、npm、HuggingFace、ChromeStore、Docker 发版实操、国内镜像源与 Checksums | 发布到全球平台或 GitHub Release 时 | 4 分钟 |
| 🏷️ [**Description 与 Topics 指南 (`description-guide.md`)**](references/description-guide.md) | 精准 120 字仓库简介与高权重标签生成指南 | 设置 GitHub 仓库门面信息时 | 3 分钟 |
| 🌐 [**开源发现与推广策略 (`discovery-and-promotion.md`)**](references/discovery-and-promotion.md) | Launch Kit 营销包、社交预览与全网发布渠道 | 准备发布与对外推广项目时 | 3 分钟 |
| 🔐 [**GitHub 推送与 MCP 指引 (`mcp-push-guide.md`)**](references/mcp-push-guide.md) | 官方 MCP 与标准 CLI 推送流程 | 执行远程推送与仓库创建时 | 2 分钟 |
| 🚦 [**PR 与发布门禁工作流 (`pr-and-release-workflow.md`)**](references/pr-and-release-workflow.md) | 分支、PR、CI 测试与发布自动化校验 | 建立持续集成与发版流水线时 | 3 分钟 |

---

## 📄 开源协议

本项目采用 [MIT 许可证](LICENSE) 开源。

详见 [CHANGELOG.md](CHANGELOG.md) 了解版本演进历史。

---

> 🌏 **English: [README.en.md](./README.en.md)**
