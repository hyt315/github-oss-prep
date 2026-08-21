<div align="center">

# 🚀 GitHub 开源准备 / GitHub OSS Prep

**一键把任意本地项目，变成专业级 GitHub 开源仓库。**

**One-click polish any project into a professional GitHub open-source repo.**

[![CI](https://github.com/hyt315/github-oss-prep/actions/workflows/validate.yml/badge.svg)](https://github.com/hyt315/github-oss-prep/actions)
[![Release](https://img.shields.io/github/v/release/hyt315/github-oss-prep?sort=semver)](https://github.com/hyt315/github-oss-prep/releases)
[![License: MIT](https://img.shields.io/github/license/hyt315/github-oss-prep)](LICENSE)
[![Stars](https://img.shields.io/github/stars/hyt315/github-oss-prep?style=social)](https://github.com/hyt315/github-oss-prep/stargazers)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1f6feb)](SKILL.md)
[![skills.sh](https://skills.sh/b/hyt315/github-oss-prep)](https://skills.sh/hyt315/github-oss-prep)

**简体中文 · [English](./README.en.md)**

</div>

> **Status:** v1.6.2 · 本地整理与 ZIP 交付**不需要 GitHub Token** · 发布到 GitHub 需你显式授权 · 只读审计，不主动推送。

---

## 中文

### 📖 这是什么？

想把本地项目开源，却怕漏了 API Key、不会写 README、不懂发版门禁？
**GitHub 开源准备** 是一个 AI Agent Skill：它自动**扫描项目 → 补齐社区健康文件 → 隐私扫描 → 采用性验证 → 安全发布**，让"开源"从一堆脏活儿变成一个动作。

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
| 🔎 **元数据闭环** | 发布时真正写入并回读验证 Description 与 Topics；无认证时明确交付手动待办 |
| 🌐 **中英双语** | 所有生成文件支持中英双语，符合 GitHub 全球社区最佳实践 |
| 📦 **多平台分发** | 代码项目支持 npm、PyPI、crates.io、Docker Hub、Homebrew 等多渠道发布 |

---

### 😰 为什么需要？(对号入座)

开源最怕的不是"不会写代码"，而是这些**看不见的坑**：

- **敏感信息外泄**：硬编码 API Key、本地私有路径悄悄混进提交
- **身份暴露**：提交历史里的企业邮箱/工号，开源后永久公开
- **杂质文件**：`.idea`、`.vscode`、`.env` 误推上 GitHub
- **门面丢分**：README 单语、无 License、无贡献指南，别人不敢用
- **发版翻车**：不会打 Release、版本号对不上、下载链接 404

「GitHub 开源准备」就是为这 5 类问题设计的——它扫描、补全、验证，把翻车概率降到最低。

---

## 🚀 快速开始

这是一个 AI Agent Skill，**装进任意 AI 助手里就能用**。三种方式，任选其一：

### 方式 A：复制一句话给任意 Agent（推荐，最通用）

把下面这句话发给你的 AI 助手，它自己会判断平台、克隆到正确的 skills 目录：

> 请安装 GitHub 开源准备 Skill：把 `https://github.com/hyt315/github-oss-prep`
> 克隆到你的 skills 目录（如 `~/.claude/skills/github-oss-prep`），并确认安装成功。

> 💡 **小模型也能用**：装完后你只要会说"帮我把这个项目开源"，它就会触发。

### 方式 B：已装 GitHub CLI 2.90+（一行命令）

```bash
gh skill install hyt315/github-oss-prep github-oss-prep --agent claude-code --scope user
# 把 claude-code 换成 codex / cursor / github-copilot 等
```

### 方式 C：Claude Code / Codex 插件市场

```bash
/plugin marketplace add hyt315/github-oss-prep
```

### 方式 D：手动分平台安装

| 平台 | 安装命令 |
|------|----------|
| **Claude Code** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.claude/skills/github-oss-prep` |
| **Codex** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.codex/skills/github-oss-prep` |
| **Cursor** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.cursor/skills/github-oss-prep` |

> 安装后即可完成**扫描、整理、隐私检查和 ZIP 交付，全程不需要 GitHub Token**；只有最终发布才需要授权。

### 怎么用

装好后直接告诉 AI 助手你的意图，它会自动执行 **定位 → 扫描 → 整理 → 验证 → 仓库门面 → PR/发布 → Release → 发现与增长**。整理和 ZIP 交付不需要 GitHub 认证；远程发布、Release 和外部推广**分别确认**，绝不越权。

---

## 🔒 安全与隐私（敢装才装）

- **默认只读审计**，不主动推送、不改动你的文件内容（有问题是"报告"给你，不是"替你改"）
- **不读取**你的源码、`.env`、密钥、用户主目录或 MCP 配置
- 公开项目默认走**分支 + Draft PR + 人工合并**，绝不直接推到你的 `main`
- 整理与 ZIP 交付**不需要 Token**；只有你明确说"发布"时才进入认证流程
- 发布、Release、包平台、对外推广**四件事分别授权**，前一步授权不扩展到后一步

---

## 📥 下载 / Download

| 方式 | 命令 / 链接 |
|------|------------|
| **HTTPS** | `git clone https://github.com/hyt315/github-oss-prep.git` |
| **SSH** | `git clone git@github.com:hyt315/github-oss-prep.git` |
| **GitHub CLI** | `gh repo clone hyt315/github-oss-prep` |
| **ZIP 源码** | [下载 ZIP](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.zip) |
| **Tar 源码** | [下载 Tar](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.tar.gz) |
| **单文件（SKILL.md）** | `curl -O https://raw.githubusercontent.com/hyt315/github-oss-prep/main/SKILL.md` |

### GitHub 发布认证（仅需最终发布时）

推荐顺序：

1. 使用 AI 平台提供的官方 GitHub 连接器；
2. 或在受信任终端运行 `gh auth login --web`；
3. 两者均不可用时，Skill 仍会输出完整源码目录、ZIP、Description 和 Topics，供网页手动上传。

不要把 PAT 写进公开仓库、聊天记录或 Git remote URL。需要 MCP 时，请使用 GitHub 当前维护的 [`github/github-mcp-server`](https://github.com/github/github-mcp-server)；旧的 `@modelcontextprotocol/server-github` npm 包已停止维护。

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
├── README.md                         # 本文件（中文）
├── README.en.md                      # 英文版
├── CHANGELOG.md                      # 版本变更记录
├── LICENSE                           # MIT 协议
├── .gitignore                        # Git 忽略规则
├── CONTRIBUTING.md                   # 贡献指南
├── CODE_OF_CONDUCT.md                # 行为准则
├── SECURITY.md                       # 安全策略
├── SUPPORT.md                        # 支持渠道
├── agents/
│   └── openai.yaml                   # Codex/OpenAI 技能元数据
├── scripts/
│   ├── validate_repo.py              # 结构/密钥/版本一致性自检
│   └── selftest.py                   # 回归测试（维护者改动后必跑）
├── .github/
│   ├── CODEOWNERS                    # 自动指派 reviewer
│   ├── pull_request_template.md      # PR 模板
│   ├── workflows/
│   │   └── validate.yml              # CI：自动跑 validate_repo.py
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.yml            # Bug 报告表单
│       ├── feature_request.yml       # 功能建议表单
│       ├── doc_improvement.yml       # 文档改进表单
│       └── config.yml                # 模板选择器配置
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

1. **安装**：复制"快速开始"里那段话发给 AI 助手 → 自动装好
2. **扫描**：识别为文档项目 → 发现缺少 LICENSE、README、.gitignore
3. **补齐**：生成对应文件，内容适配文档项目特性
4. **审查**：隐私扫描通过，文件内容确认无误
5. **交付**：确认仓库名和 Topics → 连接器/`gh` 发布，或输出 ZIP 手动上传
6. **完成**：本地开源包一定可交付；授权可用时同步发布到 GitHub

---

## ❓ 常见问题 FAQ

- **Q：不会用命令行也能装吗？** A：能。用"方式 A"——把那句话复制给任意 AI 助手，它帮你装。
- **Q：小模型/弱模型能用吗？** A：能。触发词很简单（如"帮我把这个项目开源"），无需复杂配置。
- **Q：装了会不会偷偷推到我 GitHub？** A：不会。默认只读、不主动推送；发布需你**显式确认**。
- **Q：不装 GitHub Token 能不能用？** A：能。扫描、整理、ZIP 交付都不需要 Token，只有最终发布要授权。
- **Q：它是怎么保证我项目安全的？** A：只读审计、不读源码/`.env`/密钥、公开项目走 Draft PR。详见上方"安全与隐私"。

---

## 🤝 贡献

请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。如果本技能帮助了你，欢迎 [Star ⭐](https://github.com/hyt315/github-oss-prep/stargazers) 或提 [Issue](https://github.com/hyt315/github-oss-prep/issues)。

---

## 📄 许可

[MIT](LICENSE)

版本变化见 [CHANGELOG.md](CHANGELOG.md)。

---

> 🌏 **English version: [README.en.md](./README.en.md)**
