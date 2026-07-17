---
name: github-oss-prep
version: 1.2.2
description: Use when preparing a project for open-source release on GitHub — covers license selection, community health files, README structure, privacy scanning, and repo push. Triggers: GitHub 开源准备、准备发布到 GitHub、美化项目准备开源、开源化、oss prep、publish to GitHub、prepare for open source.
---

# GitHub 开源准备

将任意项目美化为适合 GitHub 发布的版本，补齐全套社区健康文件，输出专业级仓库。

## 核心理念

- **只补缺，不覆盖**：已有文件不修改，只补充缺失项
- **按项目类型适配**：Skill 项目、代码项目、文档项目的侧重点不同
- **对齐 GitHub 社区配置文件标准**：目标是通过 Insights → Community 中 100% 的考核
- **确认后再推送**：生成内容后展示给用户确认，收到明确同意才创建仓库

---

## 前置条件

确认 GitHub 推送凭据可用。

**发现策略**（按优先级）：

1. **检查环境变量**：`GITHUB_TOKEN`、`GITHUB_PERSONAL_ACCESS_TOKEN`
2. **自动发现 MCP 配置**：在用户主目录下搜索包含 `github` MCP 服务器配置的 JSON 文件（各类 AI 编码工具都会在特定目录存放 MCP 配置）
3. **参考常见路径**（仅作兜底，不同工具路径可能不同）：
   - `~/.cursor/mcp.json`（Cursor）
   - `~/Library/Application Support/Claude/claude_desktop_config.json`（Claude Desktop macOS）
   - `%APPDATA%\Claude\claude_desktop_config.json`（Claude Desktop Windows）
   - `~/.codeium/mcp_config.json`（Windsurf）
   - `.vscode/mcp.json`（VS Code / GitHub Copilot，项目级配置）
   - `~/.trae/mcp.json`（Trae）

发现配置文件后，从中提取 `GITHUB_PERSONAL_ACCESS_TOKEN` 字段值。

Token 推荐使用 Classic PAT（`ghp_` 前缀），需要 `repo` 权限。如所有方式都找不到，引导用户参考 `references/github-pat-setup.md` 配置。Fine-grained PAT 与 Classic PAT 的差异详见 `references/github-pat-comparison.md`。

---

## 工作流程

```
Step 1: 扫描（识别类型 + 检查缺失文件）
    ↓
Step 2: 补齐（生成缺失的标准文件）
    ↓
Step 3: 审查（内容质量 + SKILL.md 合规）
    ↓
Step 4: 生成 Description（按规则 + 模板，详见 references/description-guide.md）
    ↓
Step 5: 推送确认 → 使用 Token → 创建仓库 + 推送（MCP 优先，curl+git 回退）
    ↓
Step 6: Release + 多平台分发（详见 references/release-and-distribution.md）
    ↓
Step 7: 发布后优化（仓库设置 + CI/CD + 推广）
```

---

## Step 1: 扫描项目

### 1.1 列出所有文件

列出项目目录下所有文件（排除 `.git`、`node_modules`、`__pycache__` 等依赖目录），用当前平台的合适工具（Windows 用 `Get-ChildItem`，Linux/macOS 用 `find`）。

### 1.2 识别项目类型

| 信号 | 类型 | 额外检查项 |
|------|------|-----------|
| 存在 `SKILL.md` | AI Agent Skill | 检查 YAML frontmatter、references/ 结构 |
| 存在 `package.json` / `setup.py` / `Cargo.toml` | 代码项目 | 检查 CI/CD、构建说明、依赖声明 |
| 纯 Markdown 文件（无代码） | 文档/方法论 | 重点评估 README 质量和内容结构 |
| SKILL.md + 代码混合 | Skill + 工具 | 按 Skill 类型处理，额外检查可执行脚本 |

### 1.3 对照标准检查缺失文件

GitHub 官方 Community Profile 考核项（Insights → Community）：

