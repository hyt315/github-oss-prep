# README.md 模板参考

以下为 README.md 的推荐结构和各部分说明。根据项目类型按需选用。

---

## 目录

- [基础结构（中英双语版）](#基础结构中英双语版)
- [中英双语 README 最佳实践](#中英双语-readme-最佳实践)
- [按项目类型补充](#按项目类型补充)
- [Badge 速查](#badge-速查)
- [五秒测试](#五秒测试)
- [README SEO 优化](#readme-seo-优化)
- [社交预览图片](#社交预览图片)
- [README.en.md 英文版编写指南](#readmeenmd-英文版编写指南)

## 基础结构（中英双语版）

```markdown
# 📊 项目名 / Project Name

<div align="center">

**一句话中文描述**

**One-liner English description**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](CHANGELOG.md)
[![GitHub Stars](https://img.shields.io/github/stars/用户名/仓库名?style=social)](https://github.com/用户名/仓库名/stargazers)

[English](#english) | [中文](#中文)

</div>

---

## 中文

## 📖 这是什么？

（2-3 段说明项目的核心价值和解决的问题）

### ✨ 核心特性

| 特性 | 说明 |
|------|------|
| 🔄 **特性 1** | 说明 |
| 📊 **特性 2** | 说明 |
| 🧠 **特性 3** | 说明 |

---

## 🚀 快速开始

（最小化可运行示例，让用户在 1 分钟内跑起来）

---

## 📥 安装 / Installation

根据项目类型选择对应的安装方式表格：

**代码项目（有包管理器）**：

| 方式 | 命令 |
|------|------|
| **npm** | `npm install -g <package>` |
| **npx**（不安装直接用） | `npx <package>` |
| **pip**（Python 项目） | `pip install <package>` |
| **cargo**（Rust 项目） | `cargo install <package>` |

**Skill 项目（AI Agent）**：

| 平台 | 命令 |
|------|------|
| **Claude Code** | `git clone https://github.com/<owner>/<repo>.git ~/.claude/skills/<repo>` |
| **Codex** | `git clone https://github.com/<owner>/<repo>.git ~/.codex/skills/<repo>` |
| **Cursor** | `git clone https://github.com/<owner>/<repo>.git ~/.cursor/skills/<repo>` |

---

## 📥 下载 / Download

源码和编译产物的所有下载方式：

**源码下载**：

| 方式 | 命令/链接 |
|------|----------|
| **HTTPS** | `git clone https://github.com/<owner>/<repo>.git` |
| **SSH** | `git clone git@github.com:<owner>/<repo>.git` |
| **GitHub CLI** | `gh repo clone <owner>/<repo>` |
| **ZIP 源码** | `[下载 ZIP](https://github.com/<owner>/<repo>/archive/refs/heads/main.zip)` |
| **Tar 源码** | `[下载 Tar](https://github.com/<owner>/<repo>/archive/refs/heads/main.tar.gz)` |
| **单文件** | `curl -O https://raw.githubusercontent.com/<owner>/<repo>/main/核心文件名` |

**编译产物下载**（如有 Release）：

| 平台 | 下载链接 |
|------|----------|
| **Windows** | [下载 .exe](https://github.com/<owner>/<repo>/releases/latest) |
| **macOS** | [下载 .dmg](https://github.com/<owner>/<repo>/releases/latest) |
| **Linux** | [下载 .AppImage](https://github.com/<owner>/<repo>/releases/latest) |
| **全部版本** | [Releases 页面](https://github.com/<owner>/<repo>/releases) |

---

## 📁 文件结构

```
项目名/
├── 核心文件        # 说明
├── README.md       # 本文件
└── references/     # 参考文件
```

---

## 📚 示例

（截图、代码示例、或链接到 references/）

---

## 🤝 贡献

（链接到 CONTRIBUTING.md）

---

## 📄 许可

[MIT](LICENSE)

---

## English

## 📖 What is this?

（英文版内容，结构与中文版对应）

### ✨ Core Features

| Feature | Description |
|---------|-------------|
| 🔄 **Feature 1** | Description |
| 📊 **Feature 2** | Description |
| 🧠 **Feature 3** | Description |

---

## 🚀 Quick Start

（英文版快速开始）

---

## 📁 File Structure

（英文版文件结构）

---

## 📚 Examples

（英文版示例）

---

## 🤝 Contributing

（英文版贡献指南）

---

## 📄 License

[MIT](LICENSE)
```

---

## 中英双语 README 最佳实践

### 语言切换

在顶部使用锚点链接实现语言切换：
```markdown
[English](#english) | [中文](#中文)
```

在对应章节前使用 Markdown 标题作为锚点（GitHub 会自动为标题生成 ID）：
```markdown
## 中文
## 📖 这是什么？

## English
## 📖 What is this?
```

> **注意**：GitHub 不支持 `<a name="xxx">` HTML 锚点标签，只有 Markdown 标题（`#`）会自动生成可跳转的锚点 ID。

### 视觉元素

1. **Emoji 图标**：每个章节标题前添加 Emoji，增强可读性
   - 📖 介绍/What is this
   - ✨ 特性/Features
   - 💡 理念/Philosophy
   - 📊 数据/图表
   - 🚀 快速开始/Quick Start
   - 📁 文件结构/File Structure
   - 📚 示例/Examples
   - 🤝 贡献/Contributing
   - 📄 许可/License

2. **居中显示**：标题和徽章使用 `<div align="center">` 居中

3. **徽章**：
   - License、Version、Build Status
   - GitHub Stars（社交证明）
   - Agent Skill（如果是 Skill 项目）

4. **表格**：用表格展示核心特性、数据分层等结构化信息

### 核心特性表格

用表格展示项目的核心功能，每个特性一行：

```markdown
### ✨ 核心特性

| 特性 | 说明 |
|------|------|
| 🔄 **特性名称 1** | 简要说明这个特性解决了什么问题 |
| 📊 **特性名称 2** | 简要说明实现方式或技术亮点 |
| 🧠 **特性名称 3** | 简要说明用户能获得的价值 |
```

---

## 按项目类型补充

### 代码项目

- **安装**：`npm install` / `pip install` / `cargo build` 等
- **依赖**：列出关键依赖及版本
- **构建**：如何构建
- **测试**：如何运行测试
- **API 文档**：如果有

### Skill 项目（AI Agent）

- **触发方式**：什么场景触发、关键词
- **前置条件**：需要什么 MCP/Plugin
- **输出示例**：执行后的产物示意

**安装命令**（针对主流 AI Agent 平台）：

```markdown
**一行命令安装**：

| 平台 | 安装命令 |
|------|----------|
| **Claude Code** | `git clone https://github.com/<owner>/<repo>.git ~/.claude/skills/<repo>` |
| **Codex** | `git clone https://github.com/<owner>/<repo>.git ~/.codex/skills/<repo>` |
| **Cursor** | `git clone https://github.com/<owner>/<repo>.git ~/.cursor/skills/<repo>` |
```

**Skills 目录路径说明**：

| 平台 | 个人级（全局） | 项目级 |
|------|---------------|--------|
| **Claude Code** | `~/.claude/skills/` | `.claude/skills/`（项目根目录） |
| **Codex** | `~/.codex/skills/` | `.codex/skills/`（项目根目录） |
| **Cursor** | `~/.cursor/skills/` | `.cursor/skills/` 或 `.agents/skills/`（项目根目录） |

**注意**：
- 安装命令应针对 Claude Code、Codex、Cursor 等主流 AI Agent 平台，而不是非主流或内部工具
- 每个 Skill 都要有自己的文件夹，不要把 SKILL.md 直接扔进 skills/ 根目录
- 个人级安装对所有项目生效，项目级安装只对当前项目生效

### 文档/方法论项目

- **谁需要这个**：目标用户画像
- **体系概览**：方法论的核心框架图
- **端到端示例**：一个完整的案例

---

## Badge 速查

```
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)]()
[![SKILL.md](https://img.shields.io/badge/Agent%20Skill-SKILL.md-green)](SKILL.md)
```

---

## 五秒测试

打开 README，闭上眼睛数 5 秒后睁开——你能在 5 秒内说出这个项目是干什么的吗？

如果不能，说明缺少：
- 一个精准的一句描述
- 一个具体的应用场景

---

## README SEO 优化

README 不直接是排名因素，但通过影响**用户行为和参与度指标**间接影响 SEO：

**必须包含的内容**：
- 清晰说明项目是什么、为谁而做
- 安装和运行指南
- 所用技术列表
- 快速上手指南
- 截图或 GIF 展示效果
- 可复制的代码示例
- 语言、许可证、构建状态等徽章
- 链接到网站、文档或社交媒体

**SEO 友好性**：
- 结构清晰、关键词明确（如包含 `OAuth2`、`Next.js` 等技术术语）
- 更容易被 Google 抓取和索引，有机会出现在外部搜索结果中

---

## 社交预览图片

在仓库 Settings → Social preview 中设置：
- **尺寸**：1280×640 像素
- **格式**：PNG 或 JPG
- **内容**：项目名称 + 一句话描述 + 视觉元素
- **影响**：社交媒体分享时的展示效果（Twitter、LinkedIn、Discord 等）

---

## README.en.md 英文版编写指南

### 为什么需要英文版

- GitHub 是全球平台，英文版提高可发现性
- 方便国际用户了解和使用项目
- 提升 SEO（搜索引擎优化）

### 文件结构

创建独立的 `README.en.md` 文件，与 `README.md` 并列放在仓库根目录。

### 语言切换链接

在两个文件顶部添加语言切换链接：

**README.md（中文版）**：
```markdown
> 🌏 **English version: [README.en.md](./README.en.md)**
```

**README.en.md（英文版）**：
```markdown
> 🌏 **中文版: [README.md](./README.md)**
```

### 编写原则

1. **结构对应**：英文版结构与中文版完全对应，章节标题、表格、代码块一一对应
2. **内容一致**：核心信息保持一致，不要添加中文版没有的内容
3. **自然翻译**：不要机械翻译，确保英文表达自然流畅
4. **技术术语**：技术术语保持英文原样，不要翻译

### 章节对照表

| 中文章节 | 英文章节 |
|----------|----------|
| 📖 这是什么？ | 📖 What is this? |
| ✨ 核心特性 | ✨ Core Features |
| 🚀 快速开始 | 🚀 Quick Start |
| 💡 核心理念 | 💡 Core Philosophy |
| 📁 文件结构 | 📁 File Structure |
| 📚 端到端示例 | 📚 End-to-End Example |
| 🤝 贡献 | 🤝 Contributing |
| 📄 许可 | 📄 License |

### 示例模板

```markdown
# 📊 Project Name

> 🌏 **中文版: [README.md](./README.md)**

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" />
  <img src="https://img.shields.io/badge/version-1.0.0-green.svg?style=flat-square" />
  <img src="https://img.shields.io/badge/Agent%20Skill-SKILL.md-green.svg?style=flat-square" />
  <img src="https://img.shields.io/badge/Platform-Claude%20Code-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Platform-Cursor-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/github/stars/用户名/仓库名?style=flat-square&color=yellow" />
</p>

---

## 📖 What is this?

（英文版介绍，与中文版对应）

---

## ✨ Core Features

| Feature | Description |
|---------|-------------|
| 🔄 **Feature 1** | Description |
| 📊 **Feature 2** | Description |
| 🧠 **Feature 3** | Description |

---

## 🚀 Quick Start

（英文版快速开始 — 根据项目类型填写对应的安装/使用方式）

---

## 💡 Core Philosophy

（英文版核心理念 — 与中文版对应）

---

## 📁 File Structure

（英文版文件结构 — 与中文版对应）

---

## 📚 Examples

（英文版示例 — 与中文版对应）

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📄 License

[MIT](LICENSE)
```
