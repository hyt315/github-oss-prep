# 📦 GitHub 开源准备 / GitHub OSS Prep

<div align="center">

**将任意项目美化为适合 GitHub 发布的专业级开源版本，补齐全套社区健康文件与 CI 自动化，构建专属针对性门面与全生态分发。**

**Turn any project into a polished, GitHub-ready open-source repository with full community health files, CI automation, and tailored multi-channel distribution.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/hyt315/github-oss-prep?sort=semver)](CHANGELOG.md)
[![Validate skill](https://github.com/hyt315/github-oss-prep/actions/workflows/validate.yml/badge.svg)](https://github.com/hyt315/github-oss-prep/actions)
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

它覆盖的不只是「补齐文件」，而是从**定位 → 扫描 → 整理 → 验证 → 门面 → 发布 → 分发 → 增长**的完整开源交付闭环，并且**每一步的授权边界都独立**：本地整理、远程推送、发布 Release、对外推广，四件事分别确认，绝不越权连带执行。

## 🎯 什么时候用它？

| 你说的话 | 技能会做的事 |
|---|---|
| 「帮我准备开源」「准备发布到 GitHub」 | 走完整 Step 0–7 流程，从定位卡开始 |
| 「美化一下项目」「README 太糙了」 | 识别项目品类 → 定向调阅专属模板 → 重构 README |
| 「看看有没有敏感信息会泄露」 | 执行五重隐私安全扫描 + Git 历史凭据残留检查 |
| 「社区健康度不满 100%」 | 对照 Insights → Community 七件套逐项补齐 |
| 「怎么发版 / 发到 PyPI / npm / HuggingFace」 | 调阅全渠道分发指南，输出对应发版指令 |
| 「帮我写仓库简介和 Topics」 | 按 120 字规则生成 Description + 5–12 个 Topics |
| 「推上去 / 创建 Release」 | 先展示确认清单，等待明确授权后才执行 |

> 本地整理、扫描、生成文档、打包 ZIP **全部无需 GitHub 认证**；只有你明确说「现在发布到 GitHub」时才会进入认证检查。

## ✨ 核心特性

| 核心特性 | 功能说明 | 带来价值 |
|---|---|---|
| **十大全景品类 README 引擎** | 覆盖 AI Skill、MCP Server、AI 模型/GGUF、CLI 工具、多媒体、SDK、浏览器扩展、IaC 配置、Web 应用、Awesome 清单 | 告别泛化概念，直接复制填空，精准呈现各类项目核心卖点 |
| **渐进式披露执行铁律** | 依据品类判定结果定向调阅专属规范，严格隔离无关品类 | 杜绝上下文膨胀与跨品类交叉污染，生成质量 100% 聚焦 |
| **五重深度隐私安全网** | 拦截 API Key、私有路径指纹、内部会话 ID、Git Remote Token、构建缓存，附带**真伪泄露案例比对表** | 100% 杜绝敏感凭据与个人开发环境泄露 |
| **2026 社区与 CI 自动化库** | 交互式 YAML Issue Forms、PR 模板、`SECURITY.md`、**Node/Python 矩阵 CI** 与 **Dependabot** | 轻松获得 GitHub Community Profile 100% 满分并实现依赖自动安全更新 |
| **全生态分发与发版实操** | **uv/PyPI、npm、Hugging Face、Chrome Web Store、Docker、Homebrew、Crates.io** 具体发版指南与 Release Checksums | 提供从本地代码到全球各大分发中心的全流程发版指令 |
| **完整开源交付闭环** | 定位 → 扫描 → 整理 → 验证 → 门面 → 发布 → Release/分发 → 推广增长，共 8 个阶段 | 不止「文件齐全」，而是「能被陌生人跑通并被真实采用」 |
| **分阶段授权与安全推送** | 四类操作独立授权；默认 `public-safe` 分支/PR 流程，可选 `solo-fast` 直推 | 高危操作（推送/发版/推广）永远由人按下最后一下 |
| **轻量规范化工程架构** | 主干精简，单层 Reference Map 直达，配齐自动化回归自测 | 严守工程纪律，`skill-doctor` 37 项审查 100% PASS |

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

```bash
python scripts/selftest.py
```

预期输出：

```
SELFTEST PASS (all AST syntax, positive, negative, and integration checks passed)
```

安装后的第一次使用建议：

> 用 github-oss-prep 扫描当前项目，先只输出定位卡和缺失清单，不要修改任何文件。

---

## 🔄 开源准备全流程架构

```
[输入：本地任意待开源项目 / 目录]
                 │
      [Step 0: 定位（目标用户 + 核心价值 + 可验证结果）]
      精准判定：AI Skill / MCP Server / 模型权重 / CLI 工具 / 浏览器扩展 / IaC / ...
                 │
      [Step 1: 扫描（识别类型 + 检查缺失、薄弱与风险项）]
      对照 GitHub Community Profile 考核项检查
                 │
      [Step 2: 整理（补齐缺失文件 + 经确认改进薄弱文件）]
      生成中英双语社区健康文件
                 │
      [Step 3: 验证（内容 + 隐私 + 来源许可 + 干净环境运行）]
      五重深度安全扫描，确保无敏感信息泄露
                 │
      [Step 4: 仓库门面（README + Description + Topics + 社交预览）]
      渐进式披露，定向调阅专属品类完整骨架
                 │
      [Step 5: 发布确认 → 分支/PR（默认）或个人直推（可选）]
      public-safe 或 solo-fast 双模式
                 │
      [Step 6: Release + 多平台分发 + 版本一致性验证]
      uv/PyPI/npm/HuggingFace/ChromeStore/Docker/Homebrew/Crates.io
                 │
      [Step 7: 发现与增长（Launch Kit + 定向发布 + 反馈闭环）]
      Stranger Test、渠道选择、发布节奏
```

## 🧭 七条不可动摇的执行原则

1. **先审后改，不盲目覆盖**：保留有效内容；已有文件若过时、残缺或存在风险，先展示差异与理由，获批后再修改。
2. **按项目类型适配**：Skill 项目、代码项目、文档项目的侧重点不同，不套通用模板。
3. **对齐 GitHub 社区配置文件标准**：目标是通过 Insights → Community 中 100% 的考核。
4. **可运行比「文件齐全」更重要**：用干净环境验证安装、最小示例、测试与打包路径。
5. **PR 默认、直推可选**：公开维护项目默认走分支、PR、CI 和人工复核；个人引导期可在明确授权后直推。
6. **确认后再发布**：生成内容后展示给用户确认，远程仓库、Release、平台发版和外部推广**分别授权**。
7. **不因文件存在就判定合格**：也不为统一模板而抹掉项目原有表达。

## 🧩 Step 0–7 逐步详解

### Step 0 · 定位与成功标准

开始改文件前，先用现有项目资料回答四个问题：

| # | 问题 | 要求 |
|---|---|---|
| 1 | **谁会用** | 首要用户只能有一类，次要用户最多两类 |
| 2 | **解决什么** | 用「用户在什么场景下，原来多麻烦，现在少几步」描述 |
| 3 | **五分钟证明** | 确定一个新用户可复现的最小示例和预期输出 |
| 4 | **本次边界** | 区分「准备开源」「发布 GitHub」「创建 Release」「对外推广」，不得把前一步授权扩展到后一步 |

产出物：一张简短**定位卡** —— 目标用户、核心承诺、最小示例、证据、非目标。详见 [`references/discovery-and-promotion.md`](references/discovery-and-promotion.md)。

### Step 1 · 扫描项目

**1.1 识别项目类型**

| 信号 | 类型 | 额外检查项 |
|------|------|-----------|
| 存在 `SKILL.md` | AI Agent Skill | 检查 YAML frontmatter、references/ 结构 |
| 存在 `package.json` / `setup.py` / `Cargo.toml` | 代码项目 | 检查 CI/CD、构建说明、依赖声明 |
| 纯 Markdown 文件（无代码） | 文档/方法论 | 重点评估 README 质量和内容结构 |
| SKILL.md + 代码混合 | Skill + 工具 | 按 Skill 类型处理，额外检查可执行脚本 |

**1.2 对照 GitHub 官方 Community Profile 检查缺失文件**

| # | 文件 | 位置 |
|---|------|------|
| 1 | Description | GitHub 网页 / API 创建时设置 |
| 2 | README.md | 根目录 / `.github/` / `docs/` |
| 3 | LICENSE | 根目录 / `.github/` / `docs/` |
| 4 | CODE_OF_CONDUCT.md | 根目录 / `.github/` / `docs/` |
| 5 | CONTRIBUTING.md | 根目录 / `.github/` / `docs/` |
| 6 | SECURITY.md | 根目录 / `.github/` / `docs/` |
| 7 | Issue / PR Templates | `.github/ISSUE_TEMPLATE/` |

### Step 2 · 补齐并改进文件

> **检查点**：向用户展示 Step 1 的结果（项目类型 + 缺失清单），确认后进入补齐。

**生成要点**
- 中英双语（中文项目可全中文，建议保留英文摘要）
- 内容精准适配项目类型，不套通用模板
- 生成前先简要说明将要创建的内容，获得用户认可
- 已有文件先按「准确、清楚、可运行、可维护」评分；只在确有收益时提出修改，并展示摘要或 diff
- 不因文件存在就自动判定合格，也不为统一模板而抹掉项目原有表达

| 文件 | 生成要点 |
|------|----------|
| README.md | 适配项目类型，突出核心价值，含快速开始和使用示例 |
| LICENSE | 根据项目类型选择合适的许可证（推荐 MIT/Apache 2.0） |
| CODE_OF_CONDUCT.md | 采用 Contributor Covenant 2.1 |
| CONTRIBUTING.md | 贡献流程、分支规范、PR 提交指南 |
| SECURITY.md | 私有漏洞报告渠道、响应 SLA、支持版本矩阵 |

### Step 3 · 验证与审查

> **检查点**：向用户展示 Step 2 生成的文件列表和内容摘要，确认后进行审查。

**3.1 内容质量审查**

- [ ] README 5 秒内可懂，至少一个可运行示例
- [ ] 无敏感信息（API Key、邮箱、内网路径）
- [ ] 文件引用路径正确（相对路径），中英双语结构对应
- [ ] Emoji 图标增强可读性，核心特性用表格展示
- [ ] README 引用 LICENSE，不超过 512 KB
- [ ] 无残留未替换的仓库所有者/名称占位符
- [ ] 下载链接的分支名与仓库实际默认分支一致

**3.2 隐私二次验证**（推送前最终检查，防止 Step 2 生成的文件引入新泄露）

- [ ] 所有文件中无真实 API Key / Token / Secret
- [ ] 无真实邮箱、手机号、身份证号、包含真实用户名的文件路径
- [ ] 无私网 IP、内网域名、数据库连接串
- [ ] 占位符（`你的 API 密钥`、`example@xxx.com`）不算泄露，保留

**3.3 来源、许可与可复现性门禁**

- [ ] 项目代码、逆向分析产物、图片、字体、音频、数据集和示例内容均有可公开分发的权利或许可证
- [ ] 第三方依赖、NOTICE、字体/素材署名与许可证文件完整
- [ ] 不只扫描工作区，还检查将要提交的 Git 树与可访问历史中是否含秘密
- [ ] 从干净目录或全新 clone 按 README 完成安装、最小示例、测试和构建
- [ ] Windows/macOS/Linux 支持范围写清楚；未测试的平台明确标为未验证
- [ ] 一键脚本失败时有可执行的手动步骤和故障排查

> **P0 门禁**：秘密泄露、许可不明、无法复现 —— 任何一项失败都必须**阻止公开发布**。验证方法与发布门禁见 [`references/pr-and-release-workflow.md`](references/pr-and-release-workflow.md)。

### Step 4 · 仓库门面与 Description

按规则生成仓库简介，**规则 + 模板 + 案例 + Topics 建议** 详见 [`references/description-guide.md`](references/description-guide.md)。

简要原则：
- 120 字以内，`功能 + 亮点`
- 禁止「一个用于…的项目」式废话、禁止版本号
- 按项目类型选用模板

同时准备：
- 5–12 个准确 Topics，优先使用目标用户会搜索的成熟词
- 1280×640 社交预览图方案，展示用途或结果
- README 首屏的「一句话价值 + 结果图/GIF + 最短安装 + 最小示例」
- 3 个真实示例或一个 60–90 秒演示

### Step 5 · 推送到 GitHub

**5.1 展示确认清单**：向用户展示仓库名、Description、Topics、文件列表，**等待明确确认**。

**5.2 创建仓库 + 推送**

优先使用当前平台已安装的官方 GitHub 连接器；否则使用已完成 `gh auth login --web` 的 GitHub CLI；两者都不可用时交付 ZIP 和网页上传说明。详细流程见 [`references/mcp-push-guide.md`](references/mcp-push-guide.md)。

> **仓库元数据是发布必做项，不是建议项**：远程仓库创建或代码推送成功后，必须实际设置已确认的 Description 和 Topics，并从 GitHub 回读验证。不能只在回复中列出 Topics。若当前认证方式无法修改元数据，则把每个未完成项标为 `待手动设置`，给出精确值与网页路径。

发布后最少验证：仓库 URL、可见性、默认分支、Description、Topics、README/文件树和最新 CI 状态。

**5.3 选择变更路径**

| 路径 | 适用条件 | 流程 |
|---|---|---|
| **`public-safe`（默认）** | 公开维护项目、多人协作 | 从最新默认分支创建短生命周期分支 → AI 修改、验证并提交 → 推送分支并创建 Draft PR → 展示 diff、验证结果与剩余风险 → 人复核 → CI 通过后 Squash Merge |
| **`solo-fast`（可选）** | 单人维护、改动低风险、用户明确同意 | 直接推送到默认分支 |

**5.4 认证安全策略**

1. 优先使用当前平台已安装的官方 GitHub 连接器
2. 若使用本机 GitHub CLI，只运行 `gh auth status` 检查状态
3. **不扫描**用户主目录、编辑器配置或 MCP 配置来寻找 Token
4. 如果用户明确选择 PAT，指导用户在 GitHub 官方页面创建最小权限凭据

凭据方案对比见 [`references/github-pat-comparison.md`](references/github-pat-comparison.md)，最小权限创建步骤见 [`references/github-pat-setup.md`](references/github-pat-setup.md)。

### Step 6 · Release + 多平台分发

**6.1 创建首个 GitHub Release**

语义化版本号（SemVer）：`v主版本.次版本.修订号`

| 变更类型 | 版本影响 | 示例 |
|----------|----------|------|
| 新功能 | 次版本增加 | v1.0.0 → v1.1.0 |
| 修复 bug | 修订号增加 | v1.1.0 → v1.1.1 |
| 重大变更 | 主版本增加 | v1.1.0 → v2.0.0 |

**发布内容**
- 标题：`v 版本号 - 简短描述`
- 说明：新增功能、修复问题、已知限制、升级指引
- 资产：ZIP 源码、Checksums 文件、安装包（如有）

**6.2 多平台分发**：依据项目类型匹配对应的发版流程 —— `uv publish`、`npm publish`、`huggingface-cli upload`、Chrome Web Store 上架或 Release 资产。详见 [`references/release-and-distribution.md`](references/release-and-distribution.md)。

**6.3 版本一致性验证**：确保版本号、CHANGELOG、Badge、Tag、Release 标题与安装链接**全部一致**。

> 纯文档/方法论项目可跳过 6.2–6.3，只做 6.1。

### Step 7 · 发现与增长

**7.1 Launch Kit 准备** —— 为每个渠道从同一事实卡改写，而不是复制粘贴同一广告：

1. **一句话**：用户 + 痛点 + 可验证结果
2. **短帖**：问题、演示、链接、一个明确提问
3. **长帖**：为什么做、关键取舍、演示、限制、路线图
4. **素材**：社交卡、GIF/视频、3 张截图、替代文本
5. **支持**：安装、FAQ、Known issues、Issue/Discussion 链接

**7.2 渠道选择**

| 目标用户 | 优先渠道 | 内容重点 |
|---|---|---|
| 开发者/Agent 用户 | GitHub Topics、技术社区、Show HN | 可运行演示、架构、限制、贡献入口 |
| 中文开发者 | 掘金、V2EX、知乎、公众号 | 使用场景、教程、真实效果和源码链接 |
| 创作者/非技术用户 | B 站、小红书、Product Hunt | 前后对比、操作视频、模板和上手成本 |

> 只选择目标用户真实存在的 **2–3 个**首发渠道，并遵守社区自我推广规则。

**7.3 发布节奏**

| 时间 | 动作 |
|---|---|
| **T-7 ~ T-1** | 陌生人测试、修安装、准备演示与 FAQ |
| **T0** | 发布 Release，更新 Topics/社交卡，再发首批渠道 |
| **T+1 ~ T+7** | 快速回复 Issue，记录安装失败点，发布一次改进说明 |
| **T+30** | 按有效反馈决定路线图，不用 Star 数代替真实采用 |

> 对早期项目，**三位陌生用户成功跑通**，比一次短期曝光更有价值。

## 🚦 检查点与授权边界

| 阶段 | 是否需要用户确认 | 需要 GitHub 认证 |
|---|---|---|
| Step 0–1 定位与扫描 | 输出后确认 | ❌ 不需要 |
| Step 2 生成社区健康文件 | **检查点：确认缺失清单后** | ❌ 不需要 |
| Step 3 验证与隐私扫描 | **检查点：确认文件列表后** | ❌ 不需要 |
| Step 4 README / Description / Topics | 展示待设置值 | ❌ 不需要 |
| Step 5 推送到 GitHub | **检查点：确认仓库名、Description、Topics、文件列表** | ✅ 需要 |
| Step 6 创建 Release / 平台发版 | **检查点：逐个平台授权** | ✅ 需要 |
| Step 7 对外推广 | **检查点：逐个渠道授权** | ❌ 不需要 |
| 交付 ZIP / 本地打包 | 无需额外授权 | ❌ 不需要 |

## 🧪 内置工程与自检工具

本技能自带可离线运行的质量防线，无需网络、无需第三方依赖：

| 工具 | 用途 | 命令 |
|---|---|---|
| `scripts/validate_repo.py` | 校验必需文件、相对路径引用、占位符残留与敏感信息，支持 JSON 输出 | `python scripts/validate_repo.py`<br>`python scripts/validate_repo.py --json` |
| `scripts/selftest.py` | 回归自测：AST 语法检查 + 正向校验 + 反向安全断言 + 避坑库深度断言 + 集成测试 | `python scripts/selftest.py` |
| `tests/test_skill.py` | Pytest 可发现的测试入口，封装完整自测套件 | `pytest tests/` |

**持续集成**：`.github/workflows/validate.yml` 在每次 PR 与 push 到 `main` 时自动运行校验，权限收敛为 `contents: read`（只读顶层权限，防止 CI 供应链投毒）。

## 📊 交付示例：分层诊断事实卡

验证完成后，技能会以标准 Markdown 分层事实卡汇报结果（示例）：

### 📊 github-oss-prep 仓库开源就绪事实卡

| 层级 | 检查项 | 测量实值 | 正常基线 | 判定结果 |
|---|---|---|---|:---:|
| L1 隐私安全 | 敏感凭据/API Key | 0 处命中 | 0 处泄漏 | 🟢 合规 |
| L1 隐私安全 | 本地绝对路径指纹 | 0 处命中 | 0 处暴露 | 🟢 合规 |
| L2 社区健康 | GitHub Insights 7 件套 | 100% 具备 | 100% 完整 | 🟢 完备 |
| L2 社区规范 | YAML Issue Forms | 已配置 | 全量 YAML | 🟢 标准 |
| L3 供应链安全 | CI permissions 顶层只读 | contents: read | contents: read | 🟢 安全 |
| L3 自动化工程 | scripts/selftest.py 回归 | 100% PASS | 0 阻断 0 失败 | 🟢 通过 |

【治理与发布建议（须用户明确授权后手动执行）】：
1. 确认上述指标均达标后，方可由用户授权执行远程分支推送与 Release 打包
2. 若发现历史提交包含敏感数据，先在云平台轮转吊销 Token，并提供回退对策后方可重写历史

## 📁 仓库结构

```
github-oss-prep/
├── SKILL.md                          # 技能主文件：7 步工作流、门禁与交付规范
├── README.md / README.en.md          # 中英双语文档
├── manifest.json                     # 版本单一事实来源（当前 3.2.0）
├── CHANGELOG.md                      # 遵循 Keep a Changelog 的版本演进
├── LICENSE                           # MIT
├── CONTRIBUTING.md                   # 贡献流程与 PR 规范
├── CODE_OF_CONDUCT.md                # Contributor Covenant
├── SECURITY.md                       # 漏洞披露渠道与响应 SLA
├── SUPPORT.md                        # 支持渠道说明
├── agents/
│   └── openai.yaml                   # Codex / OpenAI 平台元数据
├── references/                       # 11 篇渐进式披露参考文档
├── scripts/
│   ├── selftest.py                   # 离线回归自测
│   └── validate_repo.py              # 仓库结构与敏感信息校验
├── tests/
│   └── test_skill.py                 # Pytest 入口
└── .github/
    ├── CODEOWNERS
    ├── ISSUE_TEMPLATE/               # 3 个交互式 YAML 表单 + config
    ├── pull_request_template.md
    └── workflows/validate.yml        # 只读权限 CI
```

## 📖 深度参考文档导读

> 遵循渐进式披露原则：只需在对应阶段调阅相关文档，无需通读全部。

| 参考文档 | 核心内容 | 推荐阅读时机 | 预估耗时 |
|---|---|---|---|
| 📑 [**十大品类完整 README 模板库 (`readme-template.md`)**](references/readme-template.md) | 10 大软件形态完整开箱即用 Markdown 骨架与现代终端运行器表 | 为项目生成或重构 README 时 | 4 分钟 |
| 🚨 [**开源准备避坑库与官方规范基线 (`github-oss-prep-pitfalls.md`)**](references/github-oss-prep-pitfalls.md) | GitHub Insights 100% 门禁、Git 历史凭据残留洗库与 CI 供应链 Action 锁定 | 制定发布门禁与排查疑难坑时 | 4 分钟 |
| 🛡️ [**五重隐私与安全扫描 (`privacy-scan.md`)**](references/privacy-scan.md) | 5 重扫描防御网、真伪泄露实战比对表与脱敏规则 | 执行本地安全自检与脱敏排查时 | 3 分钟 |
| 🏛️ [**社区健康文件与 CI 模板 (`community-templates.md`)**](references/community-templates.md) | 现代交互式 YAML Issue Forms、Node/Python 矩阵 CI 工作流与 Dependabot | 补齐 GitHub 社区文件与持续集成时 | 3 分钟 |
| 🚀 [**全渠道分发与发版指南 (`release-and-distribution.md`)**](references/release-and-distribution.md) | uv、npm、HuggingFace、ChromeStore、Docker 发版实操、国内镜像源与 Checksums | 发布到全球平台或 GitHub Release 时 | 4 分钟 |
| 🏷️ [**Description 与 Topics 指南 (`description-guide.md`)**](references/description-guide.md) | 精准 120 字仓库简介与高权重标签生成指南 | 设置 GitHub 仓库门面信息时 | 3 分钟 |
| 🌐 [**开源发现与推广策略 (`discovery-and-promotion.md`)**](references/discovery-and-promotion.md) | Launch Kit 营销包、社交预览与全网发布渠道 | 准备发布与对外推广项目时 | 3 分钟 |
| 🔐 [**GitHub 推送与 MCP 指引 (`mcp-push-guide.md`)**](references/mcp-push-guide.md) | 官方 MCP 与标准 CLI 推送流程 | 执行远程推送与仓库创建时 | 2 分钟 |
| 🚦 [**PR 与发布门禁工作流 (`pr-and-release-workflow.md`)**](references/pr-and-release-workflow.md) | 分支、PR、CI 测试与发布自动化校验 | 建立持续集成与发版流水线时 | 3 分钟 |
| 🔑 [**GitHub 凭据方案对比 (`github-pat-comparison.md`)**](references/github-pat-comparison.md) | 官方连接器、GitHub CLI 与 PAT 的权限与安全对比 | 选择推送认证方式时 | 2 分钟 |
| 🔒 [**最小权限 PAT 创建指引 (`github-pat-setup.md`)**](references/github-pat-setup.md) | 在 GitHub 官方页面创建最小权限个人访问令牌的步骤 | 明确选择 PAT 方式时 | 1 分钟 |

## 🌐 GitHub 开源全生命周期套件

面向开源维护者与贡献者的完整生产级工具链：

| 阶段 / 角色 | 推荐技能 | 核心使命与能力 | GitHub 仓库 |
|---|---|---|---|
| 📦 **发布前准备** | [**`github-oss-prep`**](https://github.com/hyt315/github-oss-prep) | 仓库脚手架自动化、中英双语 README、CI 工作流与合规检查 | [hyt315/github-oss-prep](https://github.com/hyt315/github-oss-prep) |
| 🩺 **质量体检** | [**`skill-doctor`**](https://github.com/hyt315/skill-doctor) | 50+ 工业级静态规则 + 动态自测运行器，保障 Agent Skill 100% 可靠 | [hyt315/skill-doctor](https://github.com/hyt315/skill-doctor) |
| ⚙️ **发布后运维** | [**`github-oss-ops`**](https://github.com/hyt315/github-oss-ops) | Issue 分诊、AI 幻觉防御、PR 审查、GHSA 漏洞 SOP 与多渠道播报 | [hyt315/github-oss-ops](https://github.com/hyt315/github-oss-ops) |
| 🚀 **贡献者导航** | [**`github-oss-contribute`**](https://github.com/hyt315/github-oss-contribute) | 端到端贡献指南：Fork 同步、Rebase 冲突解决、DCO 签署与反 AI 灌水门禁 | [hyt315/github-oss-contribute](https://github.com/hyt315/github-oss-contribute) |

## ❓ 常见问题 FAQ

**Q：这个技能会自动往我的 GitHub 推东西吗？**
不会。推送、创建 Release、对外推广都是独立检查点，必须等你明确授权。默认只做本地整理与报告。

**Q：必须装 GitHub CLI 或配置 Token 吗？**
不必须。扫描、隐私检查、生成文档、打包 ZIP 全部离线可用。只有真的要推远程才需要认证。

**Q：会覆盖我现有的 README / 社区文件吗？**
不会盲目覆盖。已有文件先按「准确、清楚、可运行、可维护」评分，只在确有收益时提出修改，并先展示摘要或 diff。

**Q：它是通用模板吗？**
不是。它按 10 大项目品类（AI Skill、MCP Server、模型/GGUF、CLI、SDK、扩展、IaC、Web 应用、多媒体、Awesome 清单）分别提供专属骨架，并严格隔离无关品类。

**Q：怎么验证这个技能本身没坏？**
`python scripts/selftest.py` 一条命令即可完成语法、正向、反向安全与集成四类检查；CI 也会在每次 PR 自动执行。

**Q：发现历史提交里有密钥怎么办？**
先在云平台轮转吊销该凭据，再评估历史重写方案 —— 仅删除文件不等于从 Git 历史中移除，详见避坑库。

## 🤝 贡献

欢迎提交 Issue 与 PR。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。

提交前请确保本仓库自测通过：

```bash
python scripts/selftest.py
python scripts/validate_repo.py
```

安全漏洞请勿公开提交 Issue，请按 [SECURITY.md](SECURITY.md) 的私有渠道报告。

## 🔒 安全与隐私原则

- **纯只读 / 先审后改（Audit Before Change）**：本地整理默认只读扫描并输出差异报告，绝不擅自强行覆盖用户现有文件。
- **渐进式隔离（Progressive Isolation）**：处理特定项目时仅读取专属模板，杜绝上下文冗余与环境参数污染。
- **五重严密防御**：对代码、文档、`.git/config` 与历史提交进行全面深度扫描，阻断任何敏感信息。
- **分阶段明确授权**：本地开源整理、远程仓库创建、Release 打包分发与外部推广分别独立确认，绝不越权连带执行。
- **零 Token 发现行为**：不扫描用户主目录、编辑器配置或 MCP 配置来寻找凭据；只使用平台官方连接器或已登录的 GitHub CLI。
- **零 Token 本地运行 / 零运行时依赖**：内置脚本为纯 Python 标准库实现，不引入第三方包，也不产生任何 API 调用费用。

## 📥 下载与获取

| 方式 | 命令 / 链接 |
|---|---|
| **HTTPS** | `git clone https://github.com/hyt315/github-oss-prep.git` |
| **SSH** | `git clone git@github.com:hyt315/github-oss-prep.git` |
| **GitHub CLI** | `gh repo clone hyt315/github-oss-prep` |
| **ZIP 压缩包** | [下载 ZIP](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.zip) |
| **Tar 归档** | [下载 Tar](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.tar.gz) |
| **单文件 (SKILL.md)** | `curl -O https://raw.githubusercontent.com/hyt315/github-oss-prep/main/SKILL.md` |

## 📄 开源协议

本项目采用 [MIT 许可证](LICENSE) 开源。

详见 [CHANGELOG.md](CHANGELOG.md) 了解版本演进历史。

---

> 🌏 **English: [README.en.md](./README.en.md)**