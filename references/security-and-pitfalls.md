# 安全底线、隐私扫描与高频避坑

> 核心原则：**任何公开、提交、推送或打包前，先由脚本做确定性扫描，再人工复核脚本盲区；发现 P0 立即阻断。**

## 1. 自动化扫描范围 vs 人工复核盲区

规则的唯一真相源是 `scripts/secret-rules.json`，文档不重复罗列正则。统一运行：

```bash
python scripts/validate_repo.py <项目目录> --strict --history
```

- **脚本自动拦截（P0 阻断）**：主流云与平台凭据（GitHub PAT、OpenAI/Anthropic/Google/AWS/HF/npm/PyPI/Slack/Stripe/Telegram/JWT/Azure）、PEM 私钥块、URL 内嵌凭据、`.git/config` 含 token 的 remote URL、敏感文件名（`.env`、`.env.*`、`credentials.json`、`*.pem`、`*.key`、`id_rsa`/`id_ed25519` 等，`.env.example` 等模板除外）、公开文档里未替换的 `{owner}`/`{repo}`。
- **脚本自动告警（`--strict` 阻断当前树 P1，历史 P1 仅报告）**：含真实用户名的本机路径（自动忽略 `<user>`、`YourName`、`%USERNAME%`、`Public` 等占位与系统目录）、RFC1918 私网 IP、本机代理配置与常见代理端口、「在我电脑上实测」类环境快照、个人邮箱（qq/163/gmail 等）与大陆手机号、已提交进 git 的构建缓存目录（`__pycache__`、`node_modules`、`dist` 等）、坏掉的 Markdown 相对链接、不安全的 GitHub Actions 配置。
- **脚本无法自动覆盖（必须人工看一眼）**：
  - 自定义格式或无固定前缀的私有密钥、高熵随机串（高敏项目建议追加 `gitleaks git` 或 `trufflehog`）；
  - AI 编程工具的会话 ID、内部工作区别名、隐藏临时目录（`.doctor/`、`.system_generated/` 等）；
  - 正文里手写的真实姓名、公司内网域名、境外手机号或证件号；
  - 第三方代码、字体、图片与数据集的再分发许可链。

**行内豁免**：确为教学或示例字符串时，可在该行末尾加 `<!-- scan-ignore: <rule-id> (<原因>) -->`。所有豁免都会作为 `P2` 在报告中显式列出，方便复核。

## 2. 高频致命坑与处置

### 2.1 Git 历史凭据残留（「删了文件 ≠ 安全」）
- `git rm` 不会抹掉 `.git/objects` 里的历史快照，一旦公开，爬虫与扫描器会在数分钟内发现旧凭据。
- **处置顺序**：① 立刻在对应平台**轮换并吊销**凭据 → ② 经用户确认后用 `git-filter-repo` 或 BFG 清理历史（禁用过时的 `git filter-branch`）→ ③ 强推后通知协作者重新克隆。
- **提交邮箱隐私**：提交前在仓库配置 `git config user.email "<id>+<user>@users.noreply.github.com"`，避免个人邮箱进入公开 commit 历史。

### 2.2 CI/CD 供应链安全（GitHub Actions）
- **显式声明只读权限**：在 workflow 顶层写 `permissions: { contents: read }`，仅在发版等必要 job 下局部放宽，禁止使用 `permissions: write-all` 或省略顶层声明。
- **锁定外部 Action 完整 40 位 SHA**：包括官方 `actions/*`，防止 tag 被篡改漂移；配合 Dependabot `github-actions` 生态自动滚版本（查询某 tag 的 SHA：`gh api repos/<owner>/<repo>/commits/<tag> --jq .sha`）。
- **警惕高危触发与脚本注入**：公开仓库避免用 `pull_request_target` 检出并运行 Fork 代码；严禁在 `run:` 中直接拼接 `${{ github.event.issue.title }}` 等不可信输入，必须先绑定到 `env:` 变量再以双引号 `$VAR` 引用。

### 2.3 开源许可证常见误区
- **无 LICENSE = 保留所有权利**：没有许可文件的公开代码，他人无权合法使用或分发。
- **代码 vs 非代码分清**：软件代码常用 MIT（简洁）或 Apache-2.0（含专利授权，企业与基础设施优选）；文档/课程/素材用 CC-BY-4.0 或 CC0；模型权重必须遵循上游基础模型许可链，切勿一律套 MIT。
- **强传染性与署名**：静态链接或嵌入 GPL/AGPL 代码会传染整个项目许可；使用 MIT/BSD 依赖或第三方素材时需保留原始版权声明与署名。

### 2.4 包注册中心版本不可变
- PyPI、npm、crates.io 等均禁止覆盖已发布的版本号。发版前先用 `uv build` / `npm pack` 检查产物清单，确认未打入 `.env` 或本地测试文件；优先用 OIDC Trusted Publishing 替代长期静态 Token。
