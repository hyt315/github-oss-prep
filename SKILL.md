---
name: github-oss-prep
description: "Use when preparing, publishing, launching, or improving a project for open-source adoption on GitHub. Triggers include GitHub 开源准备、准备发布到 GitHub、美化项目准备开源、开源化、开源推广、oss prep、publish to GitHub, launch an open-source project, and prepare for open source."
license: MIT
metadata:
  version: "3.3.2"
---

# GitHub 开源准备

把一个项目整理成适合在 GitHub 公开的仓库：补齐社区健康文件，做隐私与许可检查，写好 README 与仓库门面，再按授权推送、发版和推广。

## 核心原则

- **先审后改**：保留有效内容；已有文件过时、残缺或有风险时，先给出差异和理由，获批再改。
- **按项目类型适配**：先判定类型，再取对应模板，不套通用模板。
- **按 GitHub 官方口径**：README、LICENSE、CODE_OF_CONDUCT、CONTRIBUTING、SECURITY、Issue/PR 模板逐项核对内容；community profile 的健康百分比只看文件在不在，不以它为目标。
- **能跑比文件齐更重要**：在干净环境里验证安装、最小示例、测试和打包。
- **不带走作者的电脑**：交付物里不能出现作者的用户名、本地路径、代理端口、"在我电脑上实测"式的环境快照、真实邮箱和凭据。
- **授权逐级给**：改文件、对外发布、对外推广各自单独确认，前一步的同意不延伸到后一步。

## 三道确认闸

| 闸 | 时机 | 给用户看什么 |
|---|---|---|
| 闸 1：改文件前 | Step 1 扫描后 | 定位卡、项目类型、缺失/薄弱/风险清单、打算新建和修改的文件 |
| 闸 2：对外发布前 | Step 3–4 完成后 | 事实卡（见文末）、diff 摘要、仓库名、可见性、Description、Topics、版本号 |
| 闸 3：对外推广前 | Release 之后 | Launch Kit 文案与渠道清单 |

闸与闸之间不再逐步询问；遇到 P0 失败或超出已确认范围的改动时，立即停下来问。

## 运行模式与认证

整理、隐私扫描、README 与社区文件生成、源码 ZIP 打包都不需要 GitHub 认证。只有用户明确要求"现在发布到 GitHub"时才做认证检查：

1. 先做**只读探测**：连接器能否完成一次真实操作、`gh` 是否存在并已登录、`github.com` 与 `api.github.com` 是否可达、`GITHUB_TOKEN` 是否存在（只判断有无）。
2. 按 `references/mcp-push-guide.md` 的判定表选路径 A（REST API + 一次性凭据推送）、B（连接器或 `gh`）或 C（交付 ZIP 与网页上传说明）。
3. 不扫描用户主目录、编辑器或 MCP 配置找 token；token 不进 URL、不落盘、不回显；需要代理时向用户要地址，不猜端口。

## 工作流程

```
Step 0 定位 → Step 1 扫描 →【闸 1】→ Step 2 整理 → Step 3 验证 → Step 4 门面
→【闸 2】→ Step 5 推送 → Step 6 Release 与分发 →【闸 3】→ Step 7 推广
```

### Step 0：定位

用现有资料回答四个问题，输出一张定位卡（目标用户、核心承诺、最小示例、证据、非目标）：

1. **谁会用**：首要用户一类，次要用户最多两类。
2. **解决什么**：在什么场景下，原来多麻烦，现在少几步。
3. **五分钟证明**：新用户能复现的最小示例和预期输出。
4. **本次边界**：区分准备开源、发布 GitHub、创建 Release、对外推广。

详见 `references/discovery-and-promotion.md`。

### Step 1：扫描

1. **判定类型**：按 `references/category-map.md` §3 执行（指纹 → 候选集 → 主产物一问 → 旗标 → 生命周期），产出**一个** `category_id`；落不进就记 `general` + `router=unresolved`，不硬套。
2. **核对社区健康文件**：README、LICENSE、CODE_OF_CONDUCT、CONTRIBUTING、SECURITY（根目录、`.github/` 或 `docs/`），Issue 表单与 PR 模板（`.github/`）。`LICENSE` 不能由组织级 `.github` 仓库兜底；Description 与 Topics 不是文件，但发布时必须设置。
3. **跑一次基线扫描**：`python scripts/validate_repo.py <项目目录> --strict --history`，记下 P0/P1 命中。

