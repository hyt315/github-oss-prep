# 十大全景开源项目品类专属 README 完整模板库

> 本文档提供 **10 份可直接复制填空的 README 骨架** + **1 份通用底座** + **逐空判据**。
> **先分类再取模板**：`category_id` 由 `references/category-map.md` §3 的判定算法产出；"品类 N"骨架与主表的对应关系见下方目录与文末《品类增量》。
> 渐进式披露：只读本总纲 + 你那一类的骨架文件，不要通读、也不要跨类拼接。
> 填空约定：`<!-- 判据：… -->` 是"怎样算写好"，`<!-- 反例：… -->` 是常见写坏的样子，`<!-- 可删：… -->` 表示该节在此场景可以整节删掉。三类注释在 GitHub 上渲染时不可见，可放心留在交付物里（也建议作者在写完后删净）。

---

## 目录导航（渐进式披露索引）

本文件是总纲：前置事实清单、通用底座 12 节、Badge 速查、安装表格与《品类增量》。**各品类骨架已拆成独立文件**，判定出 `category_id` 后只打开对应那一份：

| 品类 | 骨架文件 | 对应 `category_id` |
|---|---|---|
| 品类 1：AI Agent 技能型 | [01-skill.md](readme-templates/01-skill.md) | `skill` |
| 品类 2：MCP Server | [02-mcp-server.md](readme-templates/02-mcp-server.md) | `mcp-server` |
| 品类 3：模型权重与数据集 | [03-model.md](readme-templates/03-model.md) | `model`（`dataset` 只借用其结构，见《品类增量》） |
| 品类 4：CLI / 系统工具 | [04-cli.md](readme-templates/04-cli.md) | `cli` |
| 品类 5：类库 / SDK | [05-library.md](readme-templates/05-library.md) | `library` |
| 品类 6：IaC（仅 Terraform 骨架） | [06-iac.md](readme-templates/06-iac.md) | `iac` |
| 品类 7：前端与多媒体生成型 | [07-frontend-media.md](readme-templates/07-frontend-media.md) | `app` 的前端子型（以 `category-map.md` 判定为准） |
| 品类 8：浏览器扩展 | [08-extension.md](readme-templates/08-extension.md) | `extension` |
| 品类 9：完整应用 / Web 服务 | [09-app.md](readme-templates/09-app.md) | `app` |
| 品类 10：知识库 / Awesome 清单 | [10-content.md](readme-templates/10-content.md) | `content` |

本文件内的小节：

