---
name: github-oss-prep
description: "Use when preparing, publishing, launching, or improving a project for open-source adoption on GitHub. Triggers include GitHub 开源准备、准备发布到 GitHub、美化项目准备开源、开源化、开源推广、oss prep、publish to GitHub, launch an open-source project, and prepare for open source."
---

# GitHub 开源准备

将任意项目美化为适合 GitHub 发布的版本，补齐全套社区健康文件，输出专业级仓库。

## 核心理念

- **先审后改，不盲目覆盖**：保留有效内容；已有文件若过时、残缺或存在风险，先展示差异与理由，获批后再修改
- **按项目类型适配**：Skill 项目、代码项目、文档项目的侧重点不同
- **对齐 GitHub 社区配置文件标准**：目标是通过 Insights → Community 中 100% 的考核
- **可运行比"文件齐全"更重要**：用干净环境验证安装、最小示例、测试与打包路径
- **PR 默认、直推可选**：公开维护项目默认走分支、PR、CI 和人工复核；个人引导期可在明确授权后直推
- **确认后再发布**：生成内容后展示给用户确认，远程仓库、Release、包平台和外部推广分别授权

---

## 运行模式与前置条件

开源整理、隐私扫描、README 与社区文件生成、源码 ZIP 打包均不需要 GitHub 认证。只有用户明确要求"现在发布到 GitHub"时才进入认证检查。

**安全策略**：
1. 优先使用当前平台已安装的官方 GitHub 连接器
2. 若使用本机 GitHub CLI，只运行 `gh auth status` 检查状态
3. 不扫描用户主目录、编辑器配置或 MCP 配置来寻找 Token
4. 如果用户明确选择 PAT，指导用户在 GitHub 官方页面创建最小权限凭据

---

## 工作流程

```
Step 0: 定位（目标用户 + 核心价值 + 可验证结果）
    ↓
Step 1: 扫描（识别类型 + 检查缺失、薄弱与风险项）
    ↓
Step 2: 整理（补齐缺失文件 + 经确认改进薄弱文件）
    ↓
Step 3: 验证（内容 + 隐私 + 来源许可 + 干净环境运行）
    ↓
Step 4: 仓库门面（README + Description + Topics + 社交预览）
    ↓
Step 5: 发布确认 → 分支/PR（默认）或个人直推（可选）
    ↓
Step 6: Release + 多平台分发 + 版本一致性验证
    ↓
Step 7: 发现与增长（Launch Kit + 定向发布 + 反馈闭环）
```

---

## Step 0: 定位与成功标准

开始改文件前先用现有项目资料回答四个问题：

1. **谁会用**：首要用户只能有一类，次要用户最多两类
2. **解决什么**：用"用户在什么场景下，原来多麻烦，现在少几步"描述
3. **五分钟证明**：确定一个新用户可复现的最小示例和预期输出
4. **本次边界**：区分"准备开源""发布 GitHub""创建 Release""对外推广"，不得把前一步授权扩展到后一步

输出一张简短定位卡：目标用户、核心承诺、最小示例、证据、非目标。详见 `references/discovery-and-promotion.md`。

---

## Step 1: 扫描项目

### 1.1 识别项目类型

| 信号 | 类型 | 额外检查项 |
|------|------|-----------|
| 存在 `SKILL.md` | AI Agent Skill | 检查 YAML frontmatter、references/结构 |
| 存在 `package.json` / `setup.py` / `Cargo.toml` | 代码项目 | 检查 CI/CD、构建说明、依赖声明 |
| 纯 Markdown 文件（无代码） | 文档/方法论 | 重点评估 README 质量和内容结构 |
| SKILL.md + 代码混合 | Skill + 工具 | 按 Skill 类型处理，额外检查可执行脚本 |

### 1.2 对照标准检查缺失文件

GitHub 官方 Community Profile 考核项（Insights → Community）：

| # | 文件 | 位置 |
|---|------|------|
| 1 | Description | GitHub 网页 / API 创建时设置 |
| 2 | README.md | 根目录 / `.github/` / `docs/` |
| 3 | LICENSE | 根目录 / `.github/` / `docs/` |
| 4 | CODE_OF_CONDUCT.md | 根目录 / `.github/` / `docs/` |
| 5 | CONTRIBUTING.md | 根目录 / `.github/` / `docs/` |
| 6 | SECURITY.md | 根目录 / `.github/` / `docs/` |
| 7 | Issue / PR Templates | `.github/ISSUE_TEMPLATE/` |

---

## Step 2: 补齐并改进文件

> **检查点**：向用户展示 Step 1 的结果（项目类型 + 缺失清单），确认后进入补齐。

