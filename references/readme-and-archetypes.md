# README 写作原则、形态增量与门面规范

现代 AI 能直接读懂代码并写出自然的 README，**不需要套用僵硬的填空骨架**。按「必要项必做、锦上添花按需、按形态补关键信息」组织即可。

## 1. 必要项（默认必做）

写之前先确认项目里真的有一条在干净目录可跑通的命令和真实输出，绝不编造效果。

- **一句话价值**：首屏说清「谁在什么场景下用它，解决什么问题」，禁止空泛形容词堆砌。
- **直观效果**：1 张真实截图 / GIF / 终端真实输出块，让访客 15 秒内看懂产物形态。
- **最短安装与最小可跑示例**：优先展示免装或一行安装命令，附带从零到首次看到结果的最小示例。
- **开源协议**：明确标注 SPDX 许可并链接到 `LICENSE`（代码常用 MIT / Apache-2.0；纯文档/素材/数据用 CC-BY-4.0 / CC0；模型权重遵循上游基础模型许可链）。

## 2. 锦上添花项（按项目体量与受众按需添加）

小工具或早期原型保持精炼即可，不必为了凑章节硬写：

- **工作原理 / 架构图**：逻辑复杂时补一张 Mermaid 或 ASCII 流程说明。
- **配置与兼容性矩阵**：有环境变量或平台限制时列出，未测过的平台显式写「未验证」。
- **排障与已知限制**：记录 2–3 个真实常见报错与「本工具不做什么」。
- **双语文档**：中文项目面向国际用户时，拆成 `README.md` + `README.en.md` 并互链，避免中英混排。
- **徽章（Badges）**：只放有效动态徽章（License、Release、CI Status）；冷启动新仓库可省略 Stars 徽章。

## 3. 6 大项目形态 + 3 个风险开关

读完仓库目录后直接判定主形态，只补充该形态真正关键的差异信息：

### 形态 1：AI Agent Skill / MCP Server
- **Agent Skill 必含安装组合（按推荐顺位）**：
  1. **一句话发给 AI 自装（最省事）**：提供可直接复制的提示词，例如：
     > 请帮我安装 `{repo}` 技能：将 `https://github.com/{owner}/{repo}` 安装到你的 skills 目录并确认可用。
  2. **跨 Agent 标准 CLI（`npx skills`）**：单技能仓库用 `npx skills add {owner}/{repo}`（加 `-g` 为全局安装）；多技能仓库加 `--skill <name>`；锁版本用 `npx skills add {owner}/{repo}@v1.0.0`。
  3. **手动克隆**：给出 Claude Code (`~/.claude/skills/`)、Cursor (`~/.cursor/skills/`)、通用 Agents (`~/.agents/skills/`) 的 `git clone` 命令；若支持 `gh skill install` 可作为补充（注明 Public Preview）。
- **Agent Skill 额外要点**：给出 2–3 条自然触发语、权限/副作用边界（是否改文件、是否联网或推送）、卸载方式；确认 `SKILL.md` frontmatter 符合 [agentskills.io](https://agentskills.io/specification) 规范（仅使用 `name`、`description`、`license`、`allowed-tools`、`metadata`、`compatibility` 六个标准顶层字段）。
- **MCP Server 额外要点**：优先给出 `npx -y <pkg>` 或 `uvx <pkg>` 免装运行方式、传输模式（stdio / HTTP）与鉴权来源、至少 2 家客户端配置示例、各 tool 的副作用说明。

### 形态 2：CLI 工具与类库 / SDK
- **现代安装命令**：Python 优先 `uvx <pkg>` / `uv tool install <pkg>`，Node 优先 `npx` / `pnpm dlx` / `bunx`，Rust 优先 `cargo binstall`，编译二进制附 `brew` / `winget` / `scoop` 与校验和。
- **额外要点**：CLI 贴一段真实终端输出、退出码与非交互/JSON 模式说明；SDK 给带返回值的最小调用示例、最低运行时版本与错误语义。

### 形态 3：完整应用 / Web 服务 / 浏览器或编辑器插件
- **应用/服务**：启动命令（Docker Compose / 本地 dev）、`.env.example` 必填变量来源、数据库迁移与健康检查方式。
- **插件（Chrome / VS Code / Obsidian）**：商店安装入口 + 开发者模式加载提示、逐项权限用途及「数据是否离开本机」说明。

### 形态 4：AI 模型权重与数据集
- **模型**：优先给 `hf download` / `ollama run`（注意 `huggingface-cli` 已废弃，统一用 `hf`）、量化与显存需求、可复现的评测条件、上游基础模型许可链。
- **数据集**：数据来源与再分发授权、schema 字典与一行真实样例、去标识与撤回机制。

### 形态 5：纯文档 / 课程 / Awesome 清单 / 个人配置（dotfiles）
- **文档/清单**：明确收录标准与内容许可（CC-BY-4.0 / CC0，不用 MIT）；目录与实际小节严格对应。
- **个人配置（dotfiles / devcontainer）**：显式声明「非可分发软件」、密钥绝不入库、引导步骤与失败手动回退方式。

### 形态 6：其他（基础设施 IaC / GitHub Action / 混合项目）
- **IaC / Helm**：provider/chart 版本约束、`plan` 示例与破坏性变更提醒、成本量级提示。
- **GitHub Action**：完整 `uses:` 示例（推荐锁 40 位 SHA）、所需 `permissions` 与 `secrets`。

### 3 个横向风险开关（命中即必写）
- **涉及用户数据或对外监听端口**：写清数据流向（本地处理 vs 上传外部）、默认端口与鉴权、隐私与安全边界。
- **含非代码素材（字体/图片/音视频/数据集）**：补分许可说明与第三方署名来源。
- **Monorepo（多产物）**：在 README 顶部给一张分产物入口清单，说明各子包用途与路径。

## 4. 仓库门面（Description 与 Topics）

- **Description**：控制在 **120 字符以内**，结构为「核心功能 + 目标用户/亮点」（中文、英文或 `中文 | English`），不写版本号，不用「一个用于……的项目」开场。
- **Topics**：选 **5–10 个**全小写 kebab-case 成熟搜索词，覆盖功能、生态与技术栈（如 `agent-skill`、`open-source`、`github`、`python`）。
- **社交预览图**（可选）：1280×640，突出产品效果而非纯文字。