- [写之前先备齐：前置事实清单](#写之前先备齐前置事实清单)
- [通用底座：12 节与判据](#通用底座12-节与判据)
- [动态 Badge 速查矩阵](#动态-badge-速查矩阵)
- [多平台现代终端下载与安装表格集合](#多平台现代终端下载与安装表格集合)
- [品类增量：`category_id` → 模板 → 必写清单](#品类增量category_id--模板--必写清单)

---

## 写之前先备齐：前置事实清单

**没有这 5 样就不要开始写 README**（缺哪样先补哪样，或用 `未验证` 如实标注）：

| # | 必须有 | 为什么 |
|---|---|---|
| 1 | **一条能跑通的命令**（从空目录开始跑通，不是"我记得能跑"） | 首屏唯一硬通货；跑不通的 README 比没有 README 更伤信任 |
| 2 | **一段真实输出**（复制粘贴，不要手写"看起来像"的输出） | 让读者知道"成功长什么样"，也是你自测的证据 |
| 3 | **一张真实结果图**（截图/照片，非设计稿；必须有 alt 文本） | 15 秒内让人理解产物形态 |
| 4 | **一个失败案例 + 处置方法** | 决定陌生人来不来开第二现场；排障表比特性表更有说服力 |
| 5 | **支持范围声明**（测过哪些平台/版本，没测的写"未验证"） | 避免"应该能在 Linux 上跑"这类隐性谎言 |

## 通用底座：12 节与判据

所有品类共用。**硬性只有 3 节**（★），其余按项目取用；不设字数与章节数量要求——只查"内容是否真存在"。

| 节 | 判据（怎样算写好） | 硬性 |
|---|---|:--:|
| 1 首屏 | 一句话价值 + 1 张带 alt 的结果图 + 1 条复制即运行命令，三者都在渲染首屏内 | ★ |
| 2 这是什么/为什么 | ≤3 段，含"原来多麻烦 / 现在少几步"对比，禁止形容词堆叠 | |
| 3 安装 | ≥2 条路径（推荐 + 离线或手动），每条给**成功判据** | |
| 4 快速开始 | 最小示例 + **真实输出代码块**；输入数据来源写清 | ★ |
| 5 能力/用法表 | 每行给"命令或 API 签名"，不给空泛特性名 | |
| 6 工作原理 | ≥1 张图（Mermaid/SVG/ASCII）+ alt；说明数据流或调用顺序 | |
| 7 配置与兼容性 | 配置表（名称/默认/必填/影响）+ 平台版本矩阵，未测显式写"未验证" | |
| 8 排障 | ≥3 条"现象 → 原因 → 处置"，至少覆盖安装失败、权限、网络三类 | ★ |
| 9 已知限制 | 明确写"不做什么"、性能/规模边界、数据与隐私注意 | |
| 10 项目结构 | 目录树 + 每个目录一行说明（monorepo 换成"分产物入口表"） | |
| 11 贡献·支持·引用 | 三行：怎么提 PR、卡住去哪问（Issue/Discussions/其它）、如何引用（`CITATION.cff`） | |
| 12 许可与致谢 | 许可**按资产类型**给 SPDX（代码/文档/图/字体/数据），第三方素材署名入口 | |


---

## 动态 Badge 速查矩阵

```markdown
<!-- License 徽章：许可文字与链接目标由 category-map 的"许可默认"列派生，不要写死 MIT；
     非代码资产（文档/图像/字体/数据）需在徽章或 §12 分许可表中体现 -->
[![License](https://img.shields.io/github/license/{owner}/{repo})](LICENSE)

<!-- 动态 Release 徽章（自动读取最新 Tag） -->
[![Release](https://img.shields.io/github/v/release/{owner}/{repo}?sort=semver)](https://github.com/{owner}/{repo}/releases)

<!-- 包管理器动态版本 (npm / PyPI / Crates) -->
[![npm version](https://img.shields.io/npm/v/{pkg-name}.svg)](https://www.npmjs.com/package/{pkg-name})
[![PyPI version](https://img.shields.io/pypi/v/{pkg-name}.svg)](https://pypi.org/project/{pkg-name}/)
[![Crates.io](https://img.shields.io/crates/v/{pkg-name}.svg)](https://crates.io/crates/{pkg-name})

<!-- CI 状态徽章 -->
[![CI Status](https://github.com/{owner}/{repo}/actions/workflows/ci.yml/badge.svg)](https://github.com/{owner}/{repo}/actions)

<!-- 平台支持徽章：链接指向"兼容性"章节锚点，不要指向项目里未必存在的 SKILL.md -->
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](#兼容性)
<!-- Stars 徽章：新仓库冷启动无信号量，建议省略；要用就放正文末尾，别占首屏 -->
```

---

## 多平台现代终端下载与安装表格集合

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
| **`Homebrew`** | `brew install {owner}/tap/{package}` | macOS / Linux 软件包管理 |
| **`Winget`** | `winget install {owner}.{package}` | Windows 官方应用管理 |
| **`Scoop`** | `scoop install <package>` | Windows 开发者工具管理 |
| **`一键脚本 (Unix)`** | `curl -fsSL https://.../install.sh -o install.sh && less install.sh && sh install.sh` | Linux / macOS：先下载、看过再运行 |
| **`一键脚本 (Win)`** | `irm https://.../install.ps1 -OutFile install.ps1`，看过后 `powershell -ExecutionPolicy Bypass -File .\install.ps1` | Windows：先下载、看过再运行 |
```

---

## 品类增量：`category_id` → 模板 → 必写清单

> 与 `references/category-map.md` §2 的"模板"列一一对应；本表是**必写增量的权威版**（category-map 指向这里）。
> "模板"列含义：`骨架`＝`readme-templates/` 下已有可直接复制的骨架；`增量`＝没有专属骨架，请用《通用底座 12 节》+ 本表增量清单。

| `category_id` | 模板 | 该类**额外必写**（底座之外） | 常见写坏的样子 |
|---|---|---|---|
| `skill` | 骨架·品类 1 | ①≥3 条真实触发语；②frontmatter 契约（`name`/`description`/版本）；③副作用与权限边界；④宿主支持矩阵；⑤卸载方式 | 只写"能帮你做 X"，不写触发方式与副作用，用户不知道怎么让它干活 |
| `mcp-server` | 骨架·品类 2 | ①安装（免装运行命令 + 成功判据）；②传输方式与鉴权（stdio/HTTP、凭据来源）；③每个 tool 的错误语义与副作用；④≥2 家客户端配置；⑤Inspector 调试路径 | 只贴一段 JSON 配置，不写错误返回，调用方不敢重试 |
| `model` | 骨架·品类 3 | ①每条跑分配复现命令与环境（harness/commit/seed/硬件）；②量化-显存-吞吐矩阵；③许可链与商用/出口限制；④不适用场景与已知偏差；⑤单文件下载与 LFS 说明 | 放一张漂亮但无法复现的排行榜 |
| `dataset` | 增量 | ①来源与采集方法（含授权依据）；②再分发许可与分许可表；③去标识与撤回机制；④schema 字典 + 一行真实样例；⑤切分方式与版本化（DVC/hash）；⑥偏倚声明 | 只给字段列表，不写数据从哪来、能不能用 |
| `library` | 骨架·品类 5 | ①错误类型与重试语义表；②最低语言/运行时版本；③体积与依赖数（tree-shaking 说明）；④API 文档入口；⑤0.x→1.0 稳定性承诺 | 示例没有返回值，异常全靠读者猜 |
| `cli` | 骨架·品类 4 | ①一段真实终端输出；②退出码与 `--json` 机器可读约定；③CI/非交互模式与颜色开关；④补全安装；⑤配置优先级；⑥安装方式**选择规则** | 罗列 uvx/npx/winget 五种装法却不告诉谁该选哪个 |
| `app` | 骨架·品类 9 | ①架构与依赖服务图；②迁移·回滚·备份三条命令；③`.env` 每项变量的获取方式；④健康检查判据；⑤最低资源与扩展性限制；⑥演示环境（可用只读账号） | 只给 `docker run`，不给 DB 迁移与回滚路径 |
| `extension` | 骨架·品类 8 | ①权限逐项用途 + "数据是否离开本机"列；②宿主×版本兼容矩阵（未测写未验证）；③更新渠道；④开发者模式加载的安全提示；⑤站点/宿主改版失效的排障入口 | 写"我们重视隐私"但没有逐项权限表 |
| `iac` | 骨架·品类 6（仅 Terraform） | ①provider/模块版本约束；②`plan` 输出样例与破坏性变更说明；③state 假设与并发；④成本量级提示；⑤Helm 子型另需 values 契约 + `--atomic` 回滚 | 用一份"基础设施"模板糊住三种完全不同的产物 |
| `env-config` | 增量 | ①密钥绝不入库（`.env`、`.env.*` 进 .gitignore，只提交 `.env.example`）；②机器绑定与 bootstrap 流程；③失败时手动步骤；④声明"这不是可分发软件" | 长得像软件仓库却没有安装/使用语义 |
| `ci-automation` | 增量 | ①`uses:` 完整调用示例（含全部 `with` 参数）；②所需 secrets 与 `permissions`；③major tag 滚动 vs SHA 锁定策略；④runner 矩阵与 self-hosted 信任边界；⑤可观测（日志摘要/PR 注释） | 只给 action 名，用户不知道要传哪些 secrets |
| `content` | 骨架·品类 10 | ①导航与小节一一对应（无栏目就删目录项）；②**本项目自定**收录准则；③内容许可（CC-BY/CC0，勿用 MIT）；④勘误与更新政策 | 把某清单的私人准则写成"行业通用标准" |
| `general` | 底座 12 节 | 在事实卡标注 `category_id=general`、`router=unresolved`，并把该形态回写 `category-map.md` §6 候选池 | 硬套最像的一类，产出不合身骨架 |

### 骨架缺位的处理（诚实优先）

`dataset`、`env-config`、`ci-automation` **目前没有专属骨架**。此时按底座 12 节 + 本表增量写，并在交付事实卡里写 `template=missing`——**不要**拿别的品类模板拼接冒充专属模板。补齐专属骨架后可在本表把"增量"改为"骨架"。
