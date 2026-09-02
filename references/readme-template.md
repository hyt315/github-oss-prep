# 六大项目品类专属 README 模板引擎

> 本文档提供 6 大类开源项目的针对性 README 门面结构规范与实战模板。
> 核心原则：**对标 2026 顶级开源门面标准、拒绝千篇一律、首屏 5 秒看懂、零私有路径泄露**。

---

## 目录

1. [品类 1：AI Agent 技能型 (Skill / Tool)](#品类-1ai-agent-技能型-skill--tool)
2. [品类 2：系统与 CLI 诊断工具型 (CLI / System Utility)](#品类-2系统与-cli-诊断工具型-cli--system-utility)
3. [品类 3：前端与多媒体生成型 (Frontend / Media Generator)](#品类-3前端与多媒体生成型-frontend--media-generator)
4. [品类 4：类库与核心 SDK 型 (Library / SDK)](#品类-4类库与核心-sdk-型-library--sdk)
5. [品类 5：完整应用与 Web 服务型 (Fullstack App)](#品类-5完整应用与-web-服务型-fullstack-app)
6. [品类 6：文档与知识库型 (Docs / Knowledge Base)](#品类-6文档与知识库型-docs--knowledge-base)
7. [动态 Badge 速查与防踩坑](#动态-badge-速查与防踩坑)

---

## 品类 1：AI Agent 技能型 (Skill / Tool)

**适用代表**：`github-oss-prep`、`skill-doctor` 等 AI 助手扩展技能。

### 核心设计要求
- 顶部居中 Header：双语一句话定位 + Agent Skills 兼容徽章 + 动态 Release 徽章。
- **快速开始第一屏必须提供：方式 A（一句话发给 Agent 自动安装）**，极致降低使用门槛。
- 跨平台标准安装路径（`~/.claude/`、`~/.codex/`、`~/.cursor/`、`~/.agents/`），**严禁出现任何本地私有盘符与机器路径**。
- 单层 Reference Map：标明各参考文档的阅读时机与时间估算。
- Zero-Token 本地执行与只读安全承诺。

---

## 品类 2：系统与 CLI 诊断工具型 (CLI / System Utility)

**适用代表**：`windows-cleanup-optimize`、`network-slow-diagnosis` 等系统级工具。

### 核心设计要求
- 用户痛点剖析：用 2~3 个真实场景痛点开篇。
- **ASCII 流程图 / 架构判定树**：让用户一眼看懂分层排查或清理逻辑。
- **6 大疑难杂症实战速查表**：以“典型现象 → 根因分类 → 核心排查命令 → 官方治理方案”表格呈现。
- **安全铁律声明**：明确声明 Dry-Run 试跑、只读优先（Zero Mutation）或零破坏（Zero Harm）。
- **操作系统与权限兼容矩阵**：标明 Windows 10/11/24H2、Linux、macOS 支持度与管理员权限需求。

---

## 品类 3：前端与多媒体生成型 (Frontend / Media Generator)

**适用代表**：`notebook-video`、Remotion 渲染工程、Canvas 视觉组件等。

### 核心设计要求
- **视觉效果 Gallery 演示**：首屏放置高画质 WebP / MP4 / GIF 动图展示实际生成效果。
- **多画布比例兼容矩阵**：清晰说明 16:9 宽屏、4:3 讲座、3:4 社交短片、9:16 竖屏短视频适配。
- **宽泛依赖兼容区间**：标明框架依赖范围（如 `react: ^18.2.0 || ^19.0.0`，`remotion: ^4.0.0`）。
- **资产流水线与渲染流程**：从输入文案/素材到最终 MP4 导出的流水线图。

---

## 品类 4：类库与核心 SDK 型 (Library / SDK)

**适用代表**：npm 包、PyPI 库、Rust Crate 等供其他开发者调用的库。

### 核心设计要求
- 包管理器安装徽章（npm / PyPI / Crates.io / NuGet）。
- **5 行极简极速 Hello World 代码块**：1 分钟内让开发者跑通最小示例。
- **TypeScript / Python 类型定义与完整 API 参数表格**。
- **错误处理范式与 SemVer 向后兼容性承诺**。

---

## 品类 5：完整应用与 Web 服务型 (Fullstack App)

**适用代表**：独立 Web 应用、Electron 桌面端、全栈服务端。

### 核心设计要求
- 在线 Live Demo 体验按钮 + 1 键云端部署按钮（Vercel / Docker / Railway）。
- `.env.example` 环境变量完整配置清单与必填项说明。
- 前后端通信架构与数据库拓扑图。

---

## 品类 6：文档与知识库型 (Docs / Knowledge Base)

**适用代表**：技术指南、Curated 资源清单、架构标准库。

### 核心设计要求
- 树状思维导图与全量知识分类索引。
- 知识收录与贡献准则（Content Inclusion Criteria）。
- 自动化链接健康检查与引用格式规范。

---

## 动态 Badge 速查与防踩坑

### 动态 Badge 官方标准语法
```markdown
<!-- License -->
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

<!-- 动态 Release (自动读取 GitHub 最新 Release，严禁写死版本号) -->
[![Release](https://img.shields.io/github/v/release/{owner}/{repo}?sort=semver)](https://github.com/{owner}/{repo}/releases)

<!-- Agent Skills 兼容标记 -->
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1f6feb)](SKILL.md)

<!-- 平台支持 -->
[![Platform](https://img.shields.io/badge/Platform-Windows%2010%20%7C%2011%20%7C%2024H2-lightgrey)](SKILL.md)

<!-- GitHub Stars -->
[![GitHub Stars](https://img.shields.io/github/stars/{owner}/{repo}?style=social)](https://github.com/{owner}/{repo}/stargazers)
```

### 避坑铁律
1. **严禁硬编码版本号**：绝不要写 `badge/version-1.1.0-blue`，一律使用动态 API 徽章。
2. **严禁本地盘符与用户名**：安装命令中必须使用标准 `~/.claude/skills/...`，不得出现真实机器路径。