**生成要点**：
- 中英双语（中文项目可全中文，建议保留英文摘要）
- 内容精准适配项目类型，不套通用模板
- 生成前先简要说明将要创建的内容，获得用户认可
- 已有文件先按"准确、清楚、可运行、可维护"评分；只在确有收益时提出修改，并展示摘要或 diff
- 不因文件存在就自动判定合格，也不为统一模板而抹掉项目原有表达

| 文件 | 生成要点 |
|------|----------|
| README.md | 适配项目类型，突出核心价值，含快速开始和使用示例 |
| LICENSE | 根据项目类型选择合适的许可证（推荐 MIT/Apache 2.0） |
| CODE_OF_CONDUCT.md | 采用 Contributor Covenant 2.1 |
| CONTRIBUTING.md | 贡献流程、分支规范、PR 提交指南 |
| SECURITY.md | 私有漏洞报告渠道、响应 SLA、支持版本矩阵 |

---

## Step 3: 验证与审查

> **检查点**：向用户展示 Step 2 生成的文件列表和内容摘要，确认后进行审查。

### 3.1 内容质量审查

- [ ] README 5 秒内可懂，至少一个可运行示例
- [ ] 无敏感信息（API Key、邮箱、内网路径）
- [ ] 文件引用路径正确（相对路径），中英双语结构对应
- [ ] Emoji 图标增强可读性，核心特性用表格展示
- [ ] README 引用 LICENSE，不超过 512 KB
- [ ] 无残留 `<owner>`/`<repo>` 等未替换占位符
- [ ] 下载链接的分支名与仓库实际默认分支一致

### 3.2 隐私二次验证

推送前最终检查（防止 Step 2 生成的文件引入新泄露）：
- [ ] 所有文件中无真实 API Key / Token / Secret
- [ ] 无真实邮箱、手机号、身份证号、包含真实用户名的文件路径
- [ ] 无私网 IP、内网域名、数据库连接串
- [ ] 占位符（`你的 API 密钥`、`example@xxx.com`）不算泄露，保留

### 3.3 来源、许可与可复现性门禁

- [ ] 项目代码、逆向分析产物、图片、字体、音频、数据集和示例内容均有可公开分发的权利或许可证
- [ ] 第三方依赖、NOTICE、字体/素材署名与许可证文件完整
- [ ] 不只扫描工作区，还检查将要提交的 Git 树与可访问历史中是否含秘密
- [ ] 从干净目录或全新 clone 按 README 完成安装、最小示例、测试和构建
- [ ] Windows/macOS/Linux 支持范围写清楚；未测试的平台明确标为未验证
- [ ] 一键脚本失败时有可执行的手动步骤和故障排查

验证方法与发布门禁见 `references/pr-and-release-workflow.md`。任何 P0（秘密、许可不明、无法复现）失败都必须阻止公开发布。

---

## Step 4: 仓库门面与 Description

按规则生成仓库简介。**规则 + 模板 + 案例 + Topics 建议** 详见 `references/description-guide.md`。

简要原则：
- 120 字以内，`功能 + 亮点`
- 禁止「一个用于…的项目」式废话、版本号
- 按项目类型选用模板

同时准备：
- 5–12 个准确 Topics，优先使用目标用户会搜索的成熟词
- 1280×640 社交预览图方案，展示用途或结果
- README 首屏的"一句话价值 + 结果图/GIF + 最短安装 + 最小示例"
- 3 个真实示例或一个 60–90 秒演示

---

## Step 5: 推送到 GitHub

### 5.1 展示确认清单

向用户展示仓库名、Description、Topics、文件列表，**等待明确确认**。

### 5.2 创建仓库 + 推送

**方案选择**：优先使用当前平台已安装的官方 GitHub 连接器；否则使用已完成 `gh auth login --web` 的 GitHub CLI；两者都不可用时交付 ZIP 和网页上传说明。详细流程见 `references/mcp-push-guide.md`。

**仓库元数据是发布必做项，不是建议项**：远程仓库创建或代码推送成功后，必须实际设置已确认的 Description 和 Topics，并从 GitHub 回读验证。不能只在回复中列出 Topics。若当前认证方式无法修改元数据，则把每个未完成项标为 `待手动设置`，给出精确值与网页路径。

发布后最少验证：仓库 URL、可见性、默认分支、Description、Topics、README/文件树和最新 CI 状态。

### 5.3 选择变更路径

默认使用 `public-safe`：
1. 从最新默认分支创建短生命周期分支
2. AI 修改、运行验证并提交
3. 推送分支并创建 Draft PR
4. 展示 diff、验证结果和剩余风险，由人复核
5. CI 通过后 Squash Merge

仅当项目由单人维护、改动低风险且用户明确同意时使用 `solo-fast` 直推。完整决策表见 `references/pr-and-release-workflow.md`。

---

## Step 6: Release + 多平台分发

