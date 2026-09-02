# 5 重深度隐私与环境安全扫描指南

> 核心原则：**在任何文件开源、提交、推送或打包前，彻底阻断敏感凭据、私有路径指纹、内部会话标记与环境污染**。

---

## 5 重深度安全扫描防御网

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 第 1 重: 敏感凭据深度扫描 (OpenAI, Anthropic, Gemini, GitHub PAT ghp_/github_pat_, SSH) │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 第 2 重: 机器指纹与私有路径扫描 (本地用户目录、私有工作区盘符、真实用户名)           │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 第 3 重: 私有 Agent 与内部会话标记扫描 (内部会话 UUID, 内部 Agent 名称, 私有环境别名) │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 第 4 重: Git 本地配置与凭据 URL 专项扫描 (.git/config Remote Token URL, Commit 历史)   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 第 5 重: 构建产物与缓存泄漏扫描 (__pycache__, node_modules, renders, .idea, .DS_Store) │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. 扫描规则与正则定义

### 1.1 凭据扫描规则
- OpenAI API Key: `sk-[A-Za-z0-9-_]{20,}`
- Anthropic API Key: `sk-ant-[A-Za-z0-9-_]{20,}`
- GitHub Classic PAT: `ghp_[A-Za-z0-9]{36}`
- GitHub Fine-Grained PAT: `github_pat_[A-Za-z0-9_]{82}`
- SSH 私钥头部: `-----BEGIN (?:RSA|OPENSSH|EC|DSA) PRIVATE KEY-----`

### 1.2 本地绝对路径与机器指纹规则
- Windows 个人主目录: `<user_home>` (skill-doctor: allow)
- 本地工作盘符路径: `(?:[D-Z]:\\[^\r\n]+)`
- Unix 个人主目录: `/home/[a-z0-9_-]+/` 或 `/Users/[a-z0-9_-]+/`

### 1.3 私有 Agent 会话标记规则
- 会话 UUID 指纹: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
- 私有内部环境/Agent 标记（如未公开的私有模型或内部测试代号）

### 1.4 Git Remote URL 凭据污染
- 检查 `.git/config` 中的 `url = https://...` 是否包含嵌入的 Token（如 `https://<token>@github.com`）。
- **治理**：必须使用不带 Token 的纯净 URL：`https://github.com/<owner>/<repo>.git`。

### 1.5 垃圾构建产物拦截清单
- Python: `__pycache__/`, `*.pyc`, `.pytest_cache/`, `.venv/`
- Node.js: `node_modules/`, `.next/`, `.turbo/`, `renders/`
- 系统与 IDE: `.DS_Store`, `Thumbs.db`, `.idea/`, `.vscode/settings.json` (若含本地路径)

---

## 2. 标准脱敏占位符库

| 敏感类型 | 错误示例 (严禁提交) | 标准脱敏占位符 (合规) |
|---|---|---|
| **API 密钥** | `sk-proj-abc12345...` | `your_api_key_here` 或 `YOUR_API_KEY` |
| **GitHub 仓库所有者** | 私有调试账号 | `<owner>` 或 `{owner}` |
| **本地安装路径** | `D:\skills\my-skill` | `~/.claude/skills/<repo>` 或 `~/.agents/skills/<repo>` |
| **电子邮箱** | 真实个人邮箱 | `username@example.com` |
| **服务器地址** | `192.168.1.100` | `127.0.0.1` 或 `example.com` |