| # | 文件 | 位置 |
|---|------|------|
| 1 | Description | GitHub 网页 / API 创建时设置 |
| 2 | README.md | 根目录 / `.github/` / `docs/` |
| 3 | LICENSE | 根目录 / `.github/` / `docs/` |
| 4 | CODE_OF_CONDUCT.md | 根目录 / `.github/` / `docs/` |
| 5 | CONTRIBUTING.md | 根目录 / `.github/` / `docs/` |
| 6 | Issue 模板 | `.github/ISSUE_TEMPLATE/` 目录（多个模板文件） |
| 7 | PR 模板 | `.github/pull_request_template.md` |

额外推荐（不在官方考核，但专业项目标配）：

| 文件 | 说明 |
|------|------|
| `SECURITY.md` | 漏洞报告渠道，支持位置：根目录 / `docs/` / `.github/` |
| `.gitignore` | Git 忽略规则 |
| `CHANGELOG.md` | 版本变更记录（代码项目推荐，使用 Conventional Commits 格式） |
| `.editorconfig` | 统一编辑器配置（缩进、行尾、编码），确保多人协作代码风格一致 |
| `.gitattributes` | 行尾规范（`* text=auto`）、二进制文件标记、语言统计修正 |
| 社交预览图片 | 仓库 Settings → Social preview，影响社交媒体分享效果 |

### 1.4 额外检查项（参考 repolinter 行业标准）

| 检查项 | 说明 | 适用类型 |
|--------|------|----------|
| README 引用 LICENSE | README 中应包含 License 链接（如 `[MIT](LICENSE)`） | 全部 |
| 无二进制文件 | 不应提交 `.exe`/`.dll` 等编译产物（应通过 Release 分发） | 全部 |
| 测试目录存在 | 代码项目应有 `test/` 或 `tests/` 目录 | 代码项目 |
| 源码 License 头部 | 源码文件头部应有 Copyright/License 声明 | 代码项目（可选） |
| NOTICE 文件 | Apache 2.0 项目需要 NOTICE 文件 | Apache 2.0 项目 |

### 1.5 输出检查结果

逐项列出：✅ 已有 / ❌ 缺失 / ⚠️ 存在但不完整。

### 1.6 隐私扫描（必须）

扫描所有文件中的敏感信息。扫描规则和处理方式详见 `references/privacy-scan.md`。

重点检查：
- API Key / Token / Secret / Password（真实值，非占位符）
- 真实邮箱、手机号、身份证号
- 包含真实用户名的文件路径（`C:\Users\用户名\...`）
- 私网 IP（`192.168.x.x`、`10.x.x.x`）
- 数据库连接串、内网域名

**发现泄露 → 列出具体行号和内容，替换为占位符后再继续。**

**异常处理**：

| 情况 | 处理 |
|------|------|
| 项目目录不存在 | 提示用户确认路径后重试 |
| 目录为空 | 询问用户是否从零创建新项目 |
| 扫描到的文件超过 200 个 | 缩小范围，跳过 `node_modules`、`vendor` 等依赖目录 |
| 检测到已有 `.git` 目录 | 不重新 git init，直接进入扫描 |

---

## Step 2: 补齐缺失文件

> **检查点**：向用户展示 Step 1 的结果（项目类型 + 缺失清单），确认后进入补齐。

生成原则：
- 中英双语（中文项目可全中文，建议保留英文摘要）
- 内容精准适配项目类型，不套通用模板
- 生成前先简要说明将要创建的内容，获得用户认可

