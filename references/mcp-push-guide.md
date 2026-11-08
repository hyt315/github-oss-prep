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
| `gh` 不存在，`api.github.com` 可达，且已有 `GITHUB_TOKEN`（`github.com` 直连失败时需用户提供代理） | 路径 A（REST API + 一次性凭据推送） |
| 以上都不可用 | 路径 C（手工交付 ZIP + 元数据待办） |

> ⚠️ 若连接器弹"账号 + Token"表单或报"字符串绑定无效"，**立即停止重试**，改走路径 A/B，不要反复触发弹窗。

---

## 路径 A：REST API 建仓 + 一次性凭据推送

**适用条件**：没有可用的 `gh` 或连接器；`api.github.com` 可达；token 已在环境变量中。`github.com` 直连失败时，向用户要代理地址填入 `PROXY`，**不要**猜端口，也不要把代理写进任何文件。

```bash
GH="$GITHUB_TOKEN"   # Windows 上若 token 在 User 级环境变量：GH=$(powershell -NoProfile -Command "[Environment]::GetEnvironmentVariable('GITHUB_TOKEN','User')" | tr -d '\r\n')
test -n "$GH" && echo "token 已取到（长度 ${#GH}）" || echo "未取到 token，改走路径 B/C"
PROXY=""             # 仅当 github.com 直连失败时填写，例如 PROXY="<proxy>"
auth() { printf 'Authorization: Bearer %s\n' "$GH"; }   # 由 printf 内建命令经 stdin 交给 curl，不出现在进程参数里

# 1) 建仓（不存在才建；description 英文 ≤120 字符为宜）
auth | curl -sS -X POST https://api.github.com/user/repos -H @- \
  -H "Content-Type: application/json; charset=utf-8" \
  --data-binary '{"name":"{repo}","description":"<english one-liner>","private":false}'

# 2) 推送：git 通过临时凭据助手读取环境变量，命令行只出现变量名
export GH_PUSH_TOKEN="$GH"
git ${PROXY:+-c http.proxy="$PROXY"} -c credential.helper= \
  -c 'credential.helper=!f() { echo username=x-access-token; echo "password=$GH_PUSH_TOKEN"; }; f' \
  push https://github.com/{owner}/{repo}.git main

# 3) 元数据：Description 用 PATCH；Topics 必须用 PUT（整体替换）
auth | curl -sS -X PATCH https://api.github.com/repos/{owner}/{repo} -H @- \
  -H "Content-Type: application/json; charset=utf-8" --data-binary '{"description":"..."}'
auth | curl -sS -X PUT https://api.github.com/repos/{owner}/{repo}/topics -H @- \
  -H "Content-Type: application/json; charset=utf-8" --data-binary '{"names":["a","b"]}'

# 4) 回读验证（不一致立即修，不得宣称完成）
curl -s https://api.github.com/repos/{owner}/{repo} | grep -E '"(description|default_branch|visibility)"'
curl -s https://api.github.com/repos/{owner}/{repo}/commits?per_page=1 | grep -m1 '"sha"'

unset GH GH_PUSH_TOKEN   # 用完清空
```

要点：**不**执行 `git remote set-url`（token 不落盘）；空的 `credential.helper=` 先屏蔽系统凭据管理器，避免 token 被存下；不在聊天、文件、日志里回显 token；`-H @-` 需要 curl 7.55 及以上。若推送被分支保护或 ruleset 拦截，改走 PR，或请仓库管理员调整规则后再推。

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

## 与其他推送技能的关系

如果用户的环境里另有专门负责推送的技能，可以把 Step 5 的推送移交给它，但凭据口径必须一致：token 只经环境变量和临时凭据助手使用，不写进 URL、不落盘、不回显。本技能不依赖任何特定的同伴技能。

---

## English summary

Probe first (connector availability, `gh`, network reachability, token env presence), then pick one of three paths: (A) REST API plus a push through a one-shot credential helper that reads the token from an environment variable (never in the URL or argv; proxy only if the user supplies one), (B) official connector or `gh` CLI, (C) manual ZIP handoff. After any publish, read repository metadata back and compare exact values. Never request, print, or store credentials; never scan the user's home directory, editor settings, or MCP configuration for tokens.