### Step 2：整理

- README 按类型取模板：先读 `references/readme-template.md`（总纲与《品类增量》），再只打开 `references/readme-templates/` 下对应的那一份骨架。
- 已有文件按"准确、清楚、可运行、可维护"评估，只在确有收益时改，并给出摘要或 diff；不为统一模板抹掉项目原有表达。
- 中文项目可全中文，建议保留英文摘要。

| 文件 | 要点 |
|---|---|
| README.md | 一句话价值、结果图或真实输出、最短安装、最小示例 |
| LICENSE | 按 `category-map.md` 的许可默认选择；内容、数据、模型不要默认 MIT |
| CODE_OF_CONDUCT.md | Contributor Covenant 3.0，附版本 URL |
| CONTRIBUTING.md | 贡献流程、分支规范、PR 要求 |
| SECURITY.md | 私有漏洞报告渠道、响应时间、支持版本 |

模板与 CI 样例见 `references/community-templates.md`。

### Step 3：验证

**P0（任一失败即阻止公开发布）**：秘密或个人信息进入当前树或历史；代码、素材、数据的分发权不明；干净 clone 无法按 README 跑通。

- [ ] `validate_repo.py --strict --history` 无 P0；P1 逐条处理或在事实卡里写明豁免理由
- [ ] 无真实 Key/Token、真实邮箱、手机号、证件号、含真实用户名的路径、私网 IP、代理端口和本机环境描述；占位符（`<your-token>`、`example@example.com`）不算泄露
- [ ] 历史提交里有泄露时：先在平台轮换吊销凭据，再经用户同意重写历史
- [ ] 第三方依赖、NOTICE、字体与素材署名完整
- [ ] 从干净目录按 README 完成安装、最小示例、测试和构建；未测试的平台写"未验证"
- [ ] 无残留占位符（`{owner}`、`{repo}`），相对链接与锚点有效，下载链接分支与默认分支一致，README 小于 512 KB

验证方法与门禁见 `references/pr-and-release-workflow.md`，扫描范围与盲区见 `references/privacy-scan.md`。

### Step 4：仓库门面

- Description：120 字符以内，`功能 + 亮点`，不写"一个用于…的项目"、不写版本号。规则与案例见 `references/description-guide.md`。
- Topics：5–10 个目标用户真会搜的成熟词。
- 社交预览图 1280×640，展示用途或结果。
- README 首屏："一句话价值 + 结果图/GIF + 最短安装 + 最小示例"。

### Step 5：推送

- 默认 `public-safe`：从最新默认分支开短分支 → 修改并验证 → Draft PR → 人复核 → CI 通过后 Squash Merge。
- 单人维护、改动低风险且用户明确同意时，可用 `solo-fast` 直推。决策表见 `references/pr-and-release-workflow.md`。
- **元数据是必做项**：推送后实际设置 Description 和 Topics，并从 GitHub 回读核对；做不到就标 `待手动设置`，给出精确值和网页路径。
- 发布后至少回读：仓库 URL、可见性、默认分支、Description、Topics、文件树、最新 CI 状态。

### Step 6：Release 与分发

- 按 SemVer 定版本号，按 Keep a Changelog 写说明；规范见 `references/pr-and-release-workflow.md` 的「Release 规范」。
- 只推 tag 不算发版，必须创建 Release 对象。
- 按类型选分发渠道（`uv publish`、`npm publish`、Hugging Face、Chrome Web Store、Release 资产），见 `references/release-and-distribution.md`。
- 核对版本号、CHANGELOG、Badge、Tag、Release 标题与安装链接一致。
- 纯文档或方法论项目只做 GitHub Release。

### Step 7：推广

- 按 `references/discovery-and-promotion.md#launch-kit` 的 5 件套，从**同一张事实卡**逐渠道改写，不复用同一条广告文案。
- 只选目标用户真实存在的 2–3 个首发渠道，遵守各社区的自我推广规则。