> **检查点**：Step 5 推送完成后进入本步骤。如果是纯文档/方法论项目，可跳过 6.2-6.4，只做 6.1。

### 6.1 创建首个 GitHub Release

语义化版本号 (SemVer): `v 主版本。次版本。修订号`

| 变更类型 | 版本影响 | 示例 |
|----------|----------|------|
| 新功能 | 次版本增加 | v1.0.0 → v1.1.0 |
| 修复 bug | 修订号增加 | v1.1.0 → v1.1.1 |
| 重大变更 | 主版本增加 | v1.1.0 → v2.0.0 |

**发布内容**：
- 标题：`v{版本号} - {简短描述}`
- 说明：新增功能、修复问题、已知限制、升级指引
- 资产:ZIP 源码、Checksums 文件、安装包（如有）

### 6.2 多平台分发

依据项目类型匹配对应的发版流程：`uv publish`、`npm publish`、`huggingface-cli upload`、Chrome Web Store 上架或 Release 资产。详见 `references/release-and-distribution.md`。

### 6.3 版本一致性验证

确保版本号、CHANGELOG、Badge、Tag、Release 标题与安装链接一致。

---

## Step 7: 发现与增长

### 7.1 Launch Kit 准备

为每个渠道从同一事实卡改写，而不是复制粘贴同一广告：
1. **一句话**：用户 + 痛点 + 可验证结果
2. **短帖**：问题、演示、链接、一个明确提问
3. **长帖**：为什么做、关键取舍、演示、限制、路线图
4. **素材**：社交卡、GIF/视频、3 张截图、替代文本
5. **支持**：安装、FAQ、Known issues、Issue/Discussion 链接

### 7.2 渠道选择

| 目标用户 | 优先渠道 | 内容重点 |
|---|---|---|
| 开发者/Agent 用户 | GitHub Topics、技术社区、Show HN | 可运行演示、架构、限制、贡献入口 |
| 中文开发者 | 掘金、V2EX、知乎、公众号 | 使用场景、教程、真实效果和源码链接 |
| 创作者/非技术用户 | B 站、小红书、Product Hunt | 前后对比、操作视频、模板和上手成本 |

只选择目标用户真实存在的 2–3 个首发渠道。遵守社区自我推广规则。

### 7.3 发布节奏

- **T-7 到 T-1**：陌生人测试、修安装、准备演示与 FAQ
- **T0**：发布 Release，更新 Topics/社交卡，再发首批渠道
- **T+1 到 T+7**：快速回复 Issue，记录安装失败点，发布一次改进说明
- **T+30**：按有效反馈决定路线图，不用 Star 数代替真实采用

对早期项目，三位陌生用户成功跑通，比一次短期曝光更有价值。

---

## Reference Map

- 📑 **[十大品类完整 README 模板库](references/readme-template.md)** - 10 大软件形态完整开箱即用 Markdown 骨架（预计阅读时间：4 分钟）
- 🚨 **[开源准备避坑库与官方规范基线](references/github-oss-prep-pitfalls.md)** - GitHub Insights 100% 门禁、Git 历史凭据残留洗库与 CI 供应链 Action 锁定（预计阅读时间：4 分钟）
- 🛡️ **[五重隐私与安全扫描](references/privacy-scan.md)** - 5 重扫描防御网、真伪泄露实战比对表与脱敏规则（预计阅读时间：3 分钟）
- 🏛️ **[社区健康文件与 CI 模板](references/community-templates.md)** - 现代交互式 YAML Issue Forms、Node/Python 矩阵 CI 工作流与 Dependabot（预计阅读时间：3 分钟）
- 🚀 **[全渠道分发与发版指南](references/release-and-distribution.md)** - uv、npm、HuggingFace、ChromeStore、Docker 发版实操、国内镜像源与 Checksums（预计阅读时间：4 分钟）
- 🏷️ **[Description 与 Topics 指南](references/description-guide.md)** - 精准 120 字仓库简介与高权重标签生成指南（预计阅读时间：3 分钟）
- 🌐 **[开源发现与推广策略](references/discovery-and-promotion.md)** - Launch Kit 营销包、社交预览与全网发布渠道（预计阅读时间：3 分钟）
- 🔐 **[GitHub 推送与 MCP 指引](references/mcp-push-guide.md)** - 官方 MCP 与标准 CLI 推送流程（预计阅读时间：2 分钟）
- 🚦 **[PR、CI 与发布门禁工作流](references/pr-and-release-workflow.md)** - 分支、PR、CI 测试与发布自动化校验（预计阅读时间：3 分钟）

---

## 交付规范：分层诊断事实卡 (Fact Card)

在阶段 5 验证完成后，向用户汇报标准 Markdown 格式分层事实卡：

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

---

> 🌏 **English**: See `README.en.md` for the English version of this skill.