| 文件 | 生成要点 |
|------|----------|
| **LICENSE** | 默认 MIT；代码保护用 Apache 2.0（需附 NOTICE 文件）；创意内容用 CC BY 4.0 |
| **README.md** | 结构参考 `references/readme-template.md`，支持中英双语。**必须包含 `📥 下载/Download` 章节**，列出表格：HTTPS clone、SSH clone、GitHub CLI (`gh repo clone`)、ZIP 下载、curl/wget 单文件下载至少 5 种方式。安装示例应覆盖 Claude Code、Codex、Cursor 等主流 AI Agent 平台（Skill 项目），示例路径用 `~/.claude/skills/`。**下载链接中的分支名必须用仓库真实默认分支**（main 或 master，见 Step 5 推送后确认），写死 `main` 在 master 仓库上会导致 ZIP/Tar/raw 链接 404；README 中的 `<owner>/<repo>` 占位符必须替换为真实用户名/仓库名 |
| **.gitignore** | Node.js: `node_modules/` `dist/`；Python: `__pycache__/` `*.pyc`；Skill: `.obsidian/workspace.json`；通用: `.DS_Store` `Thumbs.db` |
| **CONTRIBUTING.md** | 贡献方式 + Fork/Branch/PR 流程 + 行为准则引用 |
| **CODE_OF_CONDUCT.md** | 引用 Contributor Covenant 2.1 + 报告渠道 |
| **SECURITY.md** | 支持位置：根目录 / `docs/` / `.github/`<br>方法论/文档类项目可极简（只说明报告渠道）<br>代码项目建议详细：支持版本、漏洞严重性分类、响应时间承诺<br>GitHub 支持开启 Private vulnerability reporting（仓库 Settings → Security） |
| **CHANGELOG.md** | 代码项目推荐，使用 Conventional Commits 格式。格式和示例见 `references/templates-and-formats.md` |
| **Issue 模板** | 使用 `.github/ISSUE_TEMPLATE/` 目录，支持两种格式：<br>• **Markdown 模板**（`.md`）：传统格式，简单直接<br>• **YAML 表单**（`.yml`）：结构化表单，用户体验更好（推荐）<br>可选添加 `config.yml` 控制模板选择器（禁用空白 Issue、添加外部链接）<br>代码项目：Bug/Feature/Question；文档/Skill：问题报告/建议/文档改进 |
| **PR 模板** | 改动类型（勾选） + 说明 + 文件列表 + 检查清单 |
| **.editorconfig** | 统一缩进风格（2空格/4空格/Tab）、行尾（LF）、编码（UTF-8） |
| **.gitattributes** | `* text=auto` 自动行尾、二进制文件标记 `binary`、vendored 代码排除统计 |

### 项目类型速查

根据 Step 1 识别的类型，按以下清单生成（跳过已存在的文件）：

| 类型 | 需要生成的文件 |
|------|--------------|
| **Skill 项目** | LICENSE + README + .gitignore + CONTRIBUTING + CODE_OF_CONDUCT + SECURITY + `.github/ISSUE_TEMPLATE/` 目录 + PR 模板 |
| **代码项目** | LICENSE + README + .gitignore + CONTRIBUTING + CODE_OF_CONDUCT + CHANGELOG + SECURITY + `.github/ISSUE_TEMPLATE/` 目录 + PR 模板 + .editorconfig + .gitattributes |
| **文档项目** | LICENSE + README + .gitignore + CONTRIBUTING + `.github/ISSUE_TEMPLATE/` 目录 + PR 模板（CODE_OF_CONDUCT 和 SECURITY 可选，不需要 CHANGELOG） |

生成后向用户展示完整文件列表和内容摘要，确认是否全部需要。

---

## Step 3: 审查改进

> **检查点**：向用户展示 Step 2 生成的文件列表和内容摘要，确认后进行审查。

### 3.1 SKILL.md 合规（仅 Skill 项目）

| 检查项 | 要求 |
|--------|------|
| YAML frontmatter | 必须有 `name` + `description` |
| 敏感信息 | 无硬编码路径、个人隐私 |
| 触发词 | 移至附录，不影响通用阅读 |
| 平台依赖 | 核心内容与特定平台解耦 |

### 3.2 隐私二次验证

