# GitHub 认证与凭据最小化指引

## 先探测，再选路

1. 平台是否提供**可实际完成操作的**官方 GitHub 连接器；
2. 是否存在已登录的 `gh`（`gh auth status --active`，只看状态）；
3. `github.com` / `api.github.com` 是否可达；
4. 是否已存在 `GITHUB_TOKEN` 环境变量（**只判断存在性，不读取内容**）。

按 `mcp-push-guide.md` 的判定表选择路径。**任何路径都不要**：请求或打印 token、把凭据写进 remote URL 并持久化、把凭据放进文件或提交、运行 `gh auth status --show-token`、为找凭据扫描用户主目录 / 编辑器配置 / MCP 配置。

## 本机事实（2026-09-19 复核）

- `gh` CLI **不存在**；
- `github.com` 直连被重置（TLS 握手失败），git 推送需代理 `http://127.0.0.1:7897`；
- `api.github.com` 直连稳定可用（REST 建仓 / 设置元数据 / 回读验证走它）；
- token 位于 **User 级环境变量 `GITHUB_TOKEN`**，通过 PowerShell 读取到 shell 变量后一次性使用，用完 `GH=` 清空。

## 一次性使用原则

一次推送的完整形态：`git -c http.proxy=<proxy> push "https://$GH@github.com/{owner}/{repo}.git" main`。要点：**不** `git remote set-url`（避免 token 固化到 `.git/config`）；命令回显由 git 自动脱敏；推送完成后立即清空变量。若所在组织要求更严格的凭据策略，改用短期凭据（GitHub App / OIDC），不要长期 PAT。

## PAT 选择（仅当用户明确需要）

| 场景 | 选择 | 理由 |
|---|---|---|
| 创建新仓库 + 推送自己的项目 | Fine-grained（含 Contents 读写 + Administration 建仓）或 Classic `repo` | 最小权限；Fine-grained 单仓授权更细 |
| 贡献**非成员**的公开仓库 | Classic PAT | Fine-grained 暂不支持该场景 |
| 需要访问 Packages / Checks API / 用户 Projects | Classic 或 GitHub App | Fine-grained 尚未覆盖（官方称非永久限制） |

上限与限制以官方个人访问令牌文档为准（每个用户 Fine-grained PAT 有数量上限，超限建议改用 GitHub App）；任何凭据一旦出现在提交或日志中，**先轮换吊销，再清理历史**。
