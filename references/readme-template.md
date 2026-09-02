# 十大全景开源项目品类专属 README 完整模板库

> 本文档为开源项目提供 **10 大主流品类的完整、开箱即用、可直接复制填空的 README.md 骨架**。
> 严格对标 Anthropic、Hugging Face、Google Chrome、CNCF 与 sindresorhus 官方标准。
> 遵循【渐进式披露原则】：仅调阅与当前项目品类匹配的专属章节，严禁通读或 cross-pollinate 其它无关品类！

---

## 目录导航（渐进式披露索引）

- [动态 Badge 速查矩阵](#动态-badge-速查矩阵)
- [🤖 智能体与 AI 核心生态](#-智能体与-ai-核心生态)
  - [品类 1：AI Agent 技能型 (Skill / Tool) 完整模板](#品类-1ai-agent-技能型-skill--tool-完整模板)
  - [品类 2：MCP Server 协议端 (Model Context Protocol) 完整模板](#品类-2mcp-server-协议端-model-context-protocol-完整模板)
  - [品类 3：AI 模型权重与数据集 (Model & Dataset / GGUF) 完整模板](#品类-3ai-模型权重与数据集-model--dataset--gguf-完整模板)
- [🛠️ 终端与系统开发生态](#️-终端与系统开发生态)
  - [品类 4：系统与 CLI 诊断工具型 (CLI / System Utility) 完整模板](#品类-4系统与-cli-诊断工具型-cli--system-utility-完整模板)
  - [品类 5：类库与核心 SDK 型 (Library / SDK) 完整模板](#品类-5类库与核心-sdk-型-library--sdk-完整模板)
  - [品类 6：基础设施代码与配置集 (IaC / Dotfiles / Helm) 完整模板](#品类-6基础设施代码与配置集-iac--dotfiles--helm-完整模板)
- [🎨 前端与交互应用生态](#-前端与交互应用生态)
  - [品类 7：前端与多媒体生成型 (Frontend / Media Generator) 完整模板](#品类-7前端与多媒体生成型-frontend--media-generator-完整模板)
  - [品类 8：浏览器扩展与插件型 (Browser Extension / MV3) 完整模板](#品类-8浏览器扩展与插件型-browser-extension--mv3-完整模板)
  - [品类 9：完整应用与 Web 服务型 (Fullstack App) 完整模板](#品类-9完整应用与-web-服务型-fullstack-app-完整模板)
- [📚 知识与内容生态](#-知识与内容生态)
  - [品类 10：知识库与 Awesome 精选清单 (Curated / Awesome List) 完整模板](#品类-10知识库与-awesome-精选清单-curated--awesome-list-完整模板)
- [多平台现代终端下载与安装表格集合 (2026 标准)](#多平台现代终端下载与安装表格集合-2026-标准)

---

## 动态 Badge 速查矩阵

```markdown
<!-- License 徽章 -->
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

<!-- 动态 Release 徽章（自动读取最新 Tag） -->
[![Release](https://img.shields.io/github/v/release/{owner}/{repo}?sort=semver)](https://github.com/{owner}/{repo}/releases)

<!-- 包管理器动态版本 (npm / PyPI / Crates) -->
[![npm version](https://img.shields.io/npm/v/{pkg-name}.svg)](https://www.npmjs.com/package/{pkg-name})
[![PyPI version](https://img.shields.io/pypi/v/{pkg-name}.svg)](https://pypi.org/project/{pkg-name}/)
[![Crates.io](https://img.shields.io/crates/v/{pkg-name}.svg)](https://crates.io/crates/{pkg-name})

<!-- CI 状态徽章 -->
[![CI Status](https://github.com/{owner}/{repo}/actions/workflows/ci.yml/badge.svg)](https://github.com/{owner}/{repo}/actions)

<!-- 平台支持与 Stars 徽章 -->
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](SKILL.md)
[![GitHub Stars](https://img.shields.io/github/stars/{owner}/{repo}?style=social)](https://github.com/{owner}/{repo}/stargazers)
```

---

# 🤖 智能体与 AI 核心生态

## 品类 1：AI Agent 技能型 (Skill / Tool) 完整模板

```markdown
# 📦 项目名称 / Project Name

<div align="center">

**一句话中文功能与价值描述**

**One-liner English description of core capabilities and benefits.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/{owner}/{repo}?sort=semver)](CHANGELOG.md)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1f6feb)](SKILL.md)
[![GitHub Stars](https://img.shields.io/github/stars/{owner}/{repo}?style=social)](https://github.com/{owner}/{repo}/stargazers)

[English](#english) | [中文](#chinese)

</div>

---

## 📖 这是什么？

说明该技能解决的具体痛点场景与核心价值（2~3 段）。

## ✨ 核心特性

| 核心特性 | 功能说明 | 带来价值 |
|---|---|---|
| **特性 1** | 功能描述 | 价值收益 |
| **特性 2** | 功能描述 | 价值收益 |

---

## 🚀 快速开始

### 方式 A：把一句话发给任意 Agent（最推荐、最通用）

> 请安装 {repo} 技能：克隆 `https://github.com/{owner}/{repo}` 到你的 skills 目录（如 `~/.claude/skills/{repo}` 或 `~/.agents/skills/{repo}`），并确认安装成功。

### 方式 B：GitHub CLI 2.90+（一行命令）

```bash
gh skill install {owner}/{repo} {name} --agent claude-code --scope user
```

### 方式 C：多平台手动安装

| 平台 | 安装命令 |
|---|---|
| **Claude Code** | `git clone https://github.com/{owner}/{repo}.git ~/.claude/skills/{repo}` |
| **Codex** | `git clone https://github.com/{owner}/{repo}.git ~/.codex/skills/{repo}` |
| **Cursor** | `git clone https://github.com/{owner}/{repo}.git ~/.cursor/skills/{repo}` |
| **通用 Agents** | `git clone https://github.com/{owner}/{repo}.git ~/.agents/skills/{repo}` |

---

## 🔒 安全与隐私原则

- **纯只读 / 先审后改**：说明技能的操作权限边界。
- **零 Token 本地运行**：说明无需额外 API 消耗。

## 📥 下载与获取

| 方式 | 命令 / 链接 |
|---|---|
| **HTTPS** | `git clone https://github.com/{owner}/{repo}.git` |
| **SSH** | `git clone git@github.com:{owner}/{repo}.git` |
| **ZIP** | [下载 ZIP](https://github.com/{owner}/{repo}/archive/refs/heads/main.zip) |
| **单文件** | `curl -O https://raw.githubusercontent.com/{owner}/{repo}/main/SKILL.md` |

## 📄 开源协议

本项目采用 [MIT 许可证](LICENSE) 开源。
```

---

## 品类 2：MCP Server 协议端 (Model Context Protocol) 完整模板

```markdown
# 🔌 项目名称 MCP Server / Project MCP Server

<div align="center">

**专为 AI 助手打造的 Model Context Protocol 协议服务端 · 开箱即用 · 纯净安全**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![npm version](https://img.shields.io/npm/v/{pkg-name}.svg)](https://www.npmjs.com/package/{pkg-name})
[![MCP Standard](https://img.shields.io/badge/MCP-2026%20Compliant-1f6feb)](https://modelcontextprotocol.io)

</div>

---

## 📖 这是什么？

这是一个基于 Model Context Protocol (MCP) 标准构建的服务端程序，用于向 Claude Desktop、Cursor、Cline、VS Code 等 AI 客户端暴露专用工具、动态资源与提示词模板。

---

## ⚙️ 客户端快速配置 (Configuration)

### 1. Claude Desktop 配置
在你的 `claude_desktop_config.json` 中加入：

```json
{
  "mcpServers": {
    "{server-name}": {
      "command": "npx",
      "args": ["-y", "{pkg-name}"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

### 2. Cursor / Cline / VS Code 配置
在 MCP 客户端配置中添加：
- **Name**: `{server-name}`
- **Transport**: `stdio`
- **Command**: `npx -y {pkg-name}`（Node）或 `uvx {pkg-name}`（Python）

---

## 🛠️ 暴露的能力清单 (Exposed Capabilities)

### 1. Tools (可执行工具列表)
| 工具名称 | 输入参数 | 返回类型 | 功能说明 |
|---|---|---|---|
| `tool_name` | `{ query: string, limit?: number }` | `JSON` | 工具具体执行动作说明 |

### 2. Resources (只读上下文资源)
| 资源 URI 模式 | MIME 类型 | 说明 |
|---|---|---|
| `{server-name}://data/status` | `application/json` | 实时状态数据源 |

### 3. Prompts (预设提示词模板)
| 模板名称 | 参数 | 说明 |
|---|---|---|
| `analyze_report` | `{ report_id: string }` | 自动生成深度分析提示词 |

---

## 🚀 本地调试与开发

```bash
# 启动开发模式 (stdio 管道)
npm run dev

# 使用 MCP Inspector 进行交互式调试
npx @modelcontextprotocol/inspector npx {pkg-name}
```
```

---

## 品类 3：AI 模型权重与数据集 (Model & Dataset / GGUF) 完整模板

```markdown
# 🧠 模型名称 / Model Name (GGUF & Safetensors)

<div align="center">

**高性能量化开源大模型 · 支持多硬件档位 · 低显存极速推理**

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face-yellow)](https://huggingface.co/{owner}/{repo})
[![Ollama Ready](https://img.shields.io/badge/Ollama-Ready-black)](https://ollama.com/{owner}/{repo})
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

</div>

---

## ⚡ 极速开始 (One-liner Quickstart)

```bash
# 🚀 Ollama 一键拉取并运行
ollama run {owner}/{repo}

# 📦 llama.cpp 极速推理
llama-cli -m {model-name}-q4_k_m.gguf -p "你好，请做个自我介绍"
```

---

## 📊 硬件显存配置与量化矩阵 (VRAM Matrix)

| 量化版本 (Quant) | 文件大小 | 推荐显存 (VRAM) | 适用场景 |
|---|---|---|---|
| **Q4_K_M** (推荐) | ~4.2 GB | **6 GB+** (RTX 3060/4060) | 日常开发、平衡速度与精度 |
| **Q5_K_M** | ~5.1 GB | **8 GB+** | 高精度推理要求 |
| **Q8_0** | ~7.8 GB | **12 GB+** | 接近全精度基线 |
| **FP16** | ~14.5 GB | **24 GB+** (RTX 3090/4090) | 原始模型权重 |

---

## 🏆 基准评测排行榜 (Benchmark Leaderboard)

| 评测集 (Benchmark) | 本模型跑分 | 基线模型对比 | 提升幅度 |
|---|---|---|---|
| **MMLU (综合知识)** | **74.8** | 71.2 | +3.6% |
| **GSM8K (数学推理)** | **82.3** | 77.5 | +4.8% |
| **HumanEval (代码能力)** | **68.4** | 62.1 | +6.3% |

---

## 💬 提示词模版 (Prompt Format - ChatML)

```text
<|im_start|>system
你是一个专业的技术助手。<|im_end|>
<|im_start|>user
{user_query}<|im_end|>
<|im_start|>assistant
```
```

---

# 🛠️ 终端与系统开发生态

## 品类 4：系统与 CLI 诊断工具型 (CLI / System Utility) 完整模板

```markdown
# 🛠️ 工具名称 / Tool Name

<div align="center">

**专治系统级疑难杂症 · 纯只读探测 · 毫秒级数据说话 · 零破坏安全保障**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/{owner}/{repo}?sort=semver)](CHANGELOG.md)
[![Platform](https://img.shields.io/badge/Platform-Windows%2010%20%7C%2011%20%7C%2024H2-lightgrey)](SKILL.md)

</div>

---

## 📖 痛点解构

描述 3 个典型疑难用户痛点（如开网页卡死 3 秒、上行吃满、休眠唤醒延迟）。

## 📊 分层架构流程图

```
[输入: 用户遇到系统变慢 / 故障]
                 │
      [第 1 层: 物理与硬件层诊断]
                 │
      [第 2 层: 协议与系统调度诊断]
                 │
      [第 3 层: 后台资源与瓶颈定位]
                 │
      [输出: 确凿毫秒级证据链 + 官方治理建议]
```

## 🎯 常见疑难杂症实战速查表

| 典型现象 | 根因分类 | 核心排查命令 | 官方治理方案 |
|---|---|---|---|
| **现象 1** | 根因 1 | `命令 1` | 解决对策 1 |
| **现象 2** | 根因 2 | `命令 2` | 解决对策 2 |

---

## 📥 现代终端安装与运行方式 (按技术栈针对性选择)

### 选项 A：Python 现代环境运行 (推荐 uv / pipx)
```bash
# 🚀 uvx 免安装即时秒开 (最推荐)
uvx {pkg-name}

# 📦 uv tool 持久隔离安装
uv tool install {pkg-name}

# 传统 pipx 隔离安装
pipx install {pkg-name}
```

### 选项 B：Node.js / 前端环境运行
```bash
# 🚀 npx / pnpm / bun 免安装即时运行
npx {pkg-name}
pnpm dlx {pkg-name}
bunx {pkg-name}

# 全局安装
npm install -g {pkg-name}
```

### 选项 C：跨平台单行脚本直装 (Standalone Binary)
```bash
# Linux / macOS
curl -fsSL https://{domain}/install.sh | sh

# Windows PowerShell
irm https://{domain}/install.ps1 | iex
```

### 选项 D：系统级包管理器
| 操作系统 | 推荐包管理器 | 安装命令 |
|---|---|---|
| **Windows** | **Winget** | `winget install {owner}.{repo}` |
| **Windows** | **Scoop** | `scoop install {repo}` |
| **macOS / Linux** | **Homebrew** | `brew install {owner}/tap/{repo}` |
| **跨平台** | **Release 预编译包** | [下载 .exe / .zip / .tar.gz 资产](https://github.com/{owner}/{repo}/releases) |
```

---

## 品类 5：类库与核心 SDK 型 (Library / SDK) 完整模板

```markdown
# 📚 SDK 名称 / Library Name

<div align="center">

**轻量、高效、类型安全的跨平台核心 SDK · 零外部冗余依赖**

[![npm](https://img.shields.io/npm/v/{pkg-name}.svg)](https://www.npmjs.com/package/{pkg-name})
[![PyPI](https://img.shields.io/pypi/v/{pkg-name}.svg)](https://pypi.org/project/{pkg-name}/)
[![Crates.io](https://img.shields.io/crates/v/{pkg-name}.svg)](https://crates.io/crates/{pkg-name})

</div>

---

## ⚡ 5 行极简极速示例 (Hello World)

```typescript
import { createClient } from '{pkg-name}';

const client = createClient({ apiKey: process.env.API_KEY });
const result = await client.execute({ prompt: "Hello World" });
console.log(result.data);
```

## 📥 安装

| 包管理器 | 命令 |
|---|---|
| **npm** | `npm install {pkg-name}` |
| **pnpm** | `pnpm add {pkg-name}` |
| **bun** | `bun add {pkg-name}` |
| **pip** | `pip install {pkg-name}` |
| **cargo** | `cargo add {pkg-name}` |

## 📖 API 参数表格

| 方法 | 参数 | 返回值 | 说明 |
|---|---|---|---|
| `execute(options)` | `RequestOptions` | `Promise<Response>` | 执行核心请求 |
```

---

## 品类 6：基础设施代码与配置集 (IaC / Dotfiles / Helm) 完整模板

```markdown
# 🏗️ 基础设施模块 / Cloud Infrastructure

<div align="center">

**生产级声明式基础设施与环境配置 · 一键部署 · 严密安全加固**

[![Terraform](https://img.shields.io/badge/Terraform-%3E%3D1.6.0-623CE4)](https://terraform.io)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-%3E%3D1.28-326CE5)](https://kubernetes.io)

</div>

---

## 🚀 一键自动化部署 (Quick Start)

```bash
# 1. 初始化模块
terraform init

# 2. 预览计划
terraform plan -out=tfplan

# 3. 执行应用
terraform apply tfplan
```

---

## 🗺️ 资源拓扑架构与清单

```
[Internet] ──> [Cloudflare / ALB] ──> [EKS / K8s Cluster]
                                              │
                                   ┌──────────┴──────────┐
                                   ▼                     ▼
                             [App Pods]            [PostgreSQL RDS]
```

## ⚙️ 核心参数配置清单 (`variables.tf` / `values.yaml`)

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|---|---|---|---|---|
| `cluster_name` | `string` | 是 | - | Kubernetes 集群名称 |
| `node_count` | `number` | 否 | `3` | 工作节点副本数 |
| `enable_ssl` | `bool` | 否 | `true` | 是否自动开启 Let's Encrypt 证书 |
```

---

# 🎨 前端与交互应用生态

## 品类 7：前端与多媒体生成型 (Frontend / Media Generator) 完整模板

```markdown
# 🎬 项目名称 / Media Generator

<div align="center">

**高质量多媒体生成与渲染引擎 · 支持多画布比例 · 宽泛框架兼容**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![npm version](https://img.shields.io/npm/v/{pkg-name}.svg)](https://www.npmjs.com/package/{pkg-name})

</div>

---

## 🎨 视觉效果预览 (Gallery)

> 此处嵌入 WebP / MP4 / GIF 动图展示生成效果。

## 📐 画布多比例适配矩阵

| 画布比例 | 分辨率 | 适用场景 |
|---|---|---|
| **16:9** | 1920x1080 | 横屏视频 / 讲座演练 |
| **9:16** | 1080x1920 | 手机竖屏短视频 |
| **4:3** | 1440x1080 | 传统复古演示 |
| **3:4** | 1080x1440 | 社交图文短视频 |

## 📦 依赖兼容性区间

```json
{
  "dependencies": {
    "react": "^18.2.0 || ^19.0.0",
    "react-dom": "^18.2.0 || ^19.0.0",
    "remotion": "^4.0.0"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
```

## 🚀 极速开始

```bash
npm install {pkg-name}
pnpm add {pkg-name}
bun add {pkg-name}
```
```

---

## 品类 8：浏览器扩展与插件型 (Browser Extension / MV3) 完整模板

```markdown
# 🧩 扩展名称 / Browser Extension

<div align="center">

**现代轻量级浏览器效率扩展 · 零隐私追踪 · Manifest V3 标准**

[![Chrome Web Store](https://img.shields.io/badge/Chrome%20Web%20Store-Install-blue?logo=googlechrome)](https://chromewebstore.google.com/detail/{id})
[![Edge Add-ons](https://img.shields.io/badge/Edge%20Add--ons-Install-0078D7?logo=microsoftedge)](https://microsoftedge.microsoft.com/addons/detail/{id})
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

## 📥 安装方式

### 方式 A：应用商店安装（最推荐）
- [前往 Chrome 网上应用店一键安装](https://chromewebstore.google.com/detail/{id})
- [前往 Edge 外接程序商店一键安装](https://microsoftedge.microsoft.com/addons/detail/{id})

### 方式 B：开发者模式离线加载
1. 在 [Releases 页面](https://github.com/{owner}/{repo}/releases) 下载最新的 `extension.zip` 并解压；
2. 打开 Chrome / Edge 浏览器，访问 `chrome://extensions`；
3. 打开右上角的 **“开发者模式”** 开关；
4. 点击左上角 **“加载已解压的扩展程序”**，选择解压出的文件夹即可。

---

## 🔒 Manifest V3 权限用途声明

| 申请权限 (Permission) | 使用原因与场景说明 |
|---|---|
| `storage` | 仅在本地持久化存储用户的自定义主题与偏好设置 |
| `activeTab` | 仅在用户主动点击扩展图标时读取当前页面标题与 URL |
| `contextMenus` | 在右键菜单中添加快捷搜索动作 |

> 🛡️ **隐私承诺**：本扩展绝不上传任何用户浏览历史或个人数据到远程服务器。
```

---

## 品类 9：完整应用与 Web 服务型 (Fullstack App) 完整模板

```markdown
# 🌐 应用名称 / Web Service

<div align="center">

**现代化全栈 Web 应用 · 一键部署 · 开箱即用**

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/{owner}/{repo})
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template)

</div>

---

## 🚀 一键云端部署与 Docker

```bash
# Docker 运行
docker run -d -p 3000:3000 --env-file .env.production ghcr.io/{owner}/{repo}:latest

# Docker Compose
docker compose up -d
```

## ⚙️ 环境变量清单 (`.env.example`)

| 变量名 | 必填 | 默认值 | 说明 |
|---|---|---|---|
| `DATABASE_URL` | 是 | - | PostgreSQL 数据库连接串 |
| `PORT` | 否 | `3000` | 服务监听端口 |
```

---

# 📚 知识与内容生态

## 品类 10：知识库与 Awesome 精选清单 (Curated / Awesome List) 完整模板

```markdown
# 🌟 Awesome 技术精选清单 / Awesome List

<div align="center">

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Track Awesome List](https://www.trackawesomelist.com/badge.svg)](https://github.com/{owner}/{repo})
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)

**经过人工严格实测、高质量、结构化的技术生态与资源导航大全**

</div>

---

## 📖 目录导航

- [🔥 必看核心项目](#-必看核心项目)
- [🛠️ 开发辅助工具](#️-开发辅助工具)
- [📚 权威教程与文档](#-权威教程与文档)
- [🤝 收录标准与贡献准则](#-收录标准与贡献准则)

---

## 🔥 必看核心项目

- [项目名称](https://github.com/...) - 一句话精准描述项目特性与核心价值。

---

## 🤝 收录标准与贡献准则

提交 PR 推荐新项目前，请确保满足以下硬性准则：
1. **活跃度**：项目近 3 个月内有代码提交更新；
2. **完整度**：具备清晰的 README、开源协议与快速开始示例；
3. **格式规范**：遵循 `[项目名](链接) - 简明中文描述。` 格式，保持按字母排序。
```

---

## 多平台现代终端下载与安装表格集合 (2026 标准)

### 1. 现代 Python 终端生态
```markdown
| 工具 / 运行器 | 命令 | 适用说明 |
|---|---|---|
| **`uvx` (免装秒开)** | `uvx <package>` | 现代标准：即时沙箱运行，不污染环境 |
| **`uv tool` (持久安装)** | `uv tool install <package>` | 现代标准：快速安装到隔离 PATH 环境 |
| **`pipx`** | `pipx install <package>` | 传统 PyPA 隔离环境安装 |
| **`pip`** | `pip install <package>` | 传统虚拟环境内安装 |
```

### 2. 现代 JavaScript / TypeScript 终端生态
```markdown
| 工具 / 运行器 | 命令 | 适用说明 |
|---|---|---|
| **`npx`** | `npx <package>` | Node.js 官方即时运行器 |
| **`pnpm dlx`** | `pnpm dlx <package>` | pnpm 官方即时运行器 |
| **`bunx`** | `bunx <package>` | Bun 超高速即时运行器 |
| **`npm (Global)`** | `npm install -g <package>` | 全局持久安装 |
```

### 3. 系统级与编译二进制生态
```markdown
| 渠道 | 安装命令 | 适用说明 |
|---|---|---|
| **`cargo binstall`** | `cargo binstall <crate>` | Rust 预编译二进制极速安装 (无需本地编译) |
| **`cargo install`** | `cargo install <crate>` | 从 Crates.io 源码编译安装 |
| **`Homebrew`** | `brew install <owner>/tap/<package>` | macOS / Linux 软件包管理 |
| **`Winget`** | `winget install <owner>.<package>` | Windows 官方应用管理 |
| **`Scoop`** | `scoop install <package>` | Windows 开发者工具管理 |
| **`一键脚本 (Unix)`** | `curl -fsSL https://.../install.sh \| sh` | Linux / macOS 单行安装 |
| **`一键脚本 (Win)`** | `irm https://.../install.ps1 \| iex` | Windows PowerShell 单行安装 |
```
