# 📦 GitHub 开源准备 / GitHub OSS Prep

<div align="center">

**将任意项目美化为适合 GitHub 发布的专业级开源版本，补齐全套社区健康文件与 CI 自动化，构建专属针对性门面与全生态分发。**

**Turn any project into a polished, GitHub-ready open-source repository with full community health files, CI automation, and tailored multi-channel distribution.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/hyt315/github-oss-prep?sort=semver)](CHANGELOG.md)
[![Validate skill](https://github.com/hyt315/github-oss-prep/actions/workflows/validate.yml/badge.svg)](https://github.com/hyt315/github-oss-prep/actions)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1f6feb)](SKILL.md)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Python)-brightgreen)](SKILL.md)
[![GitHub Stars](https://img.shields.io/github/stars/hyt315/github-oss-prep?style=social)](https://github.com/hyt315/github-oss-prep/stargazers)

[English](./README.en.md) | [中文](./README.md)

</div>

---

## 📖 这是什么？

将代码、智能体或知识库项目推送到 GitHub 开源时，开发者往往面临这些繁琐痛点：
- 缺少合规的 `LICENSE`、`CODE_OF_CONDUCT.md`、`CONTRIBUTING.md` 或现代 YAML 格式的 Issue 表单，社区健康文件不齐（GitHub 官方未提供"满分/百分比"口径，本技能按官方点名文件逐一核对）；
- README 结构泛化千篇一律，无法突出 AI 技能、MCP Server、大模型/GGUF、系统 CLI、浏览器扩展或全栈 Web 应用的独特核心价值；
- 缺少 `uvx`、`bunx`、`pnpm dlx`、Hugging Face、Chrome Web Store 的具体发版指令与 CI 矩阵测试；
- 不慎把本地绝对路径（`<user_home>`）、私有 Agent 会话标记、甚至 API 密钥与 Git 凭据推送到公共仓库造成泄露。

**`github-oss-prep`** 是一个专为 AI Agent（与开源作者）打造的专业级 GitHub 开源准备技能。它确立了 **渐进式披露原则（Progressive Disclosure）**，内置 **十大全景项目品类专属 README 完整模板库**、**全生态发版实操指南**、**五重深度环境与隐私安全审计网** 与 **GitHub 2026 社区与 CI 自动化文件库**，实现一键规范化整理与安全发布。

---

## ✨ 核心特性

| 核心模块 | 覆盖功能 | 带来价值 |
|---|---|---|
| **分类主表 + 品类 README 引擎** | `references/category-map.md` 用 12 类主表 + 三轴 + 旗标做判定（唯一分类源）；`readme-template.md` 提供 10 份骨架、通用底座 12 节与**逐空判据**（`<!-- 判据 -->`/`<!-- 反例 -->`/`<!-- 可删 -->`） | 先定类再取模板；填空处同时给出"怎样算写好"，避免只套格式不判断 |
| **渐进式披露执行铁律** | 依据品类判定结果定向调阅专属规范，严格隔离无关品类 | 减少上下文膨胀与跨品类交叉污染 |
| **五重深度隐私安全网** | 凭据/PAT/PEM 私钥、路径与私网指纹、会话标记、Git Remote 凭据、构建缓存；规则唯一真相源 `scripts/secret-rules.json` | 拦住现行格式的凭据泄露；覆盖范围与已知盲区在 `privacy-scan.md` 明示 |
| **2026 社区与 CI 自动化库** | 交互式 YAML Issue Forms、PR 模板、`SECURITY.md`、**Node/Python 矩阵 CI（锁 SHA + 顶层只读）** 与 **Dependabot 配置** | 社区健康文件按官方口径齐备；CI 供应链加固、依赖自动更新 |
| **全生态分发与发版实操** | **uv/PyPI、npm、Hugging Face、Chrome Web Store、Docker、Homebrew、Crates.io** 具体发版指南与 Release Checksums | 提供从本地代码到全球各大分发中心的全流程发版指令 |
| **可验证工程架构** | 校验器可指向任意项目（`validate_repo.py <dir>`）、分级 finding、fixture 回归（真阳必检、干净样例不误报） | 门禁可复核：每条结论都能用命令复现，未测量不出口绿灯 |

---

## 📊 开源准备全流程架构

```
[输入：本地任意待开源项目 / 目录]
                 │
      [Step 0: 定位（目标用户 + 核心价值 + 可验证结果）]
      精准判定：AI Skill / MCP Server / 模型权重 / CLI 工具 / 浏览器扩展 / IaC / ...
                 │
      [Step 1: 扫描（识别类型 + 检查缺失、薄弱与风险项）]
      对照 GitHub Community Profile 考核项检查
                 │
      [Step 2: 整理（补齐缺失文件 + 经确认改进薄弱文件）]
      生成中英双语社区健康文件
                 │
      [Step 3: 验证（内容 + 隐私 + 来源许可 + 干净环境运行）]
      五重深度安全扫描，确保无敏感信息泄露
                 │
      [Step 4: 仓库门面（README + Description + Topics + 社交预览）]
      渐进式披露，定向调阅专属品类完整骨架
                 │
      [Step 5: 发布确认 → 分支/PR（默认）或个人直推（可选）]
      public-safe 或 solo-fast 双模式
                 │
      [Step 6: Release + 多平台分发 + 版本一致性验证]
      uv/PyPI/npm/HuggingFace/ChromeStore/Docker/Homebrew/Crates.io
                 │
      [Step 7: 发现与增长（Launch Kit + 定向发布 + 反馈闭环）]
      Stranger Test、渠道选择、发布节奏
```

---

## 🚀 快速开始

这是一个标准的 AI Agent Skill —— 安装到你的 AI 助手后即可直接使用。

### 方式 A：把一句话发给任意 Agent（最推荐、最通用）

把下面这句话直接复制发送给你的 AI 助手，它会自动识别环境并克隆到正确的技能目录：

> 请安装 github-oss-prep 技能：克隆 `https://github.com/hyt315/github-oss-prep` 到你的 skills 目录（如 `~/.claude/skills/github-oss-prep` 或 `~/.agents/skills/github-oss-prep`），并确认安装成功。

> 💡 **小模型同样适配**：安装完成后，只需对 AI 说“帮我把这个项目开源整理一下”或“准备发布到 GitHub”，即可自动触发全流程。

### 方式 B：GitHub CLI 2.90+（一行命令）

```bash
# gh skill 目前为 Public Preview（命令与 flag 可能变动），先 `gh skill --help` 确认
gh skill install hyt315/github-oss-prep github-oss-prep --agent claude-code --scope user --pin
```

### 方式 C：多平台手动安装

| 平台 | 安装命令 |
|---|---|
| **Claude Code** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.claude/skills/github-oss-prep` |
| **Codex** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.codex/skills/github-oss-prep` |
| **Cursor** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.cursor/skills/github-oss-prep` |
| **通用 Agents 目录** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.agents/skills/github-oss-prep` |

### 方式 D：本地运行回归自测

```bash
python scripts/selftest.py
```

---

## 📚 端到端实战演示

假设本地有一个编写好的 Python CLI 工具、MCP Server 或浏览器扩展准备开源：

1. **触发与扫描**：向 AI 发送“帮我准备开源这个项目” → 自动识别品类，执行 5 重隐私扫描，阻断路径指纹与未清理缓存；
2. **生成社区与 CI 文件**：自动生成符合 GitHub 2026 规范的 YAML Issue Forms、`SECURITY.md`、`LICENSE` 以及 Node/Python 矩阵 CI 流水线；
3. **渐进式渲染门面**：严格根据品类调阅对应模版，生成包含痛点解构、现代运行器矩阵 (`uvx`/`bunx`)、配置代码块的中英文 README；
4. **验证与分发**：本地运行 `selftest.py` 自动化回归自检，输出完整可审查项目包，在获得授权后一键发布 GitHub、Release 资产与对应生态中心。

---

## 🔒 安全与隐私原则

- **先审后改（Audit Before Change）**：本地整理默认只读扫描并输出差异报告，绝不擅自强行覆盖用户现有文件。
- **渐进式隔离（Progressive Isolation）**：处理特定项目时仅读取专属模板，杜绝上下文冗余与环境参数污染。
- **五重严密防御**：对代码、文档、`.git/config` 与历史提交进行全面深度扫描，阻断任何敏感信息。
- **分阶段明确授权**：本地开源整理、远程仓库创建、Release 打包分发与外部推广分别独立确认，绝不越权连带执行。

---

## 📥 下载与获取

| 方式 | 命令 / 链接 |
|---|---|
| **HTTPS** | `git clone https://github.com/hyt315/github-oss-prep.git` |
| **SSH** | `git clone git@github.com:hyt315/github-oss-prep.git` |
| **GitHub CLI** | `gh repo clone hyt315/github-oss-prep` |
| **ZIP 压缩包** | [下载 ZIP](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.zip) |
| **Tar 归档** | [下载 Tar](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.tar.gz) |
| **单文件 (SKILL.md)** | `curl -O https://raw.githubusercontent.com/hyt315/github-oss-prep/main/SKILL.md` |

---

## 📖 深度参考文档导读

| 参考文档 | 核心内容 | 推荐阅读时机 | 篇幅 |
|---|---|---|---|
| 🗺️ [**分类主表与判定路由 (`category-map.md`)**](references/category-map.md) | 12 类主表、三轴与旗标、主产物判定算法、路由回归用例 | 扫描项目、需要定 `category_id` 时 | 9.7 KB |
| 📑 [**十大品类完整 README 模板库 (`readme-template.md`)**](references/readme-template.md) | 10 大软件形态完整开箱即用 Markdown 骨架与现代终端运行器表 | 为项目生成或重构 README 时 | ~39.2 KB |
| 🚨 [**开源准备避坑库与官方规范基线 (`github-oss-prep-pitfalls.md`)**](references/github-oss-prep-pitfalls.md) | 社区健康文件官方口径、Git 历史凭据残留洗库与 CI 供应链 Action 锁定 | 评估安全基线与排查深水陷阱时 | ~16.3 KB |
| 🛡️ [**五重隐私与安全扫描 (`privacy-scan.md`)**](references/privacy-scan.md) | 5 重扫描防御网、真伪泄露实战比对表与脱敏规则 | 执行本地安全自检与脱敏排查时 | ~7.2 KB |
| 🏛️ [**社区健康文件与 CI 模板 (`community-templates.md`)**](references/community-templates.md) | 现代交互式 YAML Issue Forms、Node/Python 矩阵 CI 工作流与 Dependabot | 补齐 GitHub 社区文件与持续集成时 | ~9.7 KB |
| 🚀 [**全渠道分发与发版指南 (`release-and-distribution.md`)**](references/release-and-distribution.md) | uv、npm、HuggingFace、ChromeStore、Docker 发版实操、国内镜像源与 Checksums | 发布到全球平台或 GitHub Release 时 | ~7.5 KB |
| 🏷️ [**Description 与 Topics 指南 (`description-guide.md`)**](references/description-guide.md) | 精准 120 字仓库简介与高权重标签生成指南 | 设置 GitHub 仓库门面信息时 | ~4.8 KB |
| 🌐 [**开源发现与推广策略 (`discovery-and-promotion.md`)**](references/discovery-and-promotion.md) | Launch Kit 营销包、社交预览与全网发布渠道 | 准备发布与对外推广项目时 | ~2.6 KB |
| 🔐 [**GitHub 推送与 MCP 指引 (`mcp-push-guide.md`)**](references/mcp-push-guide.md) | 官方 MCP 与标准 CLI 推送流程 | 执行远程推送与仓库创建时 | ~5.2 KB |
| 🚦 [**PR 与发布门禁工作流 (`pr-and-release-workflow.md`)**](references/pr-and-release-workflow.md) | 分支、PR、CI 测试与发布自动化校验 | 建立持续集成与发版流水线时 | ~2.3 KB |
| 🔑 [**GitHub 凭据方案对比 (`github-pat-comparison.md`)**](references/github-pat-comparison.md) | 官方连接器、GitHub CLI 与 PAT 的权限与安全对比 | 选择推送认证方式时 | ~2.6 KB |
| 🔒 [**最小权限 PAT 创建指引 (`github-pat-setup.md`)**](references/github-pat-setup.md) | 在 GitHub 官方页面创建最小权限个人访问令牌的步骤 | 明确选择 PAT 方式时 | ~2.2 KB |

---

## 📁 文件结构

```
github-oss-prep/
├── SKILL.md                          # 核心技能定义、渐进式披露与轻量化工作流
├── README.md                         # 中文说明文档
├── README.en.md                      # 英文说明文档
├── CHANGELOG.md                      # 版本发布记录
├── LICENSE                           # MIT 开源许可证
├── .gitignore                        # Git 忽略规则
├── CONTRIBUTING.md                   # 社区贡献指南
├── CODE_OF_CONDUCT.md                # 行为准则
├── SECURITY.md                       # 安全策略
├── SUPPORT.md                        # 支持渠道
├── manifest.json                     # 技能元数据清单
├── agents/                           # 多 Agent 平台元数据
├── scripts/
│   ├── secret-rules.json             # 凭据/路径规则的**唯一真相源**（扫描器与测试共用）
│   ├── validate_repo.py              # 仓库结构、规范与隐私安全校验器（可指向任意目录）
│   └── selftest.py                   # 自动化回归自测脚本
├── tests/
│   ├── test_skill.py                 # stdlib unittest 入口（含门禁红/绿样例）
│   └── fixtures/
│       ├── leaked-repo/              # 故意含假凭据：断言必须被检出
│       └── clean-repo/               # 干净样例：断言不误报
├── .github/
│   ├── CODEOWNERS                    # 代码审查者配置
│   ├── pull_request_template.md      # 标准 PR 模板
│   ├── workflows/                    # CI 自动化工作流
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.yml            # 交互式 Bug 反馈表单
│       ├── doc_improvement.yml       # 文档改进表单
│       ├── feature_request.yml       # 交互式功能建议表单
│       └── config.yml                # Issue 模板选择器配置
└── references/                       # 深度参考文档
    ├── category-map.md               # 唯一分类源：12 类主表 + 判定路由
    ├── github-oss-prep-pitfalls.md   # 开源准备核心避坑库与官方规范基线
    ├── readme-template.md            # 十大品类专属 README 完整模板库
    ├── privacy-scan.md               # 五重深度隐私与环境安全扫描指南
    ├── community-templates.md        # GitHub 2026 社区文件库与 CI 模板
    ├── release-and-distribution.md   # 全渠道现代分发与发版实操指南
    ├── description-guide.md          # Description 与 Topics 标签优化指南
    ├── discovery-and-promotion.md    # 开源发现、Launch Kit 与推广策略
    ├── mcp-push-guide.md             # GitHub 推送与授权指引
    ├── pr-and-release-workflow.md    # PR、CI 与发布门禁
    ├── github-pat-setup.md           # GitHub PAT 配置指南
    └── github-pat-comparison.md      # GitHub PAT 权限类型对比
```

---

---

## 🌐 GitHub 开源全生命周期协作矩阵 (Open Source Lifecycle Suite)

面向独立开发者与开源团队的完整工具链闭环：

| 阶段 / 角色 | 推荐技能 | 核心使命与能力 | GitHub 仓库 |
|---|---|---|---|
| 📦 **开源前准备** | [**`github-oss-prep`**](https://github.com/hyt315/github-oss-prep) | 自动化生成规范门面、中英双语 README、CI 工作流、社区资产与合规审计 | [hyt315/github-oss-prep](https://github.com/hyt315/github-oss-prep) |
| 🩺 **质量体检** | [**`skill-doctor`**](https://github.com/hyt315/skill-doctor) | 50+ 项工业级静态规则 + 动态实跑自测（结论均可用命令复核） | [hyt315/skill-doctor](https://github.com/hyt315/skill-doctor) |
| ⚙️ **开源后运营** | [**`github-oss-ops`**](https://github.com/hyt315/github-oss-ops) | 智能分流 Issue、AI 垃圾防御、PR 辅助审查、GHSA 私有漏洞协同与发版全渠道广播 | [hyt315/github-oss-ops](https://github.com/hyt315/github-oss-ops) |
| 🚀 **贡献者导航** | [**`github-oss-contribute`**](https://github.com/hyt315/github-oss-contribute) | 面向贡献者的全程向导：Fork 同步、Rebase 冲突消解、DCO 签名、反 AI Slop 质量门禁 | [hyt315/github-oss-contribute](https://github.com/hyt315/github-oss-contribute) |

---

## ❓ 常见问题 (FAQ)

- **Q: 整理和打包需要 GitHub Token 吗？**  
  A: 不需要。项目扫描、隐私检查、规范补齐、README 生成与源码 ZIP 打包均在本地完成，只有最终向 GitHub 推送时才需要授权。
- **Q: 它会擅自修改我的现有代码吗？**  
  A: 绝对不会。本技能坚持“先审后改”原则，仅在用户明确批准后才创建或修改文件。
- **Q: 我的项目不是 AI 技能，也能使用吗？**  
  A: 完全可以。内置十大全景品类模板引擎，对 MCP Server、AI 模型权重、CLI 工具、浏览器扩展、类库 SDK、IaC 配置与 Web 应用均有深度针对性支持。
- **Q: 为什么技能主干 `SKILL.md` 能够保持轻量？**  
  A: 技能严格遵循渐进式披露架构，将各领域的详细模板下沉到 `references/` 独立模块中，避免 AI 上下文过载与交叉污染。

---

## ⚠️ 已知限制

按本技能自己的"§9 已知限制"标准，如实列出它做不到的事：

- **不验证运行期行为**：它整理文件、扫描凭据、检查链接与版本一致性，但**不会**真的安装你的包或跑你的测试；"干净环境跑通"这一步必须你（或 CI）来做。
- **不扫历史与远程**：默认只扫工作树。要查提交历史里的凭据，需另行运行 `gitleaks`/`trufflehog`（本技能文档已点名它们，但未内建）。
- **分类有边界**：主表当前 12 类；桌面 App、移动 App、硬件、游戏、研究复现等**没有专属骨架**，此时按底座 12 节 + 品类增量写，并在事实卡标 `template=missing`，不会硬套模板冒充专属。
- **凭据检测有盲区**：规则是模式匹配（`scripts/secret-rules.json`），不是高熵检测；自定义格式或已泄露进历史的密钥仍可能漏，故所有豁免会以 P2 明示、发布前仍需人工复核。
- **许可建议不是法律意见**：分许可表帮你想清"什么资产配什么许可"，重大选择请找法务；模型/数据类还需自行确认上游许可链。
- **发布不越权**：远程推送、Tag、Release、对外推广各需单独授权；本技能不会自己替你发布。

## 🆘 支持

卡住了：先查 [Issues](https://github.com/hyt315/github-oss-prep/issues) 与 [Discussions](https://github.com/hyt315/github-oss-prep/discussions)（提问请到 Discussions），提交时请附可复现步骤与你跑的那条命令。响应节奏见 [SECURITY.md](SECURITY.md)（漏洞）与 [SUPPORT.md](SUPPORT.md)（一般问题）。

## 🤝 参与贡献

欢迎提交 Issue 与 Pull Request！详见 [CONTRIBUTING.md](CONTRIBUTING.md)。如果这个技能对你有帮助，欢迎在 GitHub 上点个 [Star ⭐](https://github.com/hyt315/github-oss-prep/stargazers)！

---

## 📄 开源协议

本项目采用 [MIT 许可证](LICENSE) 开源。

详见 [CHANGELOG.md](CHANGELOG.md) 了解版本演进历史。

---

> 🌏 **English: [README.en.md](./README.en.md)**
