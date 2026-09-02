# 全渠道现代分发与下载矩阵路由系统

> 本文档规范不同软件形态的下载链接、包管理器接入与 Release 校验和发布流程。

---

## 1. 多元化分发矩阵速查

| 软件形态 | 优先分发渠道 | 次要 / 备用渠道 | 必配安全与校验 |
|---|---|---|---|
| **AI Agent 技能** | 一句话 Agent 自装<br>`gh skill install` | `git clone`<br>单文件 `curl -O .../SKILL.md` | `manifest.json` 元数据<br>`SKILL.md` Frontmatter |
| **系统 CLI / 独立工具** | GitHub Release 预编译资产<br>（`.zip` / `.tar.gz` / `.exe`） | `winget` / `scoop` / `brew`<br>源码克隆 | **SHA-256 校验和 (`checksums.txt`)**<br>跨平台构建产物 |
| **类库 / 模块 SDK** | 官方包管理器 (`npm` / `pip` / `cargo`) | GitHub Release 源码包 | SemVer 版本锁定 (`lockfile`)<br>自动化 CI 发布 |
| **全栈应用 / Web 服务** | 1 键云部署 (Vercel / Railway)<br>Docker 镜像 (`ghcr.io`) | 源码克隆 + Docker Compose | `.env.example` 环境变量清单 |

---

## 2. 针对 AI Agent 技能的极速分发标准

README 中必须提供多层次的安装指引：

### 方式 A：Agent 一句话自装（最推荐）
```
请安装 <skill-name> 技能：克隆 https://github.com/<owner>/<repo>.git 到你的 skills 目录（如 ~/.claude/skills/<repo> 或 ~/.agents/skills/<repo>），并确认安装成功。
```

### 方式 B：GitHub CLI 2.90+ 一行命令
```bash
gh skill install <owner>/<repo> <skill-name> --agent claude-code --scope user
```

### 方式 C：多平台标准目录克隆
- **Claude Code**: `git clone https://github.com/<owner>/<repo>.git ~/.claude/skills/<repo>`
- **Codex**: `git clone https://github.com/<owner>/<repo>.git ~/.codex/skills/<repo>`
- **Cursor**: `git clone https://github.com/<owner>/<repo>.git ~/.cursor/skills/<repo>`
- **通用 Agents**: `git clone https://github.com/<owner>/<repo>.git ~/.agents/skills/<repo>`

---

## 3. 针对 CLI 与独立工具的 Release 资产与校验和规范

发布 GitHub Release 时，必须随附 SHA-256 校验和文件：

### 3.1 生成 Checksums 校验和命令
```powershell
# Windows PowerShell 生成 SHA-256
Get-FileHash -Path "dist/*" -Algorithm SHA256 | ForEach-Object { "$($_.Hash)  $($_.Path | Split-Path -Leaf)" } | Out-File -Encoding utf8 dist/checksums.txt
```

### 3.2 用户端校验指引（写入 README）
```powershell
certutil -hashfile <downloaded_file> SHA256
```