推送前最终检查（防止 Step 2 生成的文件引入新泄露）：
- [ ] 所有文件中无真实 API Key / Token / Secret
- [ ] 无真实邮箱、手机号、身份证号
- [ ] 无包含真实用户名的文件路径
- [ ] 无私网 IP、内网域名、数据库连接串
- [ ] 占位符（`你的API密钥`、`example@xxx.com`）不算泄露，保留

### 3.3 通用内容审查

- [ ] README 5 秒内可懂
- [ ] 至少一个可运行示例
- [ ] 无敏感信息（API Key、邮箱、内网路径）
- [ ] 文件引用路径正确（相对路径）
- [ ] 中英双语版本结构对应（如果需要双语）
- [ ] 语言切换链接正确（`[English](#english) | [中文](#中文)`）
- [ ] Emoji 图标增强可读性
- [ ] 核心特性用表格展示
- [ ] README 引用 LICENSE（如 `[MIT](LICENSE)`）
- [ ] README 不超过 512 KB（GitHub 会截断超过此大小的内容）
- [ ] 无残留 `<owner>`/`<repo>` 等未替换占位符（README、`.github/ISSUE_TEMPLATE/config.yml` 等交付文件）
- [ ] 下载链接（ZIP/Tar/raw 单文件）的分支名与仓库实际默认分支一致（main 或 master）

---

## Step 4: 生成 Description

按规则生成仓库简介。**规则 + 模板 + 案例 + Topics 建议** 详见 `references/description-guide.md`。

简要原则：
- 120 字以内，`功能 + 亮点`
- 禁止「一个用于…的项目」式废话、版本号
- 按项目类型选用模板

---

## Step 5: 推送到 GitHub

### 5.1 展示确认清单

向用户展示仓库名、Description、Topics、文件列表，**等待明确确认**。

### 5.2 创建仓库 + 推送

**方案选择**：优先尝试 GitHub MCP 工具，如 MCP 不可用或权限不足，回退到 curl + git。详细命令和异常处理见 `references/mcp-push-guide.md`。

如找不到 token，引导用户参考 `references/github-pat-setup.md` 配置。

---

## Step 6: Release + 多平台分发

> **检查点**：Step 5 推送完成后进入本步骤。如果是纯文档/方法论项目，可跳过 6.2-6.4，只做 6.1。

### 6.1 创建首个 GitHub Release

语义化版本号（SemVer）：`v主版本.次版本.修订号`

| 变更类型 | 版本影响 | 示例 |
|----------|----------|------|
| 破坏性变更 | 主版本 +1 | `v2.0.0` |
| 新功能 | 次版本 +1 | `v1.1.0` |
| Bug 修复 | 修订号 +1 | `v1.0.1` |

**创建步骤**：打 tag 并推送 → GitHub Releases → Create a new release → 填写说明 → 上传编译产物（如有）→ Publish

> 详细步骤、下载链接格式见 `references/release-and-distribution.md`。

### 6.2 多平台包发布（代码项目）

根据项目主语言选择对应的包管理平台发布。**详细配置和发布命令见 `references/release-and-distribution.md`**。

**推荐发布顺序**（不用一次全搞定）：
1. 代码推到 GitHub → 源码下载自动有
2. 发布到主语言的包管理器（JS→npm，Python→PyPI，Rust→crates.io）
3. 用户量大了再加：Homebrew、Docker

### 6.3 README 安装章节适配

根据项目类型在 README 中提供对应的安装/下载方式表格。**模板见 `references/readme-template.md`**。

### 6.4 向用户确认分发方案

根据 Step 1 识别的项目类型和技术栈，向用户推荐适合的分发渠道：
- 检测到 `package.json` → 推荐 npm 发布
- 检测到 `pyproject.toml` / `setup.py` → 推荐 PyPI 发布
- 检测到 `Cargo.toml` → 推荐 crates.io 发布
- 检测到 `Dockerfile` → 推荐 Docker Hub 发布
- Skill 项目 → 只需要 git clone 安装方式

**用户确认后，才协助执行发布命令。**

---

## Step 7: 发布后优化

