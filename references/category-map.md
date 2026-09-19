# 分类主表与判定路由（唯一分类源）

> **本文件是本项目唯一的分类系统。** 扫描（Step 1）、README 模板选择（Step 4）、分发渠道（Step 6）、许可默认（Step 2）都引用同一 `category_id`。
> 背景：技能内曾并存三套互不映射的分类（4 类 / 9 类 / 10 类）。现已合并——`SKILL.md` 只保留指向本文件的判定动作。

---

## 1. 三轴 + 旗标（先定位，再选类）

| 轴 | 取值 | 决定什么 |
|---|---|---|
| **轴 1 产物形态** | 下表 12 个 `category_id`（**唯一主类**） | 安装/验证方式、专属章节、分发渠道、许可默认 |
| **轴 2 首要受众** | `dev`（写代码的人）/ `platform`（运维·平台工程）/ `creator`（非技术·创作者）/ `research`（研究者）/ `enterprise`（采购·合规） | 术语密度、是否必须图形化演示、是否要合规与审计段落 |
| **轴 3 生命周期** | `incubating`(<1.0) / `ga` / `maintenance` / **`archived`** | 稳定性承诺、是否接受贡献、**归档态必须写状态横幅与替代品**（`0.x` 不得承诺兼容） |

**旗标（可多选，逐个开关一段必写内容）**：

| 旗标 | 触发即必写 |
|---|---|
| `monorepo` | 分产物入口表 + 各产物版本策略 |
| `binary` | 平台矩阵 + 校验和 + 签名/公证说明 |
| `network-surface` | SECURITY 范围 + 默认端口与鉴权说明 + 反向代理注意 |
| `user-data` | 数据流向图 + 本地/上传边界 + 撤回机制 |
| `ai-generated` | AI 生成内容声明 + 人工复核范围 |
| `non-code-assets` | 分许可表（字体/图像/数据/硬件各有专用许可）+ NOTICE/素材署名 |
| `paid-deps` | 免费额度、必需密钥来源、无密钥时的降级路径 |

---

## 2. 主表：12 类

「进入判据」是**候选生成**（命中≠确定），最终由 §3 的主产物问题确认。

| `category_id` | 名称 | 进入判据（硬信号） | 歧义消解 | 分发渠道 | 许可默认 | 模板 |
|---|---|---|---|---|---|---|
| `skill` | AI Agent 技能 | 存在 `SKILL.md` 且含 `name`/`description` frontmatter | 若进程被 MCP 客户端连接 → `mcp-server`；若只是文档+脚本包 → `skill` | `gh skill publish`（Public Preview）、仓库自装、Release ZIP | MIT 或 Apache-2.0（含提示词/数据集资产时分许可） | 品类 1 |
| `mcp-server` | MCP 服务端 | 依赖含 `@modelcontextprotocol/sdk` / `mcp[cli]`；有 `.mcpb`/MCP manifest | 与 `skill` 的区别：对外暴露 tools/resources 的**进程** | npm/PyPI（`npx -y`/`uvx`）、Registry 目录 | Apache-2.0（企业集成侧）优先 | 品类 2 |
| `model` | 模型权重 / 量化包 | `*.safetensors`/`*.gguf` + `config.json`/tokenizer，或 `Modelfile` | 权重为主 → `model`；结构化记录为主 → `dataset` | HF Hub、Ollama/ModelScope、Release 资产 | **跟随基础模型许可链**（厂商许可可能非 OSI）；不得默认 MIT | 品类 3 |
| `dataset` | 数据集 | 数据文件为主（`parquet`/`csv`/图像目录）+ dataset card / DVC | 与 `model` 分离：本类必写来源、去标识、schema、切分 | HF datasets、Kaggle、Zenodo、Release 资产 | CC-BY-4.0 / CDLA-Permissive-2.0 / ODbL（按再分发权决定） | 品类 3 的**数据集增量**（正文缺，见 `13`） |
| `library` | 类库 / SDK | 被 import：`package.json` 有 `main`/`exports` 无 `bin`；`pyproject` 无 `[project.scripts]`；`Cargo.toml` 有 `[lib]` | 若同时提供可执行命令 → 以「用户 5 分钟内跑什么」定主类，另一记为次产物 | npm / PyPI / crates.io / Maven Central（**Portal token 流程**）/ NuGet / Go proxy | 宽松（MIT/Apache-2.0）；重专利域选 Apache-2.0 | 品类 5 |
| `cli` | 命令行 / TUI 工具 | `package.json` 有 `bin`；`[project.scripts]`；`[[bin]]`；Cobra/argparse main | 若默认起 HTTP 服务 → `app`；若只是库的可选入口 → `library` | 包管理器（winget/brew/scoop/choco/AUR）、`uvx`/`npx`、Release 二进制 + 校验和 | MIT / Apache-2.0 | 品类 4 |
| `app` | 完整应用 / Web 服务 | 监听端口 + `Dockerfile`/`compose.yml` + `.env.example` | 前端构建产物为主的站点 → `frontend` | Docker/OCI、PaaS 一键部署、云市场 | Apache-2.0（SaaS 注意 AGPL 差异） | 品类 9（现最弱，见 `13`） |
| `extension` | 宿主插件（浏览器 / 编辑器 / 平台） | 浏览器：`manifest.json` 含 `manifest_version`；VS Code：`package.json` 有 `contributes`+`.vsixmanifest`；Obsidian：`manifest.json` 含 `id` | 子型 `browser`/`vscode`/`other-host` 决定商店与审核章节 | Chrome Web Store / Edge / VS Code Marketplace + Open VSX / Obsidian | MIT（权限与隐私声明必写） | 品类 8 |
| `iac` | 基础设施模块 / Chart | `*.tf`+`variables.tf`/`outputs.tf`；或 `Chart.yaml`；或 `kustomization.yaml`/CFN 模板 | **个人环境配置不属本类** → `env-config` | Terraform Registry、Helm repo 或 OCI chart、CloudFormation 公共段 | Apache-2.0（含云厂商示例素材时分许可） | 品类 6（当前正文只有 Terraform，见 `13`） |
| `env-config` | dotfiles / devcontainer / 开发机模板 | `Brewfile`、`.bashrc`/`.zshrc` 集、`stow` 目录、`.devcontainer/`、`.files.zsh` | 无「安装即运行」语义：README 须声明"这不是可分发软件" | 无（仅仓库 + 引导脚本） | MIT 或 CC0（**密钥旗标强制为真**） | 品类 6 的 **dotfiles 增量**（正文缺） |
| `ci-automation` | CI/CD 与工程构件 | `action.yml`；`.pre-commit-hooks.yaml`；可复用 workflow；CI orb/模板 | 若同时是 CLI → 主类看"用户调用方式"（在流水线里被调用 → 本类） | GitHub Marketplace、Gitlab 模板、PyPI/npm（action 的 CLI 伴生包） | MIT + **完整 SHA 锁定文档**、major tag 滚动策略 | 无（用 `general` 底座 + §4 增量） |
| `content` | 文档 / 课程 / 清单 | 纯 Markdown 为主，无构建产物；`SUMMARY.md`/课程大纲/收录准则 | 若代码示例可运行 → 主类仍看"用户跑什么"；否则 `content` | GitHub Pages、文档站、awesome 列表 PR | **CC-BY-4.0 / CC0（勿用 MIT 覆盖内容）** | 品类 10 |
| `general` | 兜底类 | 无法归入以上 12 类 | **禁止硬套最像的一类**：产出 `category_id=general` + `router=unresolved`，并把形态回写本表候选池 | 按实际产物 | 代码宽松 + 素材按类型分许可 | 底座 12 节 + 最相近 2 类增量 |

