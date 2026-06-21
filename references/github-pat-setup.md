# GitHub PAT 配置指南

如果推送时找不到 Token，引导用户按以下步骤配置。

> Fine-grained PAT 与 Classic PAT 的能力对比和限制分析见 `github-pat-comparison.md`。

---

## 目录

- [什么是 PAT](#什么是-pat)
- [第一步：生成 Classic PAT](#第一步生成-classic-pat)
- [第二步：配置到 MCP Server](#第二步配置到-mcp-server)
- [第三步：验证](#第三步验证)
- [常见问题](#常见问题)
- [安全提醒](#安全提醒)

---

## 什么是 PAT

PAT（Personal Access Token）是 GitHub 的个人访问令牌，用于替代密码进行 API 认证和 git 操作。GitHub 目前提供两种 PAT：

- **Classic PAT**（`ghp_` 前缀）：传统令牌，通过 scope 授权（如 `repo`），会授予你可访问的所有组织仓库 + 所有个人仓库的访问权，权限范围较宽
- **Fine-grained PAT**（`github_pat_` 前缀）：细粒度令牌，可限定到特定仓库、授予更精细的权限，安全性更高

> 本 Skill 推荐使用 **Classic PAT**，原因详见 `github-pat-comparison.md`。

---

## 第一步：生成 Classic PAT

1. 打开 https://github.com/settings/tokens/new （或直接访问 Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token）

2. 点击 **Generate new token (classic)**

3. 填写：
   - **Note**：`github-oss-prep`（备注名称，随意）
   - **Expiration**：选择过期时间（建议 90 天或 No expiration）
   - **Select scopes**：勾选 `repo`（完整仓库访问权限）

4. 点击 **Generate token**

5. **立即复制 token**（`ghp_` 开头的字符串），页面刷新后无法再次查看

---

## 第二步：配置到 MCP Server

根据你使用的 AI Agent 工具，将 PAT 配置到对应位置：

> 以下仅列出常见工具示例。如果你使用的是其他支持 MCP 的工具，找到它的 MCP 配置文件，按相同格式添加即可。

> **两种 MCP Server 可选：** GitHub 官方目前推荐使用 Docker 方式运行 `github/github-mcp-server`（活跃维护），原 npx 方式 `@modelcontextprotocol/server-github` 已停止维护但仍可使用。两种方式工具接口完全兼容，任选其一即可。

### Cursor

编辑 `~/.cursor/mcp.json`：

**方式一：Docker（推荐）**

```json
{
  "mcpServers": {
    "github": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN", "ghcr.io/github/github-mcp-server"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_你的token"
      }
    }
  }
}
```

**方式二：npx（备选，需安装 Node.js）**

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_你的token"
      }
    }
  }
}
```

### Claude Desktop

编辑配置文件（路径因系统而异）：

- macOS：`~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows：`%APPDATA%\Claude\claude_desktop_config.json`

**方式一：Docker（推荐）**

```json
{
  "mcpServers": {
    "github": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN", "ghcr.io/github/github-mcp-server"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_你的token"
      }
    }
  }
}
```

**方式二：npx（备选，需安装 Node.js）**

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_你的token"
      }
    }
  }
}
```

### Windsurf

编辑 `~/.codeium/mcp_config.json`：

**方式一：Docker（推荐）**

```json
{
  "mcpServers": {
    "github": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN", "ghcr.io/github/github-mcp-server"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_你的token"
      }
    }
  }
}
```

**方式二：npx（备选，需安装 Node.js）**

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_你的token"
      }
    }
  }
}
```

### Claude Code

编辑 `~/.claude/settings.json`，在 `mcpServers` 中添加：

**方式一：Docker（推荐）**

```json
{
  "mcpServers": {
    "github": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN", "ghcr.io/github/github-mcp-server"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_你的token"
      }
    }
  }
}
```

**方式二：npx（备选，需安装 Node.js）**

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_你的token"
      }
    }
  }
}
```

### VS Code / GitHub Copilot

在项目根目录创建或编辑 `.vscode/mcp.json`（项目级配置）：

**方式一：Docker（推荐）**

```json
{
  "servers": {
    "github": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN", "ghcr.io/github/github-mcp-server"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_你的token"
      }
    }
  }
}
```

**方式二：npx（备选，需安装 Node.js）**

```json
{
  "servers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_你的token"
      }
    }
  }
}
```

> 注意：VS Code 使用 `servers` 而非 `mcpServers` 作为顶层键名。

### 通用方式（环境变量）

如果以上都不适用，直接设置环境变量：

```bash
# Windows PowerShell
$env:GITHUB_TOKEN = "ghp_你的token"

# Linux / macOS
export GITHUB_TOKEN="ghp_你的token"
```

---

## 第三步：验证

配置完成后，验证 token 是否有效：

```bash
curl -sI -H "Authorization: token ghp_你的token" \
  https://api.github.com/user | grep -i x-oauth-scopes
```

输出应包含 `repo`，如：
```
x-oauth-scopes: repo, workflow
```

---

## 常见问题

| 问题 | 原因 | 解决 |
|------|------|------|
| token 生成后找不到 | Classic PAT 位置不对 | 确保在 "Tokens (classic)" 页面生成，不是 "Fine-grained tokens" |
| 403 Forbidden | scope 不够 | 重新生成 token，确保勾选了 `repo` |
| 401 Bad credentials | token 过期或被撤销 | 重新生成 |
| 创建仓库失败 | 用了 Fine-grained PAT | 改用 Classic PAT（Fine-grained 虽可创建仓库但权限配置繁琐，详见 `github-pat-comparison.md`） |
| Fine-grained PAT 能用吗 | Fine-grained 有功能缺口 | 本 Skill 推荐 Classic PAT，操作更简单 |
| PAT 被自动删除了 | GitHub 会清理一年未使用的 PAT | 重新生成，或定期使用以保持活跃 |
| `npx` 命令报错 | 没安装 Node.js | 先安装 Node.js（https://nodejs.org） |
| `docker` 命令报错 | 没安装 Docker Desktop | 安装 Docker Desktop（https://www.docker.com/products/docker-desktop），或改用 npx 备选方式 |

---

## 安全提醒

- PAT 等同于账号密码，**不要分享给任何人**
- **不要提交到公开仓库**（本技能的隐私扫描会检测这个）
- 推送完成后，git remote 中的 token 会被立即清除（`git remote remove origin`）
- 建议设置过期时间，定期轮换
- **GitHub 会自动删除一年未使用的 PAT**，长期不用的 token 需重新生成