> 推送和分发完成后，建议进行以下优化。非必须，但能显著提升项目专业度和可维护性。

### 7.1 仓库设置优化

引导用户在 GitHub 仓库 Settings 中配置：

| 设置项 | 位置 | 推荐值 |
|--------|------|--------|
| **合并策略** | Settings → General → Pull Requests | 只启用 Squash Merge（保持主分支线性历史） |
| **自动删除分支** | Settings → General → Pull Requests | 开启 "Automatically delete head branches" |
| **建议更新分支** | Settings → General → Pull Requests | 开启 "Always suggest updating pull request branches" |
| **Discussions** | Settings → Features | 按需开启，将问答和讨论从 Issues 中分离 |
| **Wiki** | Settings → Features | 复杂项目开启，简单项目不需要 |
| **社交预览图** | Settings → Social preview | 上传 1280x640 PNG 图片 |

**分支保护**：推荐使用 **Repository Rulesets**（Settings → Rules → New ruleset），比传统分支保护规则更灵活（可组合、可针对用户/团队、可分层）。新项目优先用 Rulesets 而非传统分支保护。

**初始 Labels**（可选）：新仓库建议创建标准标签，便于后续 Issue 管理。已安装 gh CLI 时可用 `gh label create bug --color "d73a4a" --description "Something isn't working"` 等命令批量创建。推荐标签：`bug`、`enhancement`、`good first issue`、`documentation`、`question`。

### 7.2 GitHub Actions CI/CD（代码项目推荐）

根据项目技术栈生成基础 CI 工作流文件 `.github/workflows/ci.yml`。**Node.js 和 Python 的完整 YAML 模板见 `references/templates-and-formats.md`**。

**推荐的额外 Actions**：

| Action | 用途 | 优先级 |
|--------|------|--------|
| `github/codeql-action` | 安全漏洞扫描 | 代码项目推荐 |
| `github/super-linter` | 多语言代码风格检查 | 可选 |
| `actions/stale` | 自动标记/关闭过期 Issue | 用户多了之后加 |

### 7.3 Dependabot 配置（代码项目推荐）

生成 `.github/dependabot.yml`，自动检测依赖更新。**完整配置示例（含 groups 分组更新、cooldown 冷却期等新功能）见 `references/templates-and-formats.md`**。

基础配置：
```yaml
version: 2
updates:
  - package-ecosystem: "npm"  # 或 "pip"、"cargo"、"gomod"
    directory: "/"
    schedule:
      interval: "weekly"
    groups:
      development-dependencies:
        applies-to: "version-updates"
        dependency-type: "development"
      production-dependencies:
        applies-to: "version-updates"
        dependency-type: "production"
```

### 7.4 .github 默认仓库机制（可选）

GitHub 支持创建一个名为 `.github` 的**公开**仓库，存放默认社区健康文件，对该账号下所有缺少对应文件的仓库生效。适合管理多个仓库的组织或个人。

> 注意：LICENSE 文件不能作为默认文件，必须添加到每个具体仓库。

### 7.5 推荐发布顺序总览

不用一开始就全部搞定，按优先级来：

| 优先级 | 事项 | 说明 |
|--------|------|------|
| P0 | 代码推到 GitHub | 源码下载自动有 |
| P0 | LICENSE + README + .gitignore | 开源三件套 |
| P1 | 创建首个 Release | 上传编译产物（如有） |
| P1 | 发布到主语言包管理器 | npm / PyPI / crates.io |
| P1 | 补全 CONTRIBUTING + Issue/PR 模板 | 吸引贡献者 |
| P1 | 仓库设置优化 | Squash Merge、Rulesets 分支保护 |
| P2 | CI/CD 工作流 | GitHub Actions 自动测试 |
| P2 | Dependabot | 依赖自动更新 |
| P2 | 加 Homebrew / Docker | 用户量大了再加 |
| P2 | .editorconfig + .gitattributes | 多人协作时加 |
| P2 | CODEOWNERS | 多人维护时加 |