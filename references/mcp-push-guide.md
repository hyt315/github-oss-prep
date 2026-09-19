# GitHub 推送指引（只读探测 → 选路 → 回读验证）

> 本文取代旧的"优先官方连接器 / MCP"写法：**先探测环境，再选路径**。不同机器的最优路径不同，把某一条当默认会在另一台机器上失败。
> 语言说明：参考文档以中文为主。English summary at the end.

---

## 0. 推送前只读探测（全部只读，不改任何状态）

```bash
gh --version 2>/dev/null || echo "no-gh"                       # 是否存在 GitHub CLI
curl -s -o /dev/null -w "api=%{http_code}\n" --max-time 10 https://api.github.com   # REST API 可达性
curl -s -o /dev/null -w "web=%{http_code}\n" --max-time 10 https://github.com       # git 传输域名可达性
python -c "import os;print('token-env=' + ('yes' if os.environ.get('GITHUB_TOKEN') else 'no'))"  # 只看是否存在，绝不打印值
```

**禁止**：为找凭据而扫描用户主目录、编辑器配置或 MCP 配置；打印任何 token 内容；运行 `gh auth status --show-token`。

| 探测结果 | 走哪条路 |
|---|---|
| 平台提供官方 GitHub 连接器，且它在本机**能完成一次真实操作**（如读取当前账号） | 路径 B（连接器） |
| 有已登录的 `gh` | 路径 B（CLI） |
| `gh` 不存在，且 `github.com` 直连被重置（`web=000`）但存在代理与 `GITHUB_TOKEN` | 路径 A（本机定稿路径）或直接移交同机 `github-upload` 技能 |
| 以上都不可用 | 路径 C（手工交付 ZIP + 元数据待办） |

> ⚠️ 若连接器弹"账号 + Token"表单或报"字符串绑定无效"，**立即停止重试**，改走路径 A/B，不要反复触发弹窗。

---

## 路径 A：REST API 建仓 + 代理推送（本机 2026-09-19 实测可用）

**环境快照（仅在探测结果与下列一致时套用）**：`gh` 不存在；`github.com` 直连被重置，推送需代理（示例 `http://127.0.0.1:7897`）；`api.github.com` 直连可用；token 位于 User 级环境变量 `GITHUB_TOKEN`。

```bash
GH=$(powershell -NoProfile -Command "[Environment]::GetEnvironmentVariable('GITHUB_TOKEN','User')" | tr -d '\r\n')
test -n "$GH" && echo "token 已取到（长度 ${#GH}）" || echo "未取到 token，改走路径 B/C"

# 1) 建仓（不存在才建；description 英文 ≤120 字符）
curl -X POST https://api.github.com/user/repos \
  -H "Authorization: Bearer $GH" -H "Content-Type: application/json; charset=utf-8" \
  --data-binary '{"name":"{repo}","description":"<english one-liner>","private":false}'

# 2) 推送：一次性 URL 内嵌 token（token 只存在于本次命令与 shell 变量）
git -c http.proxy=http://127.0.0.1:7897 push "https://$GH@github.com/{owner}/{repo}.git" main

# 3) 元数据：Description 用 PATCH；Topics 必须用 PUT
curl -X PATCH https://api.github.com/repos/{owner}/{repo} -H "Authorization: Bearer $GH" \
  -H "Content-Type: application/json; charset=utf-8" --data-binary '{"description":"..."}'
curl -X PUT https://api.github.com/repos/{owner}/{repo}/topics -H "Authorization: Bearer $GH" \
  -H "Content-Type: application/json; charset=utf-8" --data-binary '{"names":["a","b"]}'

# 4) 回读验证（不一致立即修，不得宣称完成）
curl -s https://api.github.com/repos/{owner}/{repo}/commits?per_page=1 | head -5

GH=   # 用完清空
```

要点：**不**执行 `git remote set-url`（token 不落盘）；不在聊天/文件/日志里回显 token；若推送被分支保护拦截，先按 `github-oss-prep-pitfalls.md` 的 ruleset 流程处理。

---

## 路径 B：官方连接器 / GitHub CLI（其他平台）

```text
gh auth status --active                      # 只查状态
gh repo create OWNER/REPO --public --source=. --remote=origin --push
gh repo edit OWNER/REPO --description "..." --add-topic topic-one --add-topic topic-two
gh repo view OWNER/REPO --json description,repositoryTopics,defaultBranchRef,visibility
```

连接器路径同理：先确认它绑定的账号与目标仓库，再创建/推送/设置元数据，最后回读比对。任何情况下都不要请求、读取或打印 token。

---

## 路径 C：无认证时的手工交付

交付：ZIP 包 + 可复制的 Description / Topics + 文件清单 + 隐私扫描结果 + 网页端创建仓库与上传步骤。把"远程未发布"如实标为待办，不要因此宣称整个开源准备工作失败。

---

## 与 `github-upload` 技能的关系

本机同时装有 `github-upload`（推送流程的定稿版：代理 + 一次性 URL + REST API，明确不用连接器、不弹登录窗）。当探测命中"路径 A"时，**推荐直接移交该技能执行推送**；两个技能对"是否允许一次性 URL 内嵌 token"的口径已统一为：**允许一次性使用、用完即清、永不落盘**。

---

## English summary

Probe first (connector availability, `gh`, network reachability, token env presence), then pick one of three paths: (A) REST API + proxy push with a one-time token-in-URL that is never persisted, (B) official connector or `gh` CLI, (C) manual ZIP handoff. After any publish, read repository metadata back and compare exact values. Never request, print, or store credentials; never scan the user's home directory, editor settings, or MCP configuration for tokens.
