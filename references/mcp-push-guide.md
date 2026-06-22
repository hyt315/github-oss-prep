# GitHub 推送指南

通过 MCP 工具或 curl + git 完成仓库创建和文件推送，支持自动发现本地 Token 配置。

## 目录

- [推送方案选择](#推送方案选择)
- [确认清单模板](#确认清单模板)
- [方案 A：MCP 工具推送](#方案-amcp-工具推送)
- [方案 B：curl + git 推送](#方案-bcurl--git-推送)
- [异常处理](#异常处理)
- [完成提示模板](#完成提示模板)

---

## 推送方案选择

| 方案 | 适用场景 | 说明 |
|------|----------|------|
| **方案 A：MCP 工具** | 已配置 GitHub MCP Server | 直接调用 `create_repository` + `push_files`，不接触 token |
| **方案 B：curl + git**（默认） | MCP 工具不可用或权限不足 | 读取 PAT，用 curl 创建仓库 + git push 推送 |

**优先尝试方案 A**：如果 Agent 能识别到 GitHub MCP 工具（`create_repository`、`push_files`），直接用 MCP 工具操作。MCP 工具调用失败时，回退到方案 B。

---

## 确认清单模板

在推送前，**必须**向用户展示以下清单并等待确认：

```
## 准备推送确认

### 仓库信息
- 仓库名：xxx
- 是否公开：public
- Description：xxx
- Topics：xxx, xxx, xxx

### 将推送的文件（N 个）
- [列出所有文件路径]
- ...

是否确认创建仓库并推送？
```

**用户明确回复「确认」「是」「好」后才执行下一步。不回复通过的不执行。**

---

## 方案 A：MCP 工具推送

如果宿主环境已配置 GitHub MCP Server，优先使用 MCP 工具完成操作，无需手动处理 token 和 git 命令。

### 检测 MCP 可用性

确认 Agent 能识别以下工具：

| 工具 | 功能 | 底层 API |
|------|------|----------|
| `create_repository` | 创建新仓库 | `POST /user/repos` |
| `push_files` | 批量推送多个文件 | Git Data API（创建 tree + commit） |
| `create_or_update_file` | 创建/更新单个文件 | Contents API |

> `push_files` 通过 Git Data API 一次性创建 tree + commit，适合批量推送整个项目。`create_or_update_file` 每次只操作一个文件，适合增量更新。

### 创建仓库

调用 `create_repository` 工具：

- `name`：仓库名
- `description`：仓库描述
- `private`：`false`（公开仓库）
- `autoInit`：`false`（不需要自动初始化 README）

### 推送文件

调用 `push_files` 工具：

- `owner`：GitHub 用户名
- `repo`：仓库名
- `branch`：`main`
- `files`：所有需要推送的文件路径和内容

如 `push_files` 失败（文件过多或权限不足），回退到方案 B。

### 设置 Topics 和 Description

通过 MCP 工具或 REST API 设置：

```bash
# Topics
curl -s -X PUT -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/repos/<owner>/<repo>/topics" \
  -d '{"names":["topic1","topic2"]}'

# Description（如创建仓库时未设置）
curl -s -X PATCH -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/repos/<owner>/<repo>" \
  -d '{"description":"<repo description>"}'
```

### 异常处理

| 错误 | 原因 | 处理 |
|------|------|------|
| MCP 工具不可用 | 宿主未配置 GitHub MCP Server | 回退到方案 B |
| `401 Bad credentials` | token 过期或无效 | 提示用户重新生成 PAT |
| `403 Forbidden` | token 权限不足 | 回退到方案 B，或提示用户检查 scope |
| `push_files` 超时/失败 | 文件过多或网络问题 | 回退到方案 B |
| `422 name already exists` | 仓库名已被占用 | 追加 `-oss` 或询问用户换名 |
| Token 找不到 | 用户未配置任何 MCP 或环境变量 | 引导用户参考 `github-pat-setup.md` 配置 |

---

## 方案 B：curl + git 推送

### 读取 Token

按以下策略自动发现 GitHub PAT（按优先级）：

**第一步：检查环境变量**

读取环境变量 `GITHUB_TOKEN`（如不存在则尝试 `GITHUB_PERSONAL_ACCESS_TOKEN`），用当前平台的合适方式读取：
- bash：`echo $GITHUB_TOKEN`
- PowerShell：`$env:GITHUB_TOKEN`

如有值，直接跳到验证步骤。

**第二步：自动发现 MCP 配置文件**

在用户主目录下搜索包含 GitHub MCP 服务器配置的 JSON 文件（搜索深度 3 层），用当前平台的合适工具：
- Windows：`Get-ChildItem -Path $HOME -Recurse -Depth 3 -Filter *.json`，然后筛选隐藏目录（以 `.` 开头）下的文件
- Linux/macOS：`find ~ -maxdepth 3 -name "*.json" -path "*/.*/*"`

搜索时匹配文件内容包含 `GITHUB_PERSONAL_ACCESS_TOKEN`、`github.*mcp` 或 `mcpServers.*github` 的 JSON 文件。

找到配置文件后，解析 JSON 并提取 Token。可用 Python 解析（兼容不同工具的 MCP 配置键名），将以下脚本保存为临时文件后用当前平台的 Python 执行（Linux/macOS 用 `python3`，Windows 用 `python`）：

```python
import json
d = json.load(open("<发现的配置文件路径>"))
# 兼容不同工具的 MCP 配置键名（mcpServers / servers / mcp）
for key in ('mcpServers', 'servers', 'mcp'):
    servers = d.get(key, {})
    if 'github' in servers:
        token = servers['github'].get('env', {}).get('GITHUB_PERSONAL_ACCESS_TOKEN', '')
        if token:
            print(token)
            break
```

**第三步：兜底参考路径**（不同工具路径各异，以下仅为常见示例）

| 路径 | 常见于 |
|------|--------|
| `~/.cursor/mcp.json` | Cursor |
| `~/Library/Application Support/Claude/claude_desktop_config.json` | Claude Desktop (macOS) |
| `%APPDATA%\Claude\claude_desktop_config.json` | Claude Desktop (Windows) |
| `~/.codeium/mcp_config.json` | Windsurf |
| `.vscode/mcp.json` | VS Code / GitHub Copilot（项目级） |
| `~/.trae/mcp.json` | Trae |

> **原则**：不依赖特定工具路径，优先通过自动发现找到配置。以上路径仅在自动发现失败时作为参考。

如所有方式都找不到，提示用户配置：见 `github-pat-setup.md`。

### 验证 Token

读取到 token 后，先验证有效性和权限：

```bash
curl -sI -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/user
```

从响应头中找到 `x-oauth-scopes` 字段（bash 可管道 `grep -i x-oauth-scopes` 过滤，PowerShell 可用 `| Select-String -Pattern x-oauth-scopes`）。

确认输出包含 `repo` scope。如不包含，提示用户重新生成 Classic PAT 并勾选 `repo` 权限。

> 推荐使用 Classic PAT（`ghp_` 前缀）。Fine-grained PAT（`github_pat_` 前缀）虽然也能创建仓库，但需要预配置权限范围且无法跨组织，开源发布场景下 Classic PAT 更省事。详见 `github-pat-comparison.md`。

### 创建仓库（如不存在）

```bash
curl -s -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/user/repos" \
  -d '{"name":"<repo-name>","description":"<description>","private":false,"auto_init":false}'
```

如返回 `name already exists`，仓库已存在，直接进入推送。

### git 推送

```bash
cd <project-dir>
```

检查项目目录是否已有 `.git` 目录（如不存在，需要先 `git init` 并将当前分支重命名为 main；如已存在，确保切换到 main 分支）：

```bash
git init
git branch -m main
```

配置提交者信息并提交：

```bash
git config user.name "<github-username>"
git config user.email "<github-id>+<username>@users.noreply.github.com"
git add -A
git commit -m "<commit message>"
```

处理 origin remote：先移除已存在的 origin（如不存在可忽略报错），再添加带 token 的 remote URL（将 `$GITHUB_TOKEN` 替换为实际读取到的 token 值），推送后立即移除 remote 以避免残留 token：

```bash
git remote remove origin
git remote add origin "https://$GITHUB_TOKEN@github.com/<owner>/<repo>.git"
git push -u origin main --allow-unrelated-histories
git remote remove origin
```

> 如带 `--allow-unrelated-histories` 的推送失败，改用普通推送：`git push -u origin main`。

### 设置 Topics 和 Description

```bash
# Topics
curl -s -X PUT -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/repos/<owner>/<repo>/topics" \
  -d '{"names":["topic1","topic2"]}'

# Description
curl -s -X PATCH -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/repos/<owner>/<repo>" \
  -d '{"description":"<repo description>"}'
```

### GitHub CLI 替代（已安装 gh 且已登录时可用）

如用户已安装 GitHub CLI 并完成 `gh auth login`（默认 scope 包含 `repo`，无需额外配置 Token），可将上述 curl 命令替换为：

```bash
# 创建仓库 + 推送（需先 git init + add + commit）
gh repo create <repo-name> --public -d "<description>" --source=. --push

# 设置 Topics
gh repo edit --add-topic "topic1" --add-topic "topic2"

# 设置 Description
gh repo edit -d "<description>"
```

---

## 异常处理

| 错误 | 原因 | 处理 |
|------|------|------|
| `401 Bad credentials` | token 过期或无效 | 提示用户重新生成 PAT |
| `403 Forbidden` | token 缺少 `repo` scope | 提示用户重新生成 Classic PAT 并勾选 `repo` |
| `404 Not Found` | API endpoint 错误或用户不存在 | 检查用户名和 API URL |
| `422 name already exists` | 仓库名被他人占用 | 追加 `-oss` 或询问用户换名 |
| `git push` 失败 | 文件未 staging 或分支冲突 | 检查 `git status`；如为历史冲突，使用 `--allow-unrelated-histories` |
| 文件超过 100 个 | GitHub API 限制 | 分 2 批推送，每批 ≤50 个 |
| MCP 配置文件无 github 条目 | 配置文件存在但未配置 GitHub MCP | 引导用户在配置文件中添加 github MCP 服务器 |
| Token 找不到 | 用户未配置任何 MCP 或环境变量 | 引导用户参考 `github-pat-setup.md` 配置 |

---

## 完成提示模板

```
## 推送完成
仓库地址：https://github.com/{owner}/{repo}
```
