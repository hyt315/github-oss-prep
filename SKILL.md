---
name: github-oss-prep
description: Use when preparing, publishing, launching, or improving any project for open-source adoption on GitHub. Features 10 Universal Archetype README engines (AI Skill, MCP Server, AI Model/GGUF, CLI tool, Multimedia, SDK, Browser Extension, IaC/Dotfiles, Fullstack App, Awesome List), progressive disclosure architecture, all-ecosystem distribution (uv, npm, HuggingFace, Chrome Store), 5-layer deep security scanning, YAML Issue Forms, CI/Dependabot templates, and approval-gated publishing. Triggers include GitHub 开源准备, 准备发布到 GitHub, 美化项目准备开源, 开源化, 开源推广, oss prep, publish to GitHub, launch an open-source project, and prepare for open source.
metadata:
  author: hyt315
---

# GitHub 开源准备

将任意项目美化为适合 GitHub 发布的专业级开源版本，补齐全套 100% 社区健康文件与 CI 自动化，构建专属针对性门面与现代全渠道分发。

## 核心理念与铁律

- **先审后改，不盲目覆盖**：保留有效内容；已有文件若过时、残缺或存在风险，先展示差异与理由，获批后再修改。
- **渐进式披露铁律（Progressive Disclosure）**：门面生成时，必须严格根据品类识别结果定向调阅对应品类的专属章节，严禁通读全库或产生跨品类交叉污染。
- **十大全景品类精准适配**：对 AI Skill、MCP Server、AI 模型/数据集、CLI 工具、前端多媒体、SDK、浏览器扩展、基础设施 IaC、全栈应用、Awesome 清单提供 100% 匹配的开箱即用门面。
- **对齐 GitHub 2026 官方社区标准**：通过 Insights → Community 100% 考核（全量采用交互式 YAML Issue Forms 与 CI 模板）。
- **五重严密环境与隐私扫描**：深度拦截敏感凭据、私有路径指纹、内部会话标记、Git URL 凭据污染与构建缓存。
- **全生态现代分发矩阵**：支持 `gh skill`、`uvx`/`uv tool`、`npx`/`bunx`、Hugging Face、Chrome Web Store、`cargo binstall`、`brew`、`winget` 与 Release Checksums。
- **分阶段授权与确认发布**：本地整理、远程推送、Release 打包与外部推广分别独立授权，严禁越权。
- **纯 Python 标准库零依赖**：所有辅助脚本（validate_repo.py、selftest.py 等）严格基于 Python 3.10+ 原生标准库，100% 零依赖、纯只读。

---

## 运行模式与前置条件

开源整理、隐私扫描、README 与社区文件生成、源码 ZIP 打包均不需要 GitHub 认证。只有用户明确要求“发布到 GitHub”时才进入认证检查：

1. **Prepare only（默认）**：完成本地开源整理，输出可审查目录与 ZIP，无需任何 GitHub 凭据。
2. **GitHub connector**：用户明确授权且当前平台已有官方连接器时使用。
3. **GitHub CLI**：使用系统已登录的 `gh` CLI 工具发布。
4. **Manual handoff**：交付完整目录、ZIP、仓库 Description 与 Topics，附带网页上传指引。

---

## 工作流程

```
Step 0: 十大全景品类精准识别 (AI Skill / MCP / 模型 / CLI / 多媒体 / SDK / 扩展 / IaC / 应用 / 清单)
    ↓
Step 1: 五重深度安全扫描 (凭据 + 私有路径 + 会话标记 + Git 污染 + 构建产物)
    ↓
Step 2: 社区文件与 CI 补全 (YAML Issue Forms + PR 模板 + SECURITY + CI/Dependabot)
    ↓
Step 3: 渐进式门面生成 (遵循渐进式披露，定向调阅专属品类模板与动态徽章)
    ↓
Step 4: 现代分发渠道精准适配 (uvx / bunx / HuggingFace / Chrome Store / brew / gh skill)
    ↓
Step 5: 干净环境回归自测 (scripts/selftest.py + 规范审计 100% 通过)
    ↓
Step 6: 发布确认 → 远程推送、创建 Release 与全渠道分发
```

---

## 工作流各阶段要点

