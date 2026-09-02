# 全渠道现代分发与发布实操指南

> 本指南详尽规范不同软件生态（npm / PyPI / Docker / Homebrew / Cargo / Go / Release 资产）的具体发版命令、配置文件与国内镜像加速方案。

---

## 目录

1. [各平台发版方式全景对照表](#1-各平台发版方式全景对照表)
2. [GitHub Release 预编译资产发布 (含 SHA-256 校验和)](#2-github-release-预编译资产发布-含-sha-256-校验和)
3. [npm 发布详解 (JavaScript / Node.js)](#3-npm-发布详解-javascript--nodejs)
4. [PyPI 发布详解 (Python)](#4-pypi-发布详解-python)
5. [Docker / OCI 镜像发布 (GitHub Packages / ghcr.io)](#5-docker--oci-镜像发布-github-packages--ghcrio)
6. [Homebrew 发布详解 (macOS / Linux)](#6-homebrew-发布详解-macos--linux)
7. [crates.io 发布详解 (Rust)](#7-cratesio-发布详解-rust)
8. [Go 模块发版规范](#8-go-模块发版规范)
9. [国内镜像加速与换源参考](#9-国内镜像加速与换源参考)

---

## 1. 各平台发版方式全景对照表

| 软件形态 | 优先分发渠道 | 次要 / 备用渠道 | 核心发版指令 | 配置文件要求 |
|---|---|---|---|---|
| **AI Agent 技能** | Agent 一句话自装<br>`gh skill install` | `git clone`<br>单文件 `curl -O .../SKILL.md` | `git tag vX.Y.Z && git push --tags` | `SKILL.md`<br>`manifest.json` |
| **系统 CLI / 独立工具** | GitHub Release 预编译包<br>（`.zip` / `.tar.gz` / `.exe`） | `winget` / `scoop` / `brew`<br>源码运行 | `gh release create vX.Y.Z ./dist/*` | `checksums.txt` (SHA-256) |
| **Node.js 库 / CLI** | npm 官方源 | npx 免安装运行<br>源码克隆 | `npm publish --access public` | `package.json`<br>`.npmignore` |
| **Python 库 / CLI** | PyPI 官方源 | wheel 文件离线安装 | `python -m build && twine upload dist/*` | `pyproject.toml` |
| **容器化服务** | GitHub Packages (`ghcr.io`) | Docker Hub | `docker push ghcr.io/{owner}/{repo}:{tag}` | `Dockerfile`<br>`compose.yml` |
| **Rust Crate** | crates.io | 源码编译安装 | `cargo publish` | `Cargo.toml` |
| **Go 模块** | Go proxy (`proxy.golang.org`) | 源码 `go install` | `git tag vX.Y.Z && git push origin vX.Y.Z` | `go.mod` |

---

## 2. GitHub Release 预编译资产发布 (含 SHA-256 校验和)

### 2.1 生成 SHA-256 校验和
在发布 Release 二进制前，必须为每个产物生成哈希校验和：

```powershell
# Windows PowerShell
Get-FileHash -Path "dist/*" -Algorithm SHA256 | ForEach-Object { "$($_.Hash)  $($_.Path | Split-Path -Leaf)" } | Out-File -Encoding utf8 dist/checksums.txt
```

```bash
# Linux / macOS
sha256sum dist/* > dist/checksums.txt
```

### 2.2 使用 GitHub CLI 一键发布
```bash
gh release create v1.0.0 --title "v1.0.0 - Initial Release" --notes "发布说明" ./dist/*.zip ./dist/*.tar.gz ./dist/checksums.txt
```

---

## 3. npm 发布详解 (JavaScript / Node.js)

### 3.1 检查 `package.json` 必备字段
```json
{
  "name": "my-tool",
  "version": "1.0.0",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "bin": {
    "my-tool": "./bin/cli.js"
  },
  "files": ["dist", "bin", "README.md", "LICENSE"],
  "publishConfig": {
    "access": "public"
  }
}
```

### 3.2 准备 `.npmignore`
排除测试夹具、源码与构建缓存：
```
src/
tests/
.github/
tsconfig.json
*.log
```

### 3.3 发布指令
```bash
# 1. 登录
npm login

# 2. 预检打包内容（不实际发布）
npm pack --dry-run

# 3. 正式发布
npm publish --access public
```

---

## 4. PyPI 发布详解 (Python)

### 4.1 配置文件 `pyproject.toml`
```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my-tool"
version = "1.0.0"
description = "My awesome tool"
readme = "README.md"
authors = [{ name = "Author", email = "author@example.com" }]
license = { text = "MIT" }
dependencies = []
requires-python = ">=3.10"
```

### 4.2 构建与上传
```bash
# 1. 安装构建工具
pip install --upgrade build twine

# 2. 构建源码包与 Wheel
python -m build

# 3. 校验产物
twine check dist/*

# 4. 上传到 PyPI (使用 API Token)
twine upload dist/*
```

---

## 5. Docker / OCI 镜像发布 (GitHub Packages / ghcr.io)

### 5.1 登录 GitHub Container Registry
```bash
echo $GITHUB_TOKEN | docker login ghcr.io -u <username> --password-stdin
```

### 5.2 构建并推送
```bash
# 构建镜像
docker build -t ghcr.io/<owner>/<repo>:1.0.0 -t ghcr.io/<owner>/<repo>:latest .

# 推送镜像
docker push ghcr.io/<owner>/<repo>:1.0.0
docker push ghcr.io/<owner>/<repo>:latest
```

---

## 6. Homebrew 发布详解 (macOS / Linux)

### 6.1 创建 Tap 仓库
创建名为 `homebrew-tap` 的 GitHub 仓库。

### 6.2 编写 Formula (`Formula/my-tool.rb`)
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

### 6.3 用户安装体验
```bash
brew install <owner>/tap/my-tool
```

---

## 7. crates.io 发布详解 (Rust)

```bash
# 1. 登录
cargo login <token>

# 2. 检查打包
cargo package

# 3. 正式发布
cargo publish
```

---

## 8. Go 模块发版规范

Go 通过 Git Tag 进行版本识别：
```bash
# 1. 打语义化 Tag 并推送
git tag v1.0.0
git push origin v1.0.0

# 2. 触发 Go proxy 缓存索引
GOPROXY=https://proxy.golang.org go list -m github.com/<owner>/<repo>@v1.0.0
```

---

## 9. 国内镜像加速与换源参考

在 README 或安装指南中，可为国内开发者提供换源提示：

| 生态 | 常用高速镜像源 | 换源命令 |
|---|---|---|
| **npm** | 淘宝 npmmirror | `npm config set registry https://registry.npmmirror.com` |
| **Python / pip** | 清华大学镜像源 | `pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple` |
| **Rust / Cargo** | 字节跳动 / 清华源 | 配置 `~/.cargo/config.toml` |
| **Homebrew** | 清华镜像 | 配置 `HOMEBREW_BREW_GIT_REMOTE` |
| **GitHub Release** | GitHub Proxy 加速 | `https://ghproxy.com/https://github.com/...` |
