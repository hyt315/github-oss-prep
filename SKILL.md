---
name: github-oss-prep
description: Use when preparing, publishing, launching, or improving any project for open-source adoption on GitHub. Features 6 archetype-tailored README engines (AI Skill, CLI tool, Multimedia, SDK, Fullstack App, Docs), 5-layer deep environment and credential security scanning, GitHub 2026 Community Profile YAML Issue Forms, multi-channel distribution matrix, clean-clone validation, and approval-gated publishing. Triggers include GitHub 开源准备, 准备发布到 GitHub, 美化项目准备开源, 开源化, 开源推广, oss prep, publish to GitHub, launch an open-source project, and prepare for open source.
metadata:
  author: hyt315
---

# GitHub 开源准备

将任意项目美化为适合 GitHub 发布的专业级开源版本，补齐全套 100% 社区健康文件，构建专属针对性门面。

## 核心理念

- **先审后改，不盲目覆盖**：保留有效内容；已有文件若过时、残缺或存在风险，先展示差异与理由，获批后再修改。
- **按六大品类深度适配**：对 AI Skill、CLI 系统工具、前端多媒体、类库 SDK、全栈应用、文档知识库提供专属门面结构。
- **对齐 GitHub 2026 官方社区标准**：通过 Insights → Community 100% 考核（全量采用交互式 YAML Issue Forms）。
- **五重严密环境与隐私扫描**：深度拦截敏感凭据、私有路径指纹、内部会话标记、Git URL 凭据污染与构建缓存。
- **全渠道现代分发与下载矩阵**：自动匹配 `gh skill`、Agent 一句话自装、Release 预编译资产（含 SHA-256 校验）与包管理器。
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
Step 2: 社区文件补全 (YAML Issue Forms + PR 模板 + SECURITY + LICENSE)
    ↓
Step 3: 专属针对性 README 门面生成 (基于六大品类引擎 + 动态 Shields 徽章)
    ↓
Step 4: 全渠道分发与下载矩阵配置 (gh skill / Agent 自装 / Release Checksums)
    ↓
Step 5: 干净环境验证 (scripts/selftest.py + 规范审计 100% 通过)
    ↓
Step 6: 发布确认 → 远程推送、创建 Release 与资产分发
```

---

## 工作流各阶段要点

### Step 0: 定位与品类识别
- 确定项目属于哪一类：**AI Agent 技能**、**CLI / 系统工具**、**前端 / 多媒体生成**、**类库 / SDK**、**全栈 / Web 服务**、**文档 / 知识库**。
- 输出定位卡：目标用户、核心价值、1 分钟复现示例与非目标。

### Step 1: 五重环境与隐私安全扫描
- 必须扫描全树代码、文档与 Git 配置。
- 严密拦截：API Keys (OpenAI, Anthropic, Gemini, GitHub PATs, SSH)、本地绝对路径 (`<user_home>` 等)、私有 Agent 会话 ID、`.git/config` 中的明文 URL Token、构建缓存残留。
- 详见 [隐私与环境安全扫描指南](references/privacy-scan.md)。

### Step 2: 100% 社区健康文件补齐
- 生成 GitHub 2026 标准 YAML 格式 Issue Forms：`.github/ISSUE_TEMPLATE/bug_report.yml`、`feature_request.yml` 与 `config.yml`。
- 补齐 `CODE_OF_CONDUCT.md`、`CONTRIBUTING.md`、`SECURITY.md`、`.editorconfig` 与 `.gitattributes`。
- 详见 [社区健康文件库与模板](references/community-templates.md)。

### Step 3: 专属针对性 README 门面生成
- 依据 Step 0 确定的项目品类，从 6 大专属模板中生成高转化率中英文门面：
  - **AI Skill**：顶部双语 + 一句话 Agent 自装 + 跨平台目录安装表 + Reference Map（阅读时机与耗时）。
  - **CLI / 系统工具**：痛点解构 + ASCII 架构图 + 6 大实战速查表 + Zero-Harm / Zero-Mutation 只读安全铁律。
  - **前端 / 多媒体**：视觉效果 Gallery + 画布比例矩阵 + 宽泛依赖区间。
  - **类库 / SDK**：5 行极速 Hello World + API 参数表 + SemVer 兼容承诺。
  - **全栈应用**：Live Demo + 1 键部署 + `.env.example` 环境变量表。
- 详见 [六大品类 README 模板库](references/readme-template.md)。

### Step 4: 全渠道分发与下载矩阵配置
- 自动适配现代分发渠道：`gh skill install`、Release 预编译资产（附带 SHA-256 校验和）、`npm/pip/cargo` 包管理。
- 详见 [全渠道分发与下载矩阵](references/release-and-distribution.md)。

### Step 5: 验证与发布门禁
- 运行 `python scripts/selftest.py` 与 `validate_repo.py` 进行全量回归。
- 详见 [PR、CI 与发布门禁工作流](references/pr-and-release-workflow.md)。

---

## Reference Map

- 需要为项目选择并生成专属风格 README 时，先读 [六大品类 README 模板库](references/readme-template.md)：涵盖 6 大项目形态完整中英文结构与动态徽章规范（预计阅读时间：4 分钟）。
- 需要执行隐私与环境安全扫描、拦截私有路径与凭据时，先读 [隐私与环境安全扫描指南](references/privacy-scan.md)：5 重扫描防御网与标准脱敏规则（预计阅读时间：3 分钟）。
- 需要配置 GitHub 2026 社区文件（YAML 表单、安全策略）时，先读 [社区健康文件库与模板](references/community-templates.md)：全量 YAML Issue Forms 与合规模版（预计阅读时间：3 分钟）。
- 需要配置软件下载形态、多平台分发与 Release 校验和时，先读 [全渠道分发与下载矩阵](references/release-and-distribution.md)：涵盖包管理、CLI 资产、Agent 技能多渠道路由（预计阅读时间：3 分钟）。
- 需要撰写仓库 Description、Topics 与推广材料时，先读 [Description 与 Topics 优化指南](references/description-guide.md) 与 [开源发现与推广策略](references/discovery-and-promotion.md)（预计阅读时间：3 分钟）。
- 需要配置远程推送、MCP 或 GitHub PAT 权限时，先读 [GitHub MCP 与推送指南](references/mcp-push-guide.md)、[PAT 配置指南](references/github-pat-setup.md) 与 [PAT 类型对比](references/github-pat-comparison.md)（预计阅读时间：2 分钟）。
- 需要配置 PR、CI 自动化测试与发版门禁时，先读 [PR、CI 与发布门禁工作流](references/pr-and-release-workflow.md)（预计阅读时间：3 分钟）。
