---
name: github-oss-prep
description: "Use when preparing, publishing, launching, or improving a project for open-source adoption on GitHub. Triggers include GitHub 开源准备、准备发布到 GitHub、美化项目准备开源、开源化、开源推广、oss prep、publish to GitHub, launch an open-source project, and prepare for open source."
version: 3.3.1
---

# GitHub 开源准备

将任意项目美化为适合 GitHub 发布的版本，补齐全套社区健康文件，输出专业级仓库。

## 核心理念

- **先审后改，不盲目覆盖**：保留有效内容；已有文件若过时、残缺或存在风险，先展示差异与理由，获批后再修改
- **按项目类型适配**：Skill 项目、代码项目、文档项目的侧重点不同
- **对齐 GitHub 社区健康文件规范（按官方口径）**：README / CODE_OF_CONDUCT / LICENSE / CONTRIBUTING 等为官方点名文件，issue 模板可计分；SECURITY、资助与支持类文件按协作规模取用。官方未使用"满分/百分比"口径，本技能也不以"分数"为目标
- **可运行比"文件齐全"更重要**：用干净环境验证安装、最小示例、测试与打包路径
- **PR 默认、直推可选**：公开维护项目默认走分支、PR、CI 和人工复核；个人引导期可在明确授权后直推
- **确认后再发布**：生成内容后展示给用户确认，远程仓库、Release、包平台和外部推广分别授权

---

## 运行模式与前置条件

开源整理、隐私扫描、README 与社区文件生成、源码 ZIP 打包均不需要 GitHub 认证。只有用户明确要求"现在发布到 GitHub"时才进入认证检查。

**认证与推送策略（只读探测后选择路径，详见 `references/mcp-push-guide.md`）**：
1. 推送前做**只读探测**：连接器可用性 / `gh` 是否存在 / 两条网络可达性 / `GITHUB_TOKEN` 是否存在
2. 连接器弹窗或报"字符串绑定无效"、或 `gh` 不存在时：按 `mcp-push-guide.md` 的本机路径执行，或把推送阶段移交同机 `github-upload` 技能；其他平台保留连接器或 `gh auth login --web` 路径
3. 绝不扫描用户主目录/编辑器/MCP 配置找 Token；一次性凭据只存在于 shell 变量，永不落盘

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

### 1.1 判定项目类型（唯一分类源：`references/category-map.md`）

👉 动作：按该文件 §3 顺序执行——指纹 → 候选集 → **主产物一问**（"新用户 5 分钟内会执行或打开的那一个东西是什么"）→ 旗标 → 生命周期，产出**一个** `category_id`；落不进记 `general` + `router=unresolved`，**禁止硬套最像的一类**。

| 分类结果 | 决定什么 | 额外检查项 |
|---|---|---|
| `skill` / `mcp-server` | 品类 1/2 模板与增量、宿主矩阵、分发渠道 | frontmatter 契约、`references/` 结构、副作用与权限声明 |
| `library` / `cli` / `app` / `extension` / `iac` / `env-config` / `ci-automation` | 对应模板、必写增量、分发渠道、许可默认 | CI/CD、构建与依赖声明、干净环境可运行 |
| `model` / `dataset` / `content` | 分许可表、必写增量（来源/隐私/偏倚/引用） | 再分发权与许可链、素材署名、版本与撤回策略 |

### 1.2 对照标准检查缺失文件

GitHub 官方社区健康文件（Insights → Community 面板 + 默认社区健康文件机制，按官方原句引用）：

| # | 文件 | 位置 |
|---|------|------|
| 1 | Description | GitHub 网页 / API 创建时设置 |
| 2 | README.md | 根目录 / `.github/` / `docs/` |
| 3 | LICENSE | 根目录 / `.github/` / `docs/` |
| 4 | CODE_OF_CONDUCT.md | 根目录 / `.github/` / `docs/` |
| 5 | CONTRIBUTING.md | 根目录 / `.github/` / `docs/` |
| 6 | SECURITY.md | 根目录 / `.github/` / `docs/` |
| 7 | Issue / PR Templates | `.github/ISSUE_TEMPLATE/`、`.github/pull_request_template.md` |

