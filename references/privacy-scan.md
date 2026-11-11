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
│ 第 2 重: 机器指纹与私有路径扫描 (用户目录、盘符路径、本机代理端口、环境快照式表述)   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 第 3 重: 私有 Agent 与内部会话标记扫描 (内部会话 UUID, 内部 Agent 名称, 私有环境别名) │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 第 4 重: Git 凭据 URL 与提交历史扫描 (Remote Token URL, 历史提交, 提交邮箱)          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 第 5 重: 构建产物与缓存泄漏扫描 (__pycache__, node_modules, renders, .idea, .DS_Store) │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

**哪几重由脚本自动完成、哪几重要人工看**（如实标注，别把人工项当成已自动覆盖）：

| 重 | 自动化 | 命令 / 规则组 | 仍需人工 |
|---|---|---|---|
| 1 凭据 | ✅ | `validate_repo.py`：`credential_patterns`、`blocked_filenames` | 新格式或自定义格式的密钥 |
| 2 机器指纹与个人信息 | ✅ | `path_patterns`、`private_ip_patterns`、`local_env_patterns`、`personal_patterns`（个人邮箱、大陆手机号） | 文中提到的真实用户名、主机名、公司名；证件号、境外手机号 |
| 3 Agent 会话标记 | ❌ | 暂无规则 | 全部人工：会话 ID、内部 Agent 名、私有工作区别名 |
| 4 Git 凭据与历史 | ✅ | `validate_repo.py --history`（历史中新增的每一行 + 提交邮箱） | `.git/config` 的 remote URL：`git remote -v` 看一眼 |
| 5 构建产物与缓存 | ⚠️ 部分 | 扫描时跳过这些目录，但**不报错** | 用 `git ls-files` 确认它们没被提交 |

> 发布前用 `--strict --history` 运行：带真实用户名的路径、内网 IP、本机环境指纹、个人邮箱和手机号都是 P1，只有 `--strict` 才会让检查失败，且只针对**当前树**；历史里的 P1 只报告不阻断。盘符绝对路径（如 `D:\Projects\`）只作 P2 提示；`C:\Windows`、`C:\ProgramData` 等系统目录和 `<user>`、`YourName`、`%USERNAME%` 这类占位用户名不报。 <!-- scan-ignore: windows-absolute-path (示例路径) -->

---

## 2. 扫描规则与正则定义

### 2.1 凭据扫描规则（唯一真相源）

规则**不在本文件重复罗列**——全部定义在 `scripts/secret-rules.json`，由 `scripts/validate_repo.py` 与 `scripts/selftest.py` 共同加载，文档只描述覆盖范围：

- 凭据：GitHub Classic / Fine-grained PAT、OpenAI 系（含 `sk-proj-`/`sk-ant-`）、Anthropic、Stripe、AWS（`AKIA`/`ASIA`）、Google API Key、Hugging Face、npm、PyPI、Slack、SendGrid、Telegram、JWT、Azure 存储密钥、URL 内嵌凭据
- 私钥：PEM 私钥块（含无算法前缀的 PKCS#8）
- 路径与网络：Windows 用户目录（任意真实用户名，含非 ASCII；占位用户名除外）、Unix 家目录、WSL/挂载路径、RFC1918 私网 IP
- 个人信息：常见个人邮箱域（qq、163、126、foxmail、gmail、outlook 等）的地址、中国大陆手机号；提交邮箱属个人邮箱域时在历史扫描里升为 P1
- 本机环境：回环地址上的代理配置、代理客户端常用端口、"本机实测"类环境快照 <!-- scan-ignore: machine-specific-claim (规则说明本身) -->
- 文件名级拦截：`.env`、`.env.*`（`.env.example` 等模板除外）、`credentials.json`、`*.pem`、`*.key`、`*.p12`、`*.pfx`、`id_rsa`/`id_ed25519`/`id_ecdsa`/`id_dsa`
- 不读的文件：图片、压缩包、模型权重与数据文件（`.gguf`、`.safetensors`、`.parquet` 等）和超过 5 MB 的文件，后者会以 P2 列出

维护规则：新增或调整只改 `secret-rules.json`；`selftest.py::test_rules_single_source` 会阻止任何文件重复声明正则。

### 2.2 本地路径与机器指纹

覆盖范围见 2.1，正则只在 `scripts/secret-rules.json` 里。

### 2.3 私有 Agent 会话标记（人工检查，暂无规则）
- 会话 UUID、Conversation ID、未公开的内部模型或测试代号、Agent 的临时追踪目录；
- UUID 在正常代码里也很常见，自动规则误报太多，所以这一项靠人工判断。

### 2.4 Git Remote URL 凭据污染
- `validate_repo.py` 会读取 `.git/config`，`url = https://...` 里嵌入了 Token 即报 P0。
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
| `127.0.0.1:3000` / `localhost:8080` | ✅ **安全合规** | 项目自身的回环调试地址，公开安全 |
| `http.proxy=http://127.0.0.1:<代理端口>` | ❌ **环境泄露** | 作者自己的代理配置；回环地址外人连不上，但暴露了作者的网络环境，别人照抄也会失败 |

---

## 4. 常见误报与白名单处理

以下情况在扫描时属于安全内容，无需报错：
- `[YOUR_API_KEY]`、`<your-token>`、`YOUR_SECRET_TOKEN` —— 占位符；
- `example@example.com`、`user@domain.com` —— 示范邮箱；
- `localhost:3000`、`127.0.0.1` —— 项目自身的调试端口（**例外**：出现在代理配置里、或是 7890/7897/1080/10809 这类代理客户端常用端口时，按环境泄露处理）；
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
