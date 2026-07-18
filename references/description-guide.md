# Description 生成指南

仓库 Description 是 GitHub 搜索和「第一眼」理解项目的重要信息。写好后在 Step 5 通过已授权的官方 GitHub 连接器或 GitHub CLI 实际设置 Description 与 Topics，并从仓库回读验证；无认证时将两者作为明确的待办和可复制内容交给用户手动填写，不能只生成后跳过。

---

## 目录

- [编写规则](#编写规则)
- [按项目类型的模板与案例](#按项目类型的模板与案例)
- [禁用写法 vs 推荐写法](#禁用写法-vs-推荐写法)
- [Topics 标签推荐](#topics-标签推荐)

## 编写规则

| 规则 | 说明 |
|------|------|
| **字数** | 控制在 120 字以内（GitHub 上限 350，但 120 以内显示最佳） |
| **结构** | `一句话功能 + 目标用户/亮点` |
| **语言** | 中文项目 → 中文；国际项目 → 英文；混合受众 → 中英双语用 `\|` 分隔 |
| **关键词** | 包含 2-3 个用户可能搜索的词（如「行业研究」「Agent Skill」「AI 框架」） |
| **避免** | 不要写版本号（会过时）、不要写「一个用于…的项目」这种废话开头 |
| **Emoji** | 可选，1 个即可，放在开头 |

---

## 按项目类型的模板与案例

### Skill 项目

**结构**：`[Emoji] 功能一句话 | 英文关键词`

**案例**：
```
🏭 AI 行业研究框架：从零散信息建立结构化认知体系 | AI-powered industry research methodology for Agent Skills
```
```
🛠 GitHub 开源准备工具：一键补齐社区标准文件 + MCP 自动推送 | Auto-prepare repos for open source
```
```
📝 代码审查助手：自动检查 PR 中的安全漏洞和代码异味 | AI code reviewer for security & style
```

### 代码项目

**结构**：`[Emoji] 功能描述，亮点一句 | English one-liner`

**案例**：
```
⚡ 高性能 JSON 解析器，零依赖，比标准库快 3 倍 | Fast JSON parser, 3x faster than standard
```
```
🐳 一键部署工具：从 Dockerfile 到生产环境只需 30 秒 | Deploy from Docker to prod in 30s
```
```
🔍 命令行全文搜索工具，支持正则和模糊匹配 | CLI fuzzy search with regex support
```

### 文档/方法论项目

**结构**：`[Emoji] 内容主题：一句话价值 | English summary`

**案例**：
```
📖 产品经理面试题库：200+ 真题与答题框架 | PM interview playbook with 200+ questions
```
```
🎯 创业避坑指南：100 个真实失败案例的方法论提炼 | Startup failure patterns distilled
```
```
🏗 系统设计面试：从单机到分布式，10 个场景深度拆解 | System design interview deep dive
```

---

## 禁用写法 vs 推荐写法

| ❌ 禁用 | 问题 | ✅ 推荐 |
|---------|------|---------|
| `一个用于行业研究的项目` | 废话，0 信息量 | `AI 行业研究框架，5 步从零建立认知体系` |
| `This is a tool for doing research` | 不说明具体价值 | `Structured industry research with 5-phase methodology` |
| `v2.1.0 版本更新` | 版本号会过时 | 不要写版本号 |
| `基于 Python 开发的 XX 工具` | 技术栈优先，应该先讲功能 | `XX 工具：一行命令完成 YY` |
| `帮助你更好地 XX` | 太模糊 | `XX：3 步内完成 YY，节省 80% 时间` |

---

## Topics 标签推荐

同时建议 5-8 个 Topics（仓库页面 Topics 区域），用于分类和搜索发现：

| 项目类型 | 推荐 Topics |
|----------|-------------|
| Skill | `agent-skill` `ai-agent` `skill-md` `claude-code` `cursor` |
| 代码 | `python` `cli-tool` `json-parser` `performance` |
| 文档 | `playbook` `interview-prep` `methodology` |

### SEO 优化要点

**Description SEO 规则**：
- **以主要关键词开头**：GitHub 搜索算法优先匹配开头的词
- **提及平台/技术栈**：如 "for Kubernetes"、"built with Next.js"
- **包含用例场景**：如 "self-hosted"、"CLI tool"

**Topics 选择策略**：
- 必须包含与项目直接相关的**主要技术关键词**
- 可添加生态系统归属标签（如 `cncf`、`awesome-list`）
- 如果项目是为某技术构建但未添加标签，用户通过该关键词过滤时会找不到

**仓库命名 SEO**：
- 包含主要关键词（如 `auth`、`monitoring`）
- 可选包含框架名（如 `next`、`rails`）
- 保持简短、可读、与搜索一致

**示例对比**：
| 仓库名 | Description | Topics | SEO 评分 |
|--------|-------------|--------|----------|
| `my-tool` | A tool for doing things | `tool` | ⭐ |
| `kubernetes-auth-proxy` | Lightweight auth proxy for Kubernetes clusters | `kubernetes` `auth` `proxy` `security` `go` | ⭐⭐⭐⭐⭐ |
