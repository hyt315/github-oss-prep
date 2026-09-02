---
name: github-oss-prep
description: Use when preparing, publishing, launching, or improving any project for open-source adoption on GitHub. Features 6 archetype-tailored README engines (AI Skill, CLI tool, Multimedia, SDK, Fullstack App, Docs), all-channel package distribution guides (npm, PyPI, Docker, Homebrew, Cargo, Go), 5-layer deep security scanning, YAML Issue Forms, CI/Dependabot templates, and approval-gated publishing. Triggers include GitHub 开源准备, 准备发布到 GitHub, 美化项目准备开源, 开源化, 开源推广, oss prep, publish to GitHub, launch an open-source project, and prepare for open source.
metadata:
  author: hyt315
---

# GitHub 开源准备

将任意项目美化为适合 GitHub 发布的专业级开源版本，补齐全套 100% 社区健康文件与 CI/Dependabot 配置，构建专属针对性门面与全渠道分发。

## 核心理念

- **先审后改，不盲目覆盖**：保留有效内容；已有文件若过时、残缺或存在风险，先展示差异与理由，获批后再修改。
- **按六大品类深度适配**：对 AI Skill、CLI 系统工具、前端多媒体、类库 SDK、全栈应用、文档知识库提供完整开箱即用门面。
- **对齐 GitHub 2026 官方社区标准**：通过 Insights → Community 100% 考核（全量采用交互式 YAML Issue Forms 与 CI 模板）。
- **五重严密环境与隐私扫描**：深度拦截敏感凭据、私有路径指纹、内部会话标记、Git URL 凭据污染与构建缓存。
- **全渠道现代分发与下载矩阵**：自动匹配 npm、pip、cargo、homebrew、winget、Docker、gh skill 与 Release SHA-256 校验和。
- **分阶段授权与确认发布**：本地整理、远程推送、Release 打包与外部推广分别独立授权，严禁越权。

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
Step 0: 定位与品类识别 (AI Skill / CLI / 多媒体 / SDK / 全栈应用 / 文档)
    ↓
Step 1: 五重深度安全扫描 (凭据 + 私有路径 + 会话标记 + Git 污染 + 构建产物)
    ↓
Step 2: 社区文件与 CI 补全 (YAML Issue Forms + PR 模板 + SECURITY + CI/Dependabot)
    ↓
Step 3: 专属针对性 README 门面生成 (从六大品类完整模板引擎渲染 + 动态徽章)
    ↓
Step 4: 全渠道分发与包管理配置 (npm / pip / cargo / docker / brew / gh skill / Checksums)
    ↓
Step 5: 干净环境验证 (scripts/selftest.py + 规范审计 100% 通过)
    ↓
Step 6: 发布确认 → 远程推送、创建 Release 与多平台分发
```

---

## 工作流各阶段要点

### Step 0: 定位与品类识别
- 确定项目属于哪一类：**AI Agent 技能**、**CLI / 系统工具**、**前端 / 多媒体生成**、**类库 / SDK**、**全栈 / Web 服务**、**文档 / 知识库**。
- 输出定位卡：目标用户、核心价值、1 分钟复现示例与非目标。

### Step 1: 五重环境与隐私安全扫描
- 必须扫描全树代码、文档与 Git 配置。
- 严密拦截：API Keys (OpenAI, Anthropic, Gemini, GitHub PATs, SSH)、本地绝对路径、私有 Agent 会话 ID、`.git/config` 中的明文 URL Token、构建缓存残留。
- 详见 [隐私与环境安全扫描指南](references/privacy-scan.md)。

### Step 2: 100% 社区健康文件与 CI 补齐
- 生成 GitHub 2026 标准 YAML 格式 Issue Forms：`.github/ISSUE_TEMPLATE/bug_report.yml`、`feature_request.yml` 与 `config.yml`。
- 补齐 `CODE_OF_CONDUCT.md`、`CONTRIBUTING.md`、`SECURITY.md`、GitHub Actions CI 矩阵工作流、`dependabot.yml`、`.editorconfig` 与 `.gitattributes`。
- 详见 [社区健康文件库与模板](references/community-templates.md)。

### Step 3: 专属针对性 README 门面生成
- 依据 Step 0 确定的项目品类，从 6 大专属完整模板中生成高转化率中英文门面：
  - **AI Skill**：顶部双语 + 一句话 Agent 自装 + 跨平台目录安装表 + Reference Map。
  - **CLI / 系统工具**：痛点解构 + ASCII 架构图 + 6 大实战速查表 + 包管理器安装表 + Zero-Harm 只读安全铁律。
  - **前端 / 多媒体**：视觉效果 Gallery + 画布比例矩阵 + 宽泛依赖区间。
  - **类库 / SDK**：5 行极速 Hello World + API 参数表 + npm/pip/cargo 安装表 + SemVer 兼容承诺。
  - **全栈应用**：Live Demo + 1 键部署 + Docker 命令 + `.env.example` 环境变量表。
- 详见 [六大品类 README 模板库](references/readme-template.md)。

### Step 4: 全渠道分发与包管理实操
- 自动适配发版渠道：npm、PyPI、Docker/ghcr.io、Homebrew、Crates.io、Go、`gh skill` 与 Release SHA-256 校验和。
- 详见 [全渠道分发与发版实操指南](references/release-and-distribution.md)。

### Step 5: 验证与发布门禁
- 运行 `python scripts/selftest.py` 与 `validate_repo.py` 进行全量回归。
- 详见 [PR、CI 与发布门禁工作流](references/pr-and-release-workflow.md)。

---

## Reference Map

- 需要为项目选择并生成专属风格 README 时，先读 [六大品类 README 模板库](references/readme-template.md)：涵盖 6 大项目形态完整开箱即用 Markdown 骨架与包管理器安装表（预计阅读时间：4 分钟）。
- 需要执行隐私与环境安全扫描、拦截私有路径与凭据时，先读 [隐私与环境安全扫描指南](references/privacy-scan.md)：5 重扫描防御网、真伪泄露案例比对与脱敏规则（预计阅读时间：3 分钟）。
- 需要配置 GitHub 2026 社区文件、CI 矩阵与 Dependabot 时，先读 [社区健康文件库与模板](references/community-templates.md)：全量 YAML Issue Forms、CI 流水线与 Dependabot 配置（预计阅读时间：3 分钟）。
- 需要配置 npm/pip/cargo/docker/brew 多平台发版与 Release 校验和时，先读 [全渠道分发与发版实操指南](references/release-and-distribution.md)：涵盖全生态发版命令、配置文件与国内镜像源（预计阅读时间：4 分钟）。
- 需要撰写仓库 Description、Topics 与推广材料时，先读 [Description 与 Topics 优化指南](references/description-guide.md) 与 [开源发现与推广策略](references/discovery-and-promotion.md)（预计阅读时间：3 分钟）。
- 需要配置远程推送、MCP 或 GitHub PAT 权限时，先读 [GitHub MCP 与推送指南](references/mcp-push-guide.md)、[PAT 配置指南](references/github-pat-setup.md) 与 [PAT 类型对比](references/github-pat-comparison.md)（预计阅读时间：2 分钟）。
- 需要配置 PR、CI 自动化测试与发版门禁时，先读 [PR、CI 与发布门禁工作流](references/pr-and-release-workflow.md)（预计阅读时间：3 分钟）。