### Step 0: 十大全景品类精准识别
- 确定项目属于哪一类，并精准锁定分发与门面规范：
  - **AI Agent 技能**：一句话 Agent 自装 / `gh skill install` / skills 目录克隆；
  - **MCP Server 协议端**：`claude_desktop_config.json` / Tools & Resources 表 / stdio 模式；
  - **AI 模型与数据集**：Hugging Face / Ollama / 显存矩阵 (VRAM) / Benchmark 跑分；
  - **系统与 CLI 工具**：`uvx` (免装) / `uv tool install` / `npx` / `bunx` / `brew`；
  - **前端与多媒体生成**：视觉动图 Gallery / 16:9 与 9:16 画布矩阵；
  - **类库与核心 SDK**：5 行极简极速 Hello World / API 参数表 / 包管理器表；
  - **浏览器扩展与插件**：Chrome 商店直达 / 离线加载步骤 / Manifest V3 权限表；
  - **基础设施与配置 (IaC)**：一键初始化 / 架构拓扑图 / `values.yaml` 参数表；
  - **完整应用与 Web 服务**：Live Demo / 1 键部署 / Docker / `.env.example` 表；
  - **知识库与 Awesome 清单**：Awesome 徽章 / 树状索引 / 收录评审准则。

### Step 1: 五重环境与隐私安全扫描
- 扫描全树代码、文档与 Git 配置。
- 严密拦截：API Keys、本地绝对路径、私有 Agent 会话 ID、`.git/config` 中的明文 URL Token、构建缓存残留。
- 详见 [隐私与环境安全扫描指南](references/privacy-scan.md)。

### Step 2: 100% 社区健康文件与 CI 补齐
- 生成 GitHub 2026 标准 YAML 格式 Issue Forms（`bug_report.yml`、`feature_request.yml`、`config.yml`）。
- 补齐 `CODE_OF_CONDUCT.md`、`CONTRIBUTING.md`、`SECURITY.md`、Node/Python 矩阵 CI、`dependabot.yml`、`.editorconfig` 与 `.gitattributes`。
- 详见 [社区健康文件库与模板](references/community-templates.md)。

### Step 3: 渐进式专属门面生成
- **严格遵循渐进式披露**：仅从 [十大品类 README 模板库](references/readme-template.md) 中调阅对应品类的专属锚点章节，渲染高质量中英文门面。

### Step 4: 现代分发渠道与发版实操
- 依据项目品类匹配对应的发版流程：`uv publish`、`npm publish`、`huggingface-cli upload`、Chrome Web Store 上架或 Release 资产。
- 详见 [全渠道分发与发版实操指南](references/release-and-distribution.md)。

### Step 5: 验证与发布门禁
- 运行 `python scripts/selftest.py` 与 `validate_repo.py` 进行全量回归。
- 详见 [PR、CI 与发布门禁工作流](references/pr-and-release-workflow.md)。

---

## Reference Map

- 需要为项目选择并生成专属风格 README 时，先读 [十大品类 README 模板库](references/readme-template.md)：涵盖 10 大项目形态完整开箱即用 Markdown 骨架与现代终端运行器表（预计阅读时间：4 分钟）。
- 需要执行隐私与环境安全扫描、拦截私有路径与凭据时，先读 [隐私与环境安全扫描指南](references/privacy-scan.md)：5 重扫描防御网、真伪泄露案例比对与脱敏规则（预计阅读时间：3 分钟）。
- 需要配置 GitHub 2026 社区文件、CI 矩阵与 Dependabot 时，先读 [社区健康文件库与模板](references/community-templates.md)：全量 YAML Issue Forms、CI 流水线与 Dependabot 配置（预计阅读时间：3 分钟）。
- 需要配置 uv/npm/HuggingFace/ChromeStore/Docker 多平台发版与 Release 校验和时，先读 [全渠道分发与发版实操指南](references/release-and-distribution.md)：涵盖全生态发版命令、配置文件与国内镜像源（预计阅读时间：4 分钟）。
- 需要撰写仓库 Description、Topics 与推广材料时，先读 [Description 与 Topics 优化指南](references/description-guide.md) 与 [开源发现与推广策略](references/discovery-and-promotion.md)（预计阅读时间：3 分钟）。
- 需要配置远程推送、MCP 或 GitHub PAT 权限时，先读 [GitHub MCP 与推送指南](references/mcp-push-guide.md)、[PAT 配置指南](references/github-pat-setup.md) 与 [PAT 类型对比](references/github-pat-comparison.md)（预计阅读时间：2 分钟）。
- 需要配置 PR、CI 自动化测试与发版门禁时，先读 [PR、CI 与发布门禁工作流](references/pr-and-release-workflow.md)（预计阅读时间：3 分钟）。
