# Release + 多平台分发指南

GitHub 推送完成后，按本指南创建 Release 和发布到各包管理平台。

---

## 目录

- [GitHub Release 详解](#github-release-详解)
- [各平台发布方式对照表](#各平台发布方式对照表)
- [npm 发布详解（JavaScript/Node.js）](#npm-发布详解javascriptnodejs)
- [pip 发布详解（Python）](#pip-发布详解python)
- [Homebrew 发布详解（macOS/Linux）](#homebrew-发布详解macoslinux)
- [Docker 发布详解](#docker-发布详解)
- [crates.io 发布详解（Rust）](#cratesio-发布详解rust)
- [Go 模块发布](#go-模块发布)
- [推荐发布顺序](#推荐发布顺序)
- [国内镜像加速](#国内镜像加速)

## GitHub Release 详解

### 两种下载方式的区别

| 类型 | 来源 | 特点 |
|------|------|------|
| **源码下载** | GitHub 自动生成 | Code 按钮里的 ZIP/Tar，包含全部源码，用户需要自己编译 |
| **Release 下载** | 手动创建 Release | 上传编译好的文件（`.exe`/`.dmg`/`.whl` 等），用户下载即用 |

### 创建 Release 步骤

**方式一：GitHub CLI（推荐，一步完成 tag + release）**

如已安装 `gh` 并完成 `gh auth login`：

```bash
# 自动打 tag + 创建 release + 发布
gh release create v0.1.0 --title "v0.1.0 - Initial Release" --notes "首个版本"

# 附带编译产物
gh release create v0.1.0 --title "v0.1.0" --notes "首个版本" ./dist/*.exe ./dist/*.dmg
```

**方式二：手动流程**

1. 在项目目录打 tag 并推送：
```bash
git tag v0.1.0

# 由于 Step 5 推送后 origin 已被清除，需要临时添加 remote 推送 tag
git remote add origin "https://${GITHUB_TOKEN}@github.com/<owner>/<repo>.git"
git push origin v0.1.0
git remote remove origin
```

2. 去 GitHub 仓库 → Releases → Create a new release

3. 选择刚推的 tag，填写：
   - **Release 标题**：与 tag 一致，如 `v0.1.0 - Initial Release`
   - **说明**：改了什么、怎么安装
   - 可点击 "Generate release notes" 自动生成基于 PR 的说明

4. 如有编译产物，拖拽上传到 "Attach binaries" 区域

5. 点击 "Publish release"

### 语义化版本号（SemVer）

格式：`v主版本.次版本.修订号`

| 变更类型 | 版本影响 | 示例 |
|----------|----------|------|
| 破坏性变更（API 不兼容） | 主版本 +1 | `v2.0.0` |
| 新功能（向下兼容） | 次版本 +1 | `v1.1.0` |
| Bug 修复 | 修订号 +1 | `v1.0.1` |

### README 中的下载链接格式

**源码下载**（GitHub 自动生成）：
```markdown
| 方式 | 链接 |
|------|------|
| ZIP 源码 | `https://github.com/<owner>/<repo>/archive/refs/heads/<branch>.zip` |
| Tar 源码 | `https://github.com/<owner>/<repo>/archive/refs/heads/<branch>.tar.gz` |
| Release 最新版 | `https://github.com/<owner>/<repo>/releases/latest` |
```

> `<branch>` 必须替换为仓库的**实际默认分支名**（main 或 master，见仓库首页分支下拉框）；写错会导致 ZIP/Tar 链接 404。`git clone` 不受影响（自动使用默认分支）。

**编译产物下载**（Release 上传后）：
```markdown
| 平台 | 下载 |
|------|------|
| Windows | [下载 .exe](https://github.com/<owner>/<repo>/releases/download/v1.0.0/app.exe) |
| macOS | [下载 .dmg](https://github.com/<owner>/<repo>/releases/download/v1.0.0/app.dmg) |
| Linux | [下载 .AppImage](https://github.com/<owner>/<repo>/releases/download/v1.0.0/app.AppImage) |
```

---

## 各平台发布方式对照表

| 安装命令 | 发布到哪 | 需要什么文件 | 发布命令 |
|----------|----------|-------------|----------|
| `npm install xxx` | npmjs.com | `package.json` | `npm publish` |
| `npx xxx` | 同上（自动） | 同上 | 不需要额外操作 |
| `pip install xxx` | pypi.org | `pyproject.toml` 或 `setup.py` | `twine upload dist/*` |
| `brew install xxx` | Homebrew | Formula 文件（PR 提交） | PR 到 homebrew-core |
| `cargo install xxx` | crates.io | `Cargo.toml` | `cargo publish` |
| `docker pull xxx` | Docker Hub | `Dockerfile` | `docker push` |
| `go install xxx` | Go Proxy | `go.mod` | 打 tag 即可自动索引 |

---

## npm 发布详解（JavaScript/Node.js）

### 第一步：配置 package.json

确保 `package.json` 包含以下关键字段：

```json
{
  "name": "my-tool",
  "version": "1.0.0",
  "description": "一个工具",
  "main": "index.js",
  "bin": {
    "my-tool": "./bin/cli.js"
  },
  "files": ["dist", "bin"],
  "license": "MIT"
}
```

| 字段 | 说明 |
|------|------|
| `name` | 包名，全局唯一，先在 npmjs.com 搜一下有没有重名 |
| `bin` | 命令行工具必配，配了后用户能 `npx my-tool` 直接用 |
| `files` | 只发布这些文件到 npm，不写则发布全部（排除 `.gitignore` 里的） |

### 第二步：发布

```bash
npm login          # 登录 npm 账号
npm publish         # 发布
```

### 更新版本

```bash
npm version patch   # 1.0.0 -> 1.0.1（修 Bug）
npm version minor   # 1.0.0 -> 1.1.0（新功能）
npm version major   # 1.0.0 -> 2.0.0（破坏性变更）
npm publish
```

---

## pip 发布详解（Python）

### 第一步：创建 pyproject.toml

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my-tool"
version = "1.0.0"
description = "一个工具"
license = "MIT"
requires-python = ">=3.8"

[project.scripts]
my-tool = "my_tool.cli:main"
```

### 第二步：构建并发布

```bash
pip install build twine
python -m build
twine upload dist/*
```

需要先在 pypi.org 注册账号。发布后用户就能 `pip install my-tool`。

---

## Homebrew 发布详解（macOS/Linux）

Homebrew 有两条路：

### 方式一：提交到官方 homebrew-core（推荐）

用户可以直接 `brew install xxx`，但需要审核。

1. 项目需要先有 GitHub Release（带编译好的二进制文件）
2. 写一个 Formula（Ruby 脚本，描述怎么下载和安装）
3. 提 PR 到 https://github.com/Homebrew/homebrew-core
4. 审核通过后用户就能 `brew install xxx`

### 方式二：创建自己的 Tap（不需要审核）

1. 创建 GitHub 仓库，命名为 `homebrew-xxx`
2. 在仓库里放 Formula 文件
3. 用户通过 `brew tap 你的用户名/xxx` 添加后安装

---

## Docker 发布详解

### 第一步：写 Dockerfile

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --production
COPY . .
CMD ["node", "index.js"]
```

### 第二步：构建并推送

```bash
docker build -t yourusername/my-tool:1.0.0 .
docker push yourusername/my-tool:1.0.0
```

需要先在 hub.docker.com 注册账号。发布后用户就能 `docker pull yourusername/my-tool`。

---

## crates.io 发布详解（Rust）

```bash
cargo login          # 登录 crates.io API Token
cargo publish         # 发布
```

需要先在 crates.io 生成 API Token。发布后用户就能 `cargo install xxx`。

---

## Go 模块发布

Go 最简单，不需要手动发布：

1. 确保 `go.mod` 中的模块路径正确（如 `github.com/owner/repo`）
2. 打 tag 并推送：`git tag v1.0.0 && git push origin v1.0.0`
3. Go Proxy 会自动索引，用户 `go install xxx` 即可

---

## 推荐发布顺序

不用一开始就全部搞定，按优先级来：

| 顺序 | 事项 | 说明 |
|------|------|------|
| 1 | 代码推到 GitHub | 源码下载自动有 |
| 2 | 写好 LICENSE + README + .gitignore | 开源三件套 |
| 3 | 创建第一个 Release | 上传编译好的文件（如有） |
| 4 | 发布到主语言的包管理器 | JS→npm，Python→PyPI，Rust→crates.io |
| 5 | 补全 CONTRIBUTING.md 和 Issue/PR 模板 | 吸引贡献者 |
| 6 | 用户量大了再加 | Homebrew、Docker、CI/CD、文档网站 |

---

## 国内镜像加速

发布后，国内用户访问可能慢，可提示用户使用镜像：

| 平台 | 镜像地址 |
|------|----------|
| npm | `npm config set registry https://registry.npmmirror.com` |
| PyPI | `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple` |
| Homebrew | `export HOMEBREW_API_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles/api"` |
