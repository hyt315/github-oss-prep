# 隐私扫描指南

推送前必须扫描所有文件，确认无敏感信息泄漏。

---

## 目录

- [扫描模式（正则）](#扫描模式正则)
- [什么是真正的泄露 vs 安全的引用](#什么是真正的泄露-vs-安全的引用)
- [常见误报](#常见误报)
- [扫描命令](#扫描命令)
- [处理原则](#处理原则)
- [GitHub 安全功能](#github-安全功能)

## 扫描模式（正则）

| 类别 | 正则/关键词 | 说明 |
|------|------------|------|
| **API Key / Token** | `api[_-]?key\|token\|secret\|password\|credential\|bearer\|authorization` | 所有文件扫描 |
| **真实邮箱** | `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` | 除 README 中的通用联系邮箱外 |
| **手机号** | `1[3-9]\d{9}` | 中国大陆手机号 |
| **身份证号** | `\d{17}[\dXx]` | 18 位身份证 |
| **用户名路径** | `C:\\Users\\[A-Za-z]+\|/Users/[A-Za-z]+\|/home/[A-Za-z]+` | 操作系统路径含真实用户名 |
| **私网 IP** | `192\.168\.\|10\.\|172\.(1[6-9]\|2[0-9]\|3[01])\.` | 内网地址 |
| **数据库连接串** | `mongodb://\|mysql://\|postgres://\|redis://` | 含密码的连接串 |
| **私有域名** | `\.local\|\.internal\|\.corp\|\.intranet` | 内网域名 |

---

## 什么是真正的泄露 vs 安全的引用

| 示例 | 判断 | 原因 |
|------|------|------|
| `C:\Users\YourName\.agent\skills\...` | ❌ 泄露 | 包含真实 Windows 用户名 |
| `C:\Users\YourName\AppData\Local\node.exe` | ❌ 泄露 | 个人计算机绝对路径 |
| `"args": ["-y", "obsidian-mcp", "你的Vault路径"]` | ✅ 安全 | 占位符，不是真实路径 |
| `需要配置 API Key` | ✅ 安全 | 是说明文字，不是实际 key |
| `sk-abc123def456` | ❌ 泄露 | 真实 API key |
| `username@users.noreply.github.com` | ⚠️ 需确认 | GitHub 默认 noreply 邮箱，看用户是否愿意公开 |
| `192.168.1.100:8080` | ❌ 泄露 | 私网 IP |

---

## 常见误报

- `[YOUR_API_KEY]`、`<your-token>`、`你的API密钥` — 占位符，安全
- `example@example.com` — 占位符，安全
- `localhost:3000` — 本地开发端口，安全
- `github.com/username` — 如果是项目公开作者的账号，安全

---

## 扫描命令

```bash
# 综合扫描（排除占位符）
grep -rn \
  -e "api[_-]?key\s*[:=]\s*['\"][a-zA-Z0-9]" \
  -e "sk-[a-zA-Z0-9]\{20,\}" \
  -e "ghp_[a-zA-Z0-9]\{30,\}" \
  -e "C:\\\\Users\\\\[A-Za-z]" \
  -e "/Users/[A-Za-z]" \
  -e "192\.168\.\|10\.\." \
  --include="*.md" --include="*.json" --include="*.yaml" --include="*.yml" \
  <project-dir> 2>/dev/null
```

实际使用中用 Grep 工具的 `pattern` 参数更高效。

---

## 处理原则

- **真正的泄露**（真实 key、真实路径、真实手机号）→ 必须删除或替换为占位符
- **README 中的公开联系邮箱** → 如果用户明确希望公开，可保留
- **占位符**（`your-key`、`xxx`）→ 不处理
- **用户自己的 GitHub 用户名** → 需要用户确认是否愿意在仓库名中出现

---

## GitHub 安全功能

### Private Vulnerability Reporting

GitHub 支持私密漏洞报告功能：
- **开启位置**：仓库 Settings → Security → Private vulnerability reporting
- **功能**：允许安全研究人员私密报告漏洞，而不是公开 Issue
- **推荐**：代码项目强烈建议开启

### SECURITY.md 最佳实践

**代码项目模板**：
```markdown
# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | ✅ |
| < 1.0   | ❌ |

## Reporting a Vulnerability

Please report security vulnerabilities to [security@example.com](mailto:security@example.com).

**Do NOT open a public issue for security vulnerabilities.**

We will acknowledge your report within 48 hours and provide a timeline for a fix.
```

**文档/方法论项目模板**：
```markdown
# Security Policy

This project is a documentation/methodology resource and does not contain executable code.

If you find any issues with the content, please open a [GitHub Issue](../../issues).
```
