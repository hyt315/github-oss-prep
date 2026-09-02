# 全渠道现代分发与发布实操指南

> 本指南详尽规范不同软件生态（AI Skills / MCP / HuggingFace / npm / PyPI / Docker / Homebrew / Cargo / Extensions / Helm / Release 资产）的具体发版命令、配置文件与国内镜像加速方案。

---

## 目录

1. [各生态发版方式全景对照表](#1-各生态发版方式全景对照表)
2. [AI 智能体与协议端发版 (Agent Skills & MCP Servers)](#2-ai-智能体与协议端发版-agent-skills--mcp-servers)
3. [AI 模型与数据集发布 (Hugging Face / ModelScope / Ollama)](#3-ai-模型与数据集发布-hugging-face--modelscope--ollama)
4. [Python 现代化 CLI 与库发布 (uv / PyPI)](#4-python-现代化-cli-与库发布-uv--pypi)
5. [Node.js 现代化 CLI 与库发布 (npm / npx / bunx)](#5-nodejs-现代化-cli-与库发布-npm--npx--bunx)
6. [浏览器扩展打包与发布 (Chrome Web Store / Edge Add-ons)](#6-浏览器扩展打包与发布-chrome-web-store--edge-add-ons)
7. [GitHub Release 预编译资产发布 (含 SHA-256 校验和)](#7-github-release-预编译资产发布-含-sha-256-校验和)
8. [Docker / OCI 镜像发布 (GitHub Packages / ghcr.io)](#8-docker--oci-镜像发布-github-packages--ghcrio)
9. [Homebrew 与 crates.io 发布 (macOS / Linux / Rust)](#9-homebrew-与-cratesio-发布-macos--linux--rust)
10. [国内镜像加速与换源参考](#10-国内镜像加速与换源参考)

---

## 1. 各生态发版方式全景对照表

| 软件形态 | 优先分发渠道 | 推荐现代命令 | 核心配置文件 |
|---|---|---|---|
| **AI Agent 技能** | Agent 一句话自装<br>`gh skill install` | `git clone` 到 skills 目录 | `SKILL.md`<br>`manifest.json` |
| **MCP Server 端** | npm / PyPI / npx | `npx -y {pkg}`<br>`uvx {pkg}` | `package.json`<br>`pyproject.toml` |
| **AI 模型 / 数据集** | Hugging Face / Ollama | `ollama run {repo}`<br>`hf download` | `Modelfile`<br>Model Card |
| **Python CLI / SDK** | PyPI (支持 `uvx` / `uv tool`) | `uvx {pkg}`<br>`uv tool install {pkg}` | `pyproject.toml` (`[project.scripts]`) |
| **Node CLI / SDK** | npm (支持 `npx` / `bunx`) | `npx {pkg}`<br>`bunx {pkg}` | `package.json` (`bin` 字段) |
| **浏览器扩展** | Chrome Web Store / Releases | 商店一键安装<br>解压离线载入 | `manifest.json` (MV3) |
| **系统 CLI / 独立工具** | GitHub Release 预编译包<br>（`.zip` / `.tar.gz` / `.exe`） | `winget`<br>`scoop`<br>`brew` | `checksums.txt` (SHA-256) |
| **容器化服务** | GitHub Packages (`ghcr.io`) | `docker pull ghcr.io/{owner}/{repo}` | `Dockerfile`<br>`compose.yml` |
| **Rust 编译工具** | crates.io (支持 `cargo binstall`) | `cargo binstall {crate}` | `Cargo.toml` |

---

## 2. AI 智能体与协议端发版 (Agent Skills & MCP Servers)

### 2.1 Agent Skills 发版
- 保持 `SKILL.md` 与 `manifest.json` 版本一致；
- 打语义化 Git Tag（如 `v1.0.0`）并推送到 GitHub；
- 用户端直接通过一句话或 `gh skill install` 安装。

### 2.2 MCP Server 发版
- **Node.js 版**：在 `package.json` 中配置 `"bin": { "my-mcp": "./dist/index.js" }` 并执行 `npm publish --access public`；
- **Python 版**：在 `pyproject.toml` 中配置 `[project.scripts]` 并执行 `uv publish`。

---

## 3. AI 模型与数据集发布 (Hugging Face / ModelScope / Ollama)

### 3.1 上传到 Hugging Face
```bash
# 1. 登录
huggingface-cli login

# 2. 上传模型权重与 GGUF
huggingface-cli upload <username>/<model-name> ./models/model-q4_k_m.gguf .
```

### 3.2 发布到 Ollama
```bash
# 编写 Modelfile (FROM ./model-q4_k_m.gguf)
ollama create <username>/<model-name> -f Modelfile
ollama push <username>/<model-name>
```

---

## 4. Python 现代化 CLI 与库发布 (uv / PyPI)

```bash
# 1. 使用 uv 构建
uv build

# 2. 发布到 PyPI
uv publish --token <YOUR_PYPI_TOKEN>
```

---

## 5. Node.js 现代化 CLI 与库发布 (npm / npx / bunx)

```bash
# 1. 预检打包内容
npm pack --dry-run

# 2. 正式发布
npm publish --access public
```

---

## 6. 浏览器扩展打包与发布 (Chrome Web Store / Edge Add-ons)

1. 确保 `manifest.json` 符合 Manifest V3 规范；
2. 剔除开发依赖与测试文件，将源码根目录打包为 `.zip`：
```powershell
Compress-Archive -Path manifest.json, src, icons, popup -DestinationPath extension.zip
```
3. 登录 [Chrome 开发者信息中心](https://chrome.google.com/webstore/devconsole) 提交发布；
4. 将 `extension.zip` 作为 GitHub Release 资产提供离线下载。

---

## 7. GitHub Release 预编译资产发布 (含 SHA-256 校验和)

### 7.1 生成 SHA-256 校验和
```powershell
# Windows PowerShell
Get-FileHash -Path "dist/*" -Algorithm SHA256 | ForEach-Object { "$($_.Hash)  $($_.Path | Split-Path -Leaf)" } | Out-File -Encoding utf8 dist/checksums.txt
```

```bash
# Linux / macOS
sha256sum dist/* > dist/checksums.txt
```

### 7.2 一键发布 Release
```bash
gh release create v1.0.0 --title "v1.0.0 - Initial Release" --notes "发布说明" ./dist/*.zip ./dist/checksums.txt
```

---

## 8. Docker / OCI 镜像发布 (GitHub Packages / ghcr.io)

```bash
echo $GITHUB_TOKEN | docker login ghcr.io -u <username> --password-stdin
docker build -t ghcr.io/<owner>/<repo>:1.0.0 -t ghcr.io/<owner>/<repo>:latest .
docker push ghcr.io/<owner>/<repo>:1.0.0
docker push ghcr.io/<owner>/<repo>:latest
```

---

## 9. Homebrew 与 crates.io 发布 (macOS / Linux / Rust)

### 9.1 Homebrew Formula
```ruby
class MyTool < Formula
  desc "My awesome tool"
  homepage "https://github.com/<owner>/<repo>"
  url "https://github.com/<owner>/<repo>/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "abcdef1234567890..."
  license "MIT"

  def install
    bin.install "my-tool"
  end
end
```

### 9.2 crates.io
```bash
cargo publish
```

---

## 10. 国内镜像加速与换源参考

| 生态 | 常用高速镜像源 | 换源命令 |
|---|---|---|
| **npm** | 淘宝 npmmirror | `npm config set registry https://registry.npmmirror.com` |
| **Python / pip / uv** | 清华大学镜像源 | `pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple` |
| **Rust / Cargo** | 字节跳动 / 清华源 | 配置 `~/.cargo/config.toml` |
| **Homebrew** | 清华镜像 | 配置 `HOMEBREW_BREW_GIT_REMOTE` |
| **GitHub Release** | GitHub Proxy 加速 | `https://ghproxy.com/https://github.com/...` |
