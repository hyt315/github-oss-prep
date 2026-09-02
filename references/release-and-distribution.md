# 全渠道现代分发与发布实操指南

> 本指南详尽规范不同软件生态（uv / npm / PyPI / Docker / Homebrew / Cargo / Go / Release 资产）的具体发版命令、配置文件与国内镜像加速方案。

---

## 目录

1. [各平台发版方式全景对照表](#1-各平台发版方式全景对照表)
2. [Python 现代化 CLI 发版 (uvx / uv tool / pipx / PyPI)](#2-python-现代化-cli-发版-uvx--uv-tool--pipx--pypi)
3. [JavaScript / TypeScript 现代 CLI 发版 (npx / pnpm dlx / bunx / npm)](#3-javascript--typescript-现代-cli-发版-npx--pnpm-dlx--bunx--npm)
4. [GitHub Release 预编译资产发布 (含 SHA-256 校验和)](#4-github-release-预编译资产发布-含-sha-256-校验和)
5. [Docker / OCI 镜像发布 (GitHub Packages / ghcr.io)](#5-docker--oci-镜像发布-github-packages--ghcrio)
6. [Homebrew 发布详解 (macOS / Linux)](#6-homebrew-发布详解-macos--linux)
7. [crates.io 发布详解 (Rust & cargo binstall)](#7-cratesio-发布详解-rust--cargo-binstall)
8. [Go 模块发版规范](#8-go-模块发版规范)
9. [国内镜像加速与换源参考](#9-国内镜像加速与换源参考)

---

## 1. 各平台发版方式全景对照表

| 软件形态 | 优先分发渠道 | 推荐现代命令 | 核心配置文件 |
|---|---|---|---|
| **AI Agent 技能** | Agent 一句话自装<br>`gh skill install` | `git clone` 到 skills 目录 | `SKILL.md`<br>`manifest.json` |
| **Python CLI 工具** | PyPI (支持 `uvx` / `uv tool`) | `uvx {pkg}`<br>`uv tool install {pkg}` | `pyproject.toml` (`[project.scripts]`) |
| **Node CLI 工具** | npm (支持 `npx` / `bunx`) | `npx {pkg}`<br>`bunx {pkg}` | `package.json` (`bin` 字段) |
| **系统 CLI / 独立工具** | GitHub Release 预编译包<br>（`.zip` / `.tar.gz` / `.exe`） | `winget`<br>`scoop`<br>`brew` | `checksums.txt` (SHA-256) |
| **容器化服务** | GitHub Packages (`ghcr.io`) | `docker pull ghcr.io/{owner}/{repo}` | `Dockerfile`<br>`compose.yml` |
| **Rust 编译工具** | crates.io (支持 `cargo binstall`) | `cargo binstall {crate}` | `Cargo.toml` |
| **Go 模块** | Go proxy (`proxy.golang.org`) | `go install {url}@latest` | `go.mod` |

---

## 2. Python 现代化 CLI 发版 (uvx / uv tool / pipx / PyPI)

### 2.1 在 `pyproject.toml` 中声明命令行入口
要想支持 `uvx <package>` 和 `uv tool install <package>`，必须在 `pyproject.toml` 中配置 `[project.scripts]`：

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my-cli-tool"
version = "1.0.0"
description = "Modern high-performance CLI utility"
readme = "README.md"
requires-python = ">=3.10"
dependencies = []

[project.scripts]
my-cli-tool = "my_cli_tool.main:entry_point"
```

### 2.2 构建与发布到 PyPI
```bash
# 1. 使用 uv 构建 (极速)
uv build

# 2. 上传到 PyPI
uv publish --token <YOUR_PYPI_TOKEN>

# 或者使用传统 twine
python -m build && twine upload dist/*
```

---

## 3. JavaScript / TypeScript 现代 CLI 发版 (npx / pnpm dlx / bunx / npm)

### 3.1 在 `package.json` 中声明 `bin` 字段
```json
{
  "name": "my-cli-tool",
  "version": "1.0.0",
  "bin": {
    "my-cli-tool": "./bin/index.js"
  },
  "files": ["dist", "bin", "README.md", "LICENSE"],
  "publishConfig": {
    "access": "public"
  }
}
```

### 3.2 发布与即时执行
发布后，全生态运行器将自动生效：
- `npx my-cli-tool`
- `pnpm dlx my-cli-tool`
- `bunx my-cli-tool`

---

## 4. GitHub Release 预编译资产发布 (含 SHA-256 校验和)

### 4.1 生成 SHA-256 校验和
```powershell
# Windows PowerShell
Get-FileHash -Path "dist/*" -Algorithm SHA256 | ForEach-Object { "$($_.Hash)  $($_.Path | Split-Path -Leaf)" } | Out-File -Encoding utf8 dist/checksums.txt
```

```bash
# Linux / macOS
sha256sum dist/* > dist/checksums.txt
```

### 4.2 使用 GitHub CLI 一键发布
```bash
gh release create v1.0.0 --title "v1.0.0 - Initial Release" --notes "发布说明" ./dist/*.zip ./dist/*.tar.gz ./dist/checksums.txt
```

---

## 5. Docker / OCI 镜像发布 (GitHub Packages / ghcr.io)

```bash
echo $GITHUB_TOKEN | docker login ghcr.io -u <username> --password-stdin
docker build -t ghcr.io/<owner>/<repo>:1.0.0 -t ghcr.io/<owner>/<repo>:latest .
docker push ghcr.io/<owner>/<repo>:1.0.0
docker push ghcr.io/<owner>/<repo>:latest
```

---

## 6. Homebrew 发布详解 (macOS / Linux)

```ruby
class MyTool < Formula
  desc "My awesome tool"
  homepage "https://github.com/<owner>/<repo>"
  url "https://github.com/<owner>/<repo>/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "abcdef1234567890..." # 使用 sha256sum 计算源码包哈希
  license "MIT"

  def install
    bin.install "my-tool"
  end
end
```

---

## 7. crates.io 发布详解 (Rust & cargo binstall)

```bash
# 发布到 Crates.io
cargo publish

# 用户支持极速下载预编译二进制
cargo binstall my-crate
```

---

## 8. Go 模块发版规范

```bash
git tag v1.0.0
git push origin v1.0.0
GOPROXY=https://proxy.golang.org go list -m github.com/<owner>/<repo>@v1.0.0
```

---

## 9. 国内镜像加速与换源参考

| 生态 | 常用高速镜像源 | 换源命令 |
|---|---|---|
| **npm** | 淘宝 npmmirror | `npm config set registry https://registry.npmmirror.com` |
| **Python / pip / uv** | 清华大学镜像源 | `pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple` |
| **Rust / Cargo** | 字节跳动 / 清华源 | 配置 `~/.cargo/config.toml` |
| **Homebrew** | 清华镜像 | 配置 `HOMEBREW_BREW_GIT_REMOTE` |
| **GitHub Release** | GitHub Proxy 加速 | `https://ghproxy.com/https://github.com/...` |