---

## 3. 主产物判定（写进 `SKILL.md` Step 1 的动作）

```
第 1 步 指纹扫描 → 候选集（可为多类）
第 2 步 问一句硬判据："新用户拿到这个仓库，5 分钟内会执行/打开的那一个东西是什么？"
        → 让 Agent 自答并给出它打算写进 README 的那条命令；答案对应的主类即选定
第 3 步 若还有第二、三个可交付物 → 主类不变 + 打 monorepo 旗标 + 写"分产物入口表"
第 4 步 生命周期：>24 个月无提交、或作者声明停止维护 → archived（强制状态横幅 + 替代品 + 无安全支持）
第 5 步 全部落不进 → category_id=general，事实卡标注 router=unresolved
```

**不允许**：跳过第 2 步直接用文件指纹定类；也不允许"两个都像"时抛给用户体验选择——先按第 2 步的判据定，再在事实卡里登记歧义。

---

## 4. 缺失模板的处理（诚实标注，不用通用套话冒充专属）

| `category_id` | 模板状态 | 现在怎么办 |
|---|---|---|
| `dataset` / `env-config` / `ci-automation` / `mobile`（未来） | 无专属骨架 | 用 `readme-base.md` 底座 12 节 + 本表"必写增量"列；并在事实卡写 `template=missing` |
| `app`（品类 9） | 有骨架但过弱（2 章节） | 按 `13` 的重写样例替换；未替换前标注 `template=weak` |
| `iac` / `content` 等 | 完整 | 直接用 |

**各 `category_id` 的必写增量（3–6 条）** 见 `readme-template.md` 的《品类增量》一节；两者不一致时**以本表为准**。

---

## 5. 路由回归用例（`tests/test_category_router.py` 的期望）

```
{"SKILL.md + scripts/*.py"}                       → skill
{"package.json: @modelcontextprotocol/sdk"}       → mcp-server
{"model-q4_k_m.gguf + config.json + Modelfile"}   → model
{"train.parquet + dataset_card/ + dvc.yaml"}      → dataset
{"package.json main/exports, no bin"}             → library
{"pyproject [project.scripts] + README 安装"}     → cli
{"Dockerfile + compose.yml + .env.example"}        → app
{"manifest.json manifest_version:3"}               → extension(browser)
{"package.json contributes + .vsixmanifest"}       → extension(vscode)
{"main.tf + variables.tf + outputs.tf"}            → iac
{"Chart.yaml + templates/ + values.yaml"}          → iac（Helm 子型，走增量）
{"Brewfile + .zshrc + stow/"}                      → env-config（user-data 旗标自动=真）
{"action.yml + workflows/"}                        → ci-automation
{"仅 *.md，无代码"}                                 → content
{"pnpm-workspace.yaml + packages/*"}               → 主产物定类 + monorepo=true
{"无任何信号（如只有 LICENSE）"}                    → general + router=unresolved
```

---

## 6. 扩表与命令时效规则

- **本表 12 类是"当前可判定集"，不是终局**。扩表唯一依据是**真实误判记录**（某项目落不进或落错），不是"感觉还缺几类"。候选池：桌面 App、移动 App、研究复现、字体/素材、硬件、游戏、提示词与评测集、数据管道、前端站点与组件库分离。
- 表内**一切命令与版本**遵循同一铁律：①标适用版本或日期 ②给核对方式（`--help`、`gh api …/releases/latest`、`endoflife.date/…`）③滚动声明。
- 许可默认列若与 `LICENSE` 实际选择冲突，**以仓库实际 LICENSE 为准并在本表登记差异**（不得为了对齐而改用户项目的许可）。
