# 品类 2：MCP Server 协议端 (Model Context Protocol) 完整模板

> 先读 [README 模板总纲](../readme-template.md) 的「前置事实清单」「通用底座 12 节」和「品类增量」表，再用本骨架。
> 只取与你项目相符的这一份，不要跨品类拼接。


````markdown
# 🔌 项目名称 MCP Server / Project MCP Server

<div align="center">

**专为 AI 助手打造的 Model Context Protocol 协议服务端 · 开箱即用 · 纯净安全**

[![License](https://img.shields.io/github/license/{owner}/{repo})](LICENSE)
[![npm version](https://img.shields.io/npm/v/{pkg-name}.svg)](https://www.npmjs.com/package/{pkg-name})
[![MCP Standard](https://img.shields.io/badge/MCP-2026%20Compliant-1f6feb)](https://modelcontextprotocol.io)

</div>

---

## 📖 这是什么？

这是一个基于 Model Context Protocol (MCP) 标准构建的服务端程序，向 Claude Desktop、Cursor、Cline、VS Code 等 AI 客户端暴露工具、资源与提示词模板。

<!-- 判据：本节之后必须能让人"连上"——安装 + 至少 1 家客户端配置 + 1 次成功调用的输出 -->
<!-- 边界：本类不含 Agent Skill（那是品类 1）；若同时提供 SKILL.md 封装，按 category-map 打 monorepo 旗标并写分产物入口表 -->

## 📥 安装与运行

| 运行时 | 命令 | 成功判据 |
|---|---|---|
| Node（推荐免装运行） | `npx -y {pkg-name}` | 进程启动并等待 stdio，无 `ERR_MODULE_NOT_FOUND` |
| Python（推荐免装运行） | `uvx {pkg-name}` | 同上，无 `ModuleNotFoundError` |
| 本地开发 | `npm run dev` | 变更后自动重载；见下节 Inspector 调试 |

---

## ⚙️ 客户端快速配置 (Configuration)

### 1. Claude Desktop 配置
在你的 `claude_desktop_config.json` 中加入：

```json
{
  "mcpServers": {
    "{server-name}": {
      "command": "npx",
      "args": ["-y", "{pkg-name}"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

### 2. Cursor / Cline / VS Code 配置
在 MCP 客户端配置中添加：
- **Name**: `{server-name}`
- **Transport**: `stdio`
- **Command**: `npx -y {pkg-name}`（Node）或 `uvx {pkg-name}`（Python）

---

## 🛠️ 暴露的能力清单 (Exposed Capabilities)

### 1. Tools (可执行工具列表)
<!-- 判据：必须写"出错时返回什么"与是否有副作用（写文件/发请求），否则调用方无法安全重试 -->
| 工具名称 | 输入参数 | 成功返回 | 错误语义与副作用 |
|---|---|---|---|
| `tool_name` | `{ query: string, limit?: number }` | `JSON` | 参数非法返回 `{error:{code:"invalid_input"}}`；无副作用 |

### 2. Resources (只读上下文资源)
| 资源 URI 模式 | MIME 类型 | 说明 |
|---|---|---|
| `{server-name}://data/status` | `application/json` | 实时状态数据源 |

### 3. Prompts (预设提示词模板)
| 模板名称 | 参数 | 说明 |
|---|---|---|
| `analyze_report` | `{ report_id: string }` | 自动生成深度分析提示词 |

---

## 🚀 本地调试与开发

```bash
# 启动开发模式 (stdio 管道)
npm run dev

# 使用 MCP Inspector 进行交互式调试
npx @modelcontextprotocol/inspector npx {pkg-name}
```
````
