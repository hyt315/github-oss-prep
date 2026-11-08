# GitHub 认证与凭据最小化指引

## 先探测，再选路

1. 平台是否提供**可实际完成操作的**官方 GitHub 连接器；
2. 是否存在已登录的 `gh`（`gh auth status --active`，只看状态）；
3. `github.com` / `api.github.com` 是否可达；
4. 是否已存在 `GITHUB_TOKEN` 环境变量（**只判断存在性，不读取内容**）。

按 `mcp-push-guide.md` 的判定表选择路径。**任何路径都不要**：请求或打印 token、把凭据写进 remote URL 并持久化、把凭据放进文件或提交、运行 `gh auth status --show-token`、为找凭据扫描用户主目录 / 编辑器配置 / MCP 配置。

## 常见环境与对应做法（按探测结果套用，不要照抄某台机器）

| 探测结果 | 做法 |
|---|---|
| 没有 `gh` | 用 REST API 建仓、设置元数据、回读验证；git 只负责推送 |
| `github.com` 直连失败、`api.github.com` 可达 | 推送时临时加代理：`git -c http.proxy=<proxy> push …`，`<proxy>` 由用户提供，不写进文件 |
| token 已在环境变量里 | 只判断"有没有"，读到 shell 变量后一次性使用，用完立即清空 |

## 一次性使用原则

推送时让 git 通过**临时凭据助手**向环境变量要 token，命令行参数里只出现变量名，不出现 token 本身（直接写进 `https://<token>@github.com/...` 会出现在进程列表和部分错误信息里）：

```bash
export GH_PUSH_TOKEN="$GH"        # 只在当前 shell 进程内
git -c credential.helper= \
    -c 'credential.helper=!f() { echo username=x-access-token; echo "password=$GH_PUSH_TOKEN"; }; f' \
    push https://github.com/{owner}/{repo}.git main
unset GH_PUSH_TOKEN GH
```

要点：第一个空的 `credential.helper=` 屏蔽系统已配置的凭据管理器，避免 token 被它存下；**不** `git remote set-url`（避免 token 固化到 `.git/config`）；推送完成后立即 `unset`。若所在组织要求更严格的凭据策略，改用短期凭据（GitHub App / OIDC），不要长期 PAT。

## PAT 选择（仅当用户明确需要）

| 场景 | 选择 | 理由 |
|---|---|---|
| 创建新仓库 + 推送自己的项目 | Fine-grained（含 Contents 读写 + Administration 建仓）或 Classic `repo` | 最小权限；Fine-grained 单仓授权更细 |
| 贡献**非成员**的公开仓库 | Classic PAT | Fine-grained 暂不支持该场景 |
| 需要访问 Packages / Checks API / 用户 Projects | Classic 或 GitHub App | Fine-grained 尚未覆盖（官方称非永久限制） |

上限与限制以官方个人访问令牌文档为准（每个用户 Fine-grained PAT 有数量上限，超限建议改用 GitHub App）；任何凭据一旦出现在提交或日志中，**先轮换吊销，再清理历史**。