| 目标用户 | 优先渠道 | 内容重点 |
|---|---|---|
| 开发者 / Agent 用户 | GitHub Topics、技术社区、Show HN | 可运行演示、架构、限制、贡献入口 |
| 中文开发者 | 掘金、V2EX、知乎、公众号 | 使用场景、教程、真实效果和源码链接 |
| 创作者 / 非技术用户 | B 站、小红书、Product Hunt | 前后对比、操作视频、模板和上手成本 |

- 节奏按 T-7 → T0 → T+7 → T+30；早期以"三位陌生用户跑通"为成功标准，不用 Star 数代替真实采用。

## Reference Map

- 🗺️ [分类主表与判定路由](references/category-map.md)：唯一分类源，主表、旗标、判定算法、路由回归用例（约 9.7 KB）
- 📑 [README 模板总纲](references/readme-template.md)：前置事实清单、通用底座 12 节、Badge、安装表格、《品类增量》（约 12.4 KB）；各品类骨架在 `references/readme-templates/`，每份 2–5 KB，只读对应那一份
- 🚨 [避坑库与官方规范基线](references/github-oss-prep-pitfalls.md)：社区健康文件口径、历史凭据清理、CI 供应链（约 17.2 KB）
- 🛡️ [隐私与安全扫描](references/privacy-scan.md)：五重扫描的自动化范围与盲区；规则唯一真相源是 `scripts/secret-rules.json`（约 8.5 KB）
- 🏛️ [社区健康文件与 CI 模板](references/community-templates.md)：Issue 表单、SHA 锁定的 CI、Dependabot（约 9.8 KB）
- 🚀 [分发与发版指南](references/release-and-distribution.md)：uv、npm、Hugging Face、Chrome Web Store、Docker 与 Checksums（约 7.8 KB）
- 🏷️ [Description 与 Topics 指南](references/description-guide.md)（约 4.7 KB）
- 🌐 [发现与推广策略](references/discovery-and-promotion.md)：Launch Kit、社交预览、渠道（约 2.5 KB）
- 🔐 [GitHub 推送指引](references/mcp-push-guide.md)：只读探测 → 路径 A/B/C；token 不进 URL、不落盘（约 5.7 KB）
- 🚦 [PR、CI 与发布门禁](references/pr-and-release-workflow.md)：分支、PR、门禁、Release 规范（约 3.1 KB）
- 🔑 [GitHub 凭据方案对比](references/github-pat-comparison.md)：Fine-grained 与 Classic PAT（约 2.5 KB）
- 🔒 [认证与凭据最小化](references/github-pat-setup.md)：只读探测、一次性凭据、PAT 选择（约 2.7 KB）

## 交付：开源就绪事实卡

在 Step 3 验证完成后、闸 2 时提交。**每个测量值必须来自当次命令的真实输出**；没跑的项写 `未测量`、判定 `⚪ 未测量`，并视为阻断项。不得照抄示例数字。

| 层级 | 检查项 | 测量值 | 命令（附执行时间） | 判定 |
|---|---|---|---|:---:|
| L1 隐私安全 | 当前树 P0 / P1 命中数 | {P0} / {P1} | `python scripts/validate_repo.py <dir> --strict`（{RUN_AT}） | {VERDICT} |
| L1 隐私安全 | 历史提交与提交邮箱 | {HISTORY} | `python scripts/validate_repo.py <dir> --history`；可加 `gitleaks git`（{RUN_AT}） | {VERDICT} |
| L2 社区健康 | 健康文件与 Issue/PR 模板 | {FILES} | `validate_repo.py` 文件清单（{RUN_AT}） | {VERDICT} |
| L3 供应链 | workflow 顶层 permissions 与 Action SHA 锁定 | {CI_PIN} | `validate_repo.py` 规则 `ci-pin-*`（{RUN_AT}） | {VERDICT} |
| L3 自动化 | 项目自带测试 / 本技能 selftest | {TESTS} | 项目测试命令或 `python scripts/selftest.py`（{RUN_AT}） | {VERDICT} |

判定取值：`🟢 通过` / `🟡 部分` / `🔴 失败` / `⚪ 未测量`。豁免项（`scan-ignore`）单列一行写理由。

---

> 🌏 English: see `README.en.md`.
