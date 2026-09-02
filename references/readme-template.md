# 六大项目品类专属 README 完整模板库

> 本文档为开源项目提供 **6 大主流品类的完整、开箱即用、可直接复制填空的 README.md 骨架**。
> 包含全套包管理器安装表（npm / pip / cargo / homebrew / winget / scoop / docker / agent 自装）、动态徽章矩阵与场景速查表。

---

## 目录

1. [动态 Badge 速查矩阵](#动态-badge-速查矩阵)
2. [品类 1：AI Agent 技能型 (Skill / Tool) 完整模板](#品类-1ai-agent-技能型-skill--tool-完整模板)
3. [品类 2：系统与 CLI 诊断工具型 (CLI / System Utility) 完整模板](#品类-2系统与-cli-诊断工具型-cli--system-utility-完整模板)
4. [品类 3：前端与多媒体生成型 (Frontend / Media Generator) 完整模板](#品类-3前端与多媒体生成型-frontend--media-generator-完整模板)
5. [品类 4：类库与核心 SDK 型 (Library / SDK) 完整模板](#品类-4类库与核心-sdk-型-library--sdk-完整模板)
6. [品类 5：完整应用与 Web 服务型 (Fullstack App) 完整模板](#品类-5完整应用与-web-服务型-fullstack-app-完整模板)
7. [品类 6：文档与知识库型 (Docs / Knowledge Base) 完整模板](#品类-6文档与知识库型-docs--knowledge-base-完整模板)
8. [多平台通用下载与安装表格集合](#多平台通用下载与安装表格集合)

---

## 动态 Badge 速查矩阵

```markdown
<!-- License 徽章 -->
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

<!-- 动态 Release 徽章（自动读取最新 Tag，严禁硬编码版本） -->
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

### 方式 A：把一句话发给任意 Agent（最推荐）

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

## 品类 2：系统与 CLI 诊断工具型 (CLI / System Utility) 完整模板

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

## 📥 安装与下载方式

| 安装渠道 | 安装命令 / 链接 |
|---|---|
| **Winget (Windows)** | `winget install {owner}.{repo}` |
| **Scoop (Windows)** | `scoop install {repo}` |
| **Homebrew (macOS)** | `brew install {owner}/tap/{repo}` |
| **Release 预编译包** | [下载 .exe / .zip 资产](https://github.com/{owner}/{repo}/releases) (含 SHA-256 校验) |
| **源码运行** | `git clone https://github.com/{owner}/{repo}.git` |
```

---

## 品类 3：前端与多媒体生成型 (Frontend / Media Generator) 完整模板

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
# npm
npm install {pkg-name}

# pnpm
pnpm add {pkg-name}

# yarn
yarn add {pkg-name}
```
```

---

## 品类 4：类库与核心 SDK 型 (Library / SDK) 完整模板

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
| **pip** | `pip install {pkg-name}` |
| **cargo** | `cargo add {pkg-name}` |

## 📖 API 参数表格

| 方法 | 参数 | 返回值 | 说明 |
|---|---|---|---|
| `execute(options)` | `RequestOptions` | `Promise<Response>` | 执行核心请求 |
```

---

## 品类 5：完整应用与 Web 服务型 (Fullstack App) 完整模板

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

## 品类 6：文档与知识库型 (Docs / Knowledge Base) 完整模板

```markdown
# 📚 知识库名称 / Knowledge Base

<div align="center">

**权威、全面、结构化的技术知识库与最佳实践指南**

</div>

---

## 🗺️ 知识索引与分类地图

- [📁 架构设计指南](#)
- [📁 安全规范与合规](#)
- [📁 性能调优实战](#)

## 🤝 知识贡献准则

提交新条目时请遵循：
1. 必须提供官方来源链接或实测验证数据；
2. 保持中英双语术语一致。
```

---

## 多平台通用下载与安装表格集合

在任意 README 中，可根据项目实际支持的渠道选择复制以下安装表格：

### 1. 包管理器一览表
```markdown
| 平台 / 包管理器 | 安装命令 | 说明 |
|---|---|---|
| **npm (Global)** | `npm install -g <package>` | 全局安装命令行工具 |
| **npx (无需安装)** | `npx <package>` | 临时直接执行 |
| **pip (Python)** | `pip install <package>` | 从 PyPI 安装模块 |
| **cargo (Rust)** | `cargo install <package>` | 从 Crates.io 编译安装 |
| **Homebrew (macOS)**| `brew install <owner>/tap/<package>` | macOS/Linux 软件包管理 |
| **Winget (Windows)** | `winget install <owner>.<package>` | Windows 官方应用管理 |
| **Scoop (Windows)** | `scoop install <package>` | Windows 开发者工具管理 |
```

### 2. 容器与镜像一览表
```markdown
| 镜像源 | 拉取命令 |
|---|---|
| **GitHub Container Registry** | `docker pull ghcr.io/<owner>/<repo>:latest` |
| **Docker Hub** | `docker pull <owner>/<repo>:latest` |
```