> 口径说明：官方"recommended community health files"一节用 "such as" 举例 README/CODE_OF_CONDUCT/LICENSE/CONTRIBUTING，issue 模板可计分；**Description 与 Topics 不以文件形式参与计数**，`LICENSE` 不能由组织级 `.github` 仓库兜底。不要使用"7 件套/满分"这类非官方表述。

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
| CODE_OF_CONDUCT.md | 采用 Contributor Covenant（当前 3.0，附版本 URL；本仓库暂仍为 2.1，升级需维护者确认） |
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
- [ ] 无残留未替换占位符（如 `{owner}`、`{repo}`、`<your-token>` 等）
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
- 5–10 个准确 Topics，优先使用目标用户会搜索的成熟词
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

语义化版本号 (SemVer 2.0.0)：`vMAJOR.MINOR.PATCH`

| 变更类型 | 版本影响 | 示例 |
|----------|----------|------|
| 向后兼容的新功能 | 次版本增加 | v1.0.0 → v1.1.0 |
| 向后兼容的修复 | 修订号增加 | v1.1.0 → v1.1.1 |
| 不兼容的变更 | 主版本增加 | v1.1.0 → v2.0.0 |

补充：**0.y.z 为初始开发阶段**（破坏性变更同样升主版本，`1.0.0` 才定义公共 API）；预发布（`-alpha.1`）优先级低于正式版、构建元数据（`+build.1`）不参与比较；`0.x` 不要承诺兼容性。

**发布内容**：
- 标题：`v{版本号} - {简短描述}`
- 说明：按 Keep a Changelog 六类条目组织——Added / Changed / Deprecated / Removed / Fixed / **Security**（漏洞修复必须记入 Security），另含已知限制与升级指引
- 资产:ZIP 源码、Checksums 文件、安装包（如有）

### 6.2 多平台分发

依据项目类型匹配对应的发版流程：`uv publish`、`npm publish`、`huggingface-cli upload`、Chrome Web Store 上架或 Release 资产。详见 `references/release-and-distribution.md`。

### 6.3 版本一致性验证

确保版本号、CHANGELOG、Badge、Tag、Release 标题与安装链接一致。

---

## Step 7: 发现与增长

### 7.1 Launch Kit 准备

👉 动作：读取 `references/discovery-and-promotion.md#launch-kit`，按其 5 件套（一句话 / 短帖 / 长帖 / 素材 / 支持）从**同一张事实卡**逐渠道改写，不复用同一条广告文案。

### 7.2 渠道选择

| 目标用户 | 优先渠道 | 内容重点 |
|---|---|---|
| 开发者/Agent 用户 | GitHub Topics、技术社区、Show HN | 可运行演示、架构、限制、贡献入口 |
| 中文开发者 | 掘金、V2EX、知乎、公众号 | 使用场景、教程、真实效果和源码链接 |
| 创作者/非技术用户 | B 站、小红书、Product Hunt | 前后对比、操作视频、模板和上手成本 |

只选择目标用户真实存在的 2–3 个首发渠道。遵守社区自我推广规则。

### 7.3 发布节奏

👉 动作：读取 `references/discovery-and-promotion.md#发布节奏`，按 T-7 → T0 → T+7 → T+30 执行；早期项目以"三位陌生用户跑通"为成功标准，不用 Star 数代替真实采用。

---

## Reference Map

