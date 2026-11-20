# 发布、推送、发版与推广指引

> 本地整理、隐私扫描与打包不需要任何 GitHub 认证。仅在用户明确要求「现在发布到 GitHub」时执行以下探测与推送流程。

## 1. 只读环境探测与选路

推送前先执行只读探测，**严禁**扫描用户主目录/编辑器配置找 token，**严禁**打印或持久化 token：

```bash
gh --version 2>/dev/null || echo "no-gh"
curl -s -o /dev/null -w "api=%{http_code}\n" --max-time 10 https://api.github.com
curl -s -o /dev/null -w "web=%{http_code}\n" --max-time 10 https://github.com
python3 -c "import os; print('token-env=' + ('yes' if os.environ.get('GITHUB_TOKEN') else 'no'))"
```

按探测结果选路：
- **路径 B（首选）**：已有可用官方 GitHub 连接器，或 `gh auth status --active` 已登录 → 直接用连接器或 `gh` 建仓、推送、设置元数据。
- **路径 A（无 `gh` 但有 `GITHUB_TOKEN`）**：用 REST API 建仓与设置元数据 + Git 临时凭据助手推送（token 仅经环境变量与 stdin 传递，不进命令参数、不写 `.git/config`）。
- **路径 C（无认证或网络受限）**：打包干净源码 ZIP，附仓库 Description、Topics 和网页上传步骤交给用户。

## 2. 推送与元数据设置（必须回读核对）

### 路径 B：`gh` CLI
```bash
gh repo create {owner}/{repo} --public --source=. --remote=origin --push
gh repo edit {owner}/{repo} --description "<120字以内简介>" --add-topic topic-1 --add-topic topic-2
gh repo view {owner}/{repo} --json description,repositoryTopics,defaultBranchRef,visibility
```

### 路径 A：REST API + 一次性凭据助手
```bash
GH="$GITHUB_TOKEN"
PROXY=""   # 仅当 github.com 直连失败时向用户索取，不猜端口、不落盘
auth() { printf 'Authorization: Bearer %s\n' "$GH"; }

auth | curl -sS -X POST https://api.github.com/user/repos -H @- \
  -H "Content-Type: application/json" \
  --data-binary '{"name":"{repo}","description":"<one-liner>","private":false}'

export GH_PUSH_TOKEN="$GH"
git ${PROXY:+-c http.proxy="$PROXY"} -c credential.helper= \
  -c 'credential.helper=!f() { echo username=x-access-token; echo "password=$GH_PUSH_TOKEN"; }; f' \
  push https://github.com/{owner}/{repo}.git main

auth | curl -sS -X PUT https://api.github.com/repos/{owner}/{repo}/topics -H @- \
  -H "Content-Type: application/json" --data-binary '{"names":["topic-1","topic-2"]}'
unset GH GH_PUSH_TOKEN
```

### PAT 类型速查（仅用户主动询问时参考）
- **Fine-grained PAT（GitHub 官方推荐）**：单仓权限最小化（建仓与推送需 Contents 读写 + Administration）；但不支持跨组织、非成员公开仓库或部分 Packages/Checks API。
- **Classic PAT（`repo` scope）**：覆盖所有可访问仓库，风险更高，仅在 Fine-grained 存在功能缺口时使用。

## 3. 分支策略与 Release 规范

- **推送模式**：已有公开仓库或多人协作默认走 `public-safe`（短分支 → Draft PR → CI 通过 → 合并）；单人初始化或低风险改动经用户同意可用 `solo-fast` 直推。
- **SemVer 与 Changelog**：版本号遵循 `vMAJOR.MINOR.PATCH`（`0.y.z` 为初始开发期），说明按 Keep a Changelog 分类（Added / Changed / Fixed / Security）。
- **Tag ≠ Release**：推完 tag 后必须创建正式 GitHub Release 对象（`gh release create v1.0.0 --generate-notes`），并核对版本号、CHANGELOG、安装命令与 Release 标题一致。

## 4. 多生态分发速查（按需）

- **AI Agent Skill**：打 tag 发 Release 即可，用户通过「一句话发给 AI」或 `npx skills add {owner}/{repo}` 安装。
- **Python（PyPI）**：`uv build` 检查产物 → `UV_PUBLISH_TOKEN=... uv publish`（或配置 OIDC Trusted Publishing）。
- **Node.js（npm）**：`npm pack --dry-run` 检查产物 → `npm publish --access public`。
- **Hugging Face（模型/数据集）**：`hf auth login` → `hf upload {owner}/{repo} <local_path> <remote_path>`（数据集加 `--repo-type dataset`）。
- **容器镜像（GHCR）**：推送至 `ghcr.io/{owner}/{repo}`。
- **预编译二进制**：附 `sha256sum` 生成的 `checksums.txt` 上传至 GitHub Release 资产。

## 5. 可选：对外推广（仅在用户需要推广时启用）

先确保陌生人按 README 能在 5 分钟内跑通，再选目标用户真实活跃的 **2–3 个渠道**改写发布，不复制粘贴同一条硬广：
- **开发者 / Agent 用户**：GitHub Topics、Show HN、相关生态 Discussions、V2EX、掘金。
- **创作者 / 非技术用户**：B 站、小红书、Product Hunt（突出前后对比与实操演示）。
- 准备 3 样素材即可：一句话价值、带真实演示图/输出的短帖、清晰的安装与反馈入口。
