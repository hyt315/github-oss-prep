# 5 重深度隐私与环境安全扫描指南

> 核心原则：**在任何文件开源、提交、推送或打包前，彻底阻断敏感凭据、私有路径指纹、内部会话标记与环境污染**。

---

## 目录

1. [5 重深度安全扫描防御网](#1-5-重深度安全扫描防御网)
2. [扫描规则与正则定义](#2-扫描规则与正则定义)
3. [什么是真正的泄露 vs 安全的引用 (实战比对表)](#3-什么是真正的泄露-vs-安全的引用-实战比对表)
4. [常见误报与白名单处理](#4-常见误报与白名单处理)
5. [标准脱敏占位符库](#5-标准脱敏占位符库)

---

## 1. 5 重深度安全扫描防御网

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 第 1 重: 敏感凭据深度扫描 (OpenAI, Anthropic, Gemini, GitHub PAT ghp_/github_pat_, SSH) │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 第 2 重: 机器指纹与私有路径扫描 (本地用户目录、私有工作区盘符、开发机用户名)           │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 第 3 重: 私有 Agent 与内部会话标记扫描 (内部会话 UUID, 内部 Agent 名称, 私有环境别名) │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 第 4 重: Git 本地配置与凭据 URL 专项扫描 (.git/config Remote Token URL, Commit 历史)   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 第 5 重: 构建产物与缓存泄漏扫描 (__pycache__, node_modules, renders, .idea, .DS_Store) │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. 扫描规则与正则定义

### 2.1 凭据扫描规则（唯一真相源）

规则**不在本文件重复罗列**——全部定义在 `scripts/secret-rules.json`，由 `scripts/validate_repo.py` 与 `scripts/selftest.py` 共同加载，文档只描述覆盖范围：

- 凭据：GitHub Classic / Fine-grained PAT、OpenAI 系（含 `sk-proj-`/`sk-ant-`）、Anthropic、Stripe、AWS（`AKIA`/`ASIA`）、Google API Key、Hugging Face、npm、PyPI、Slack、SendGrid、Telegram、JWT、Azure 存储密钥、URL 内嵌凭据
- 私钥：PEM 私钥块（含无算法前缀的 PKCS#8）
- 路径与网络：Windows 任意用户名（含非 ASCII）、Unix 家目录、WSL/挂载路径、RFC1918 私网 IP
- 文件名级拦截：`.env`（`.env.example` 除外）、`*.pem`、`*.key`、`*.p12`、`*.pfx`、`id_rsa*`

维护规则：新增或调整只改 `secret-rules.json`；`selftest.py::test_rules_single_source` 会阻止任何文件重复声明正则。

### 2.2 本地绝对路径与机器指纹规则（正则以 `scripts/secret-rules.json` 为准）
- Windows 个人主目录: `C:\\Users\\` <!-- scan-ignore: windows-user-profile-path (规则示例本身) -->
- 本地工作盘符路径: `(?:[D-Z]:\\[^\r\n]+)`
- Unix 个人主目录: `/home/[a-z0-9_-]+/` 或 `/Users/[a-z0-9_-]+/`

### 2.3 私有 Agent 会话标记规则
- 会话 UUID 指纹: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- 私有内部环境/Agent 标记（如未公开的私有模型或内部测试代号）

### 2.4 Git Remote URL 凭据污染
- 检查 `.git/config` 中的 `url = https://...` 是否包含嵌入的 Token（如 `https://<token>@github.com`）。
- **治理**：必须使用不带 Token 的纯净 URL：`https://github.com/{owner}/{repo}.git`。

### 2.5 垃圾构建产物拦截清单
- Python: `__pycache__/`, `*.pyc`, `.pytest_cache/`, `.venv/`
- Node.js: `node_modules/`, `.next/`, `.turbo/`, `renders/`
- 系统与 IDE: `.DS_Store`, `Thumbs.db`, `.idea/`, `.vscode/settings.json` (若含本地路径)

---

## 3. 什么是真正的泄露 vs 安全的引用 (实战比对表)

| 示例代码 / 文本 | 判断结果 | 原因与治理说明 |
|---|---|---|
| `sk-example1234567890abcdef...` <!-- scan-ignore: openai-style-key (示例字符串，非真实凭据) --> | ❌ **严重泄露** | 真实 API 密钥，必须彻底移除并立即在服务商后台吊销 |
| `export API_KEY="<placeholder_key>"`  | ✅ **安全合规** | 明确的占位符，用于指引用户填入自己的 Key |
| `git remote set-url origin https://ghp_xxx@github.com/...` | ❌ **严重泄露** | `.git/config` 中包含明文 Token，必须清理 |
| `git clone https://github.com/{owner}/{repo}.git` | ✅ **安全合规** | 纯净的标准 Git URL |
| `C:\Users\alice\Desktop\my-project` <!-- scan-ignore: windows-user-profile-path, windows-absolute-path (示例，非真实路径) --> | ❌ **环境泄露** | 包含开发者的真实 Windows 用户名与绝对路径 |
| `~/.claude/skills/<repo-name>` | ✅ **安全合规** | 跨平台相对主目录标准规范路径 |
| `192.168.1.100:8080` / `10.0.0.5` | ❌ **内部泄露** | 暴露了真实的内网 IP 拓扑 | <!-- scan-ignore: rfc1918-ip (示例，非真实内网) -->
| `127.0.0.1:3000` / `localhost:8080` | ✅ **安全合规** | 本机回环调试地址，公开安全 |

---

## 4. 常见误报与白名单处理

以下情况在扫描时属于安全内容，无需报错：
- `[YOUR_API_KEY]`、`<your-token>`、`YOUR_SECRET_TOKEN` —— 占位符；
- `example@example.com`、`user@domain.com` —— 示范邮箱；
- `localhost:3000`、`127.0.0.1` —— 本机标准调试端口；
- 正则表达式定义本身（如扫描工具自身的模式匹配代码）。

---

## 5. 标准脱敏占位符库

| 敏感类型 | 错误示例 (严禁提交) | 标准脱敏占位符 (合规) |
|---|---|---|
| **API 密钥** | `sk-proj-abc12345...` | `your_api_key_here` 或 `YOUR_API_KEY` |
| **GitHub 仓库所有者** | 私有调试账号 | `{owner}`（统一写法，勿写真实账号名） |
| **本地安装路径** | `D:\skills\my-skill` | `~/.claude/skills/{repo}` 或 `~/.agents/skills/{repo}` | <!-- scan-ignore: windows-absolute-path (示例路径) -->
| **电子邮箱** | 真实个人邮箱 | `username@example.com` |
| **服务器地址** | `192.168.1.100` | `127.0.0.1` 或 `example.com` | <!-- scan-ignore: rfc1918-ip (示例，非真实内网) -->