- 🗺️ **[分类主表与判定路由（唯一分类源）](references/category-map.md)** - 12 类主表 + 三轴 + 旗标 + 判定算法 + 路由回归用例（约 9.7 KB）
- 📑 **[十大品类完整 README 模板库](references/readme-template.md)** - 10 大软件形态完整开箱即用 Markdown 骨架（22.1 KB）
- 🚨 **[开源准备避坑库与官方规范基线](references/github-oss-prep-pitfalls.md)** - 社区健康文件官方口径、Git 历史凭据洗库与 CI 供应链 Action 锁定（16.1 KB）
- 🛡️ **[五重隐私与安全扫描](references/privacy-scan.md)** - 5 重扫描防御网、真伪泄露比对表；规则唯一真相源在 `scripts/secret-rules.json`（7.2 KB）
- 🏛️ **[社区健康文件与 CI 模板](references/community-templates.md)** - YAML Issue Forms、Node/Python 矩阵 CI（SHA 锁定）与 Dependabot（9.2 KB）
- 🚀 **[全渠道分发与发版指南](references/release-and-distribution.md)** - uv、npm、Hugging Face、ChromeStore、Docker 发版实操与 Checksums（6.9 KB）
- 🏷️ **[Description 与 Topics 指南](references/description-guide.md)** - ≤120 字符仓库简介与 Topics 生成指南（4.8 KB）
- 🌐 **[开源发现与推广策略](references/discovery-and-promotion.md)** - Launch Kit 营销包、社交预览与发布渠道（2.6 KB）
- 🔐 **[GitHub 推送指引（探测后选路）](references/mcp-push-guide.md)** - 只读探测 → 路径 A/B/C；与 `github-upload` 技能的关系（5.2 KB）
- 🚦 **[PR、CI 与发布门禁工作流](references/pr-and-release-workflow.md)** - 分支、PR、CI 测试与发布自动化校验（2.3 KB）
- 🔑 **[GitHub 凭据方案对比](references/github-pat-comparison.md)** - Fine-grained 与 Classic PAT 的能力与限制对比（2.6 KB）
- 🔒 **[认证与凭据最小化指引](references/github-pat-setup.md)** - 只读探测、一次性凭据与 PAT 选择（2.2 KB）
---

## 交付规范：分层诊断事实卡 (Fact Card)

在阶段 5 验证完成后，向用户汇报标准 Markdown 格式分层事实卡：

### 📊 github-oss-prep 仓库开源就绪事实卡

**填写铁律**：每个"测量实值"必须来自**当次命令的真实输出**；未运行该项检查时必须写 `未测量`（判定为 `⚪ 未测量`），并且视为 P0 阻断项。禁止照抄示例数字或默认绿色。

| 层级 | 检查项 | 测量实值 | 产生命令（附执行时间） | 判定结果 |
|---|---|---|---|:---:|
| L1 隐私安全 | 凭据 P0 / 路径与私网 P1 命中数 | {SECRETS_P0_HITS} / {PATH_P1_HITS} | `python scripts/validate_repo.py --json`（{RUN_AT}） | {SECRETS_VERDICT} / {PATH_VERDICT} |
| L1 隐私安全 | 全历史凭据（可选） | {HISTORY_RESULT} | `gitleaks detect`（{RUN_AT}） | {HISTORY_VERDICT} |
| L2 社区健康 | 官方点名健康文件 + issue 模板 | {COMMUNITY_FILES_PRESENT} | `ls` / `validate_repo.py` 文件清单（{RUN_AT}） | {COMMUNITY_VERDICT} |
| L3 供应链安全 | workflow 顶层 permissions 与 Action SHA 锁定 | {CI_PIN_RESULT} | `python scripts/validate_repo.py` 检查项 `CI-PIN`（{RUN_AT}） | {CI_VERDICT} |
| L3 自动化工程 | selftest 回归 | {SELFTEST_RESULT} | `python scripts/selftest.py`（{RUN_AT}） | {SELFTEST_VERDICT} |

判定取值：`🟢 通过` / `🟡 部分` / `🔴 失败` / `⚪ 未测量`。豁免项（`scan-ignore`）必须在表中单列一行说明理由。

【治理与发布建议（须用户明确授权后手动执行）】：
1. 确认上述指标均达标后，方可由用户授权执行远程分支推送与 Release 打包
2. 若发现历史提交包含敏感数据，先在云平台轮转吊销 Token，并提供回退对策后方可重写历史

---

> 🌏 **English**: See `README.en.md` for the English version of this skill.
