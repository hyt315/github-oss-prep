# 品类 4：系统与 CLI 诊断工具型 (CLI / System Utility) 完整模板

> 先读 [README 模板总纲](../readme-template.md) 的「前置事实清单」「通用底座 12 节」和「品类增量」表，再用本骨架。
> 只取与你项目相符的这一份，不要跨品类拼接。


````markdown
# 🛠️ 工具名称 / Tool Name

<div align="center">

**专治系统级疑难杂症 · 纯只读探测 · 毫秒级数据说话 · 零破坏安全保障**

[![License](https://img.shields.io/github/license/{owner}/{repo})](LICENSE)
[![Release](https://img.shields.io/github/v/release/{owner}/{repo}?sort=semver)](https://github.com/{owner}/{repo}/releases/latest)
[![Platform](https://img.shields.io/badge/Platform-Windows%2010%20%7C%2011-lightgrey)](#兼容性)
<!-- 判据：徽章链接必须指向本项目真实存在的小节（如 ## 兼容性）；无该小节就删掉链接，不要指向别人项目里未必存在的 SKILL.md -->

</div>

---

## 📖 痛点解构

<!-- 判据：恰好 3 条；每条 = 可观测现象 + 量化数字 + 用户代价 + 本工具用哪个输出证明；无数字即视为没写 -->
<!-- 反例："网络很慢，影响体验" —— 无观测、无量化、无证据 -->
描述 3 个典型疑难用户痛点（如开网页卡死 3 秒、上行吃满、休眠唤醒延迟）。

## 📊 分层架构流程图

```
[输入: 用户遇到系统变慢 / 故障]
                 │
      [第 1 层: 物理与硬件层诊断]
                 │
      [第 2 层: 协议与系统调度诊断]
                 │
      [第 3 层: 后台资源与瓶颈定位]
                 │
      [输出: 确凿毫秒级证据链 + 官方治理建议]
```

## 🎯 常见疑难杂症实战速查表

| 典型现象 | 根因分类 | 核心排查命令 | 官方治理方案 |
|---|---|---|---|
| **现象 1** | 根因 1 | `命令 1` | 解决对策 1 |
| **现象 2** | 根因 2 | `命令 2` | 解决对策 2 |

## 📺 一段真实输出（不是示意图）

<!-- 判据：必须是从终端直接复制的文本，含提示符与耗时；改动数字/路径也要保留真实形态 -->
```console
$ {tool} probe --latency --samples 40
sample  dns=18ms  tcp=9ms  tls=31ms  ttfb=44ms   (40/40 ok)
p50 ttfb=44ms   p95 ttfb=132ms   worst=287ms  @ 2026-09-19 12:04
→ 结论：TLS 握手抖动集中在代理侧（见 --verbose 的 handshake 明细）
```

## 🧭 我该用哪种安装方式

| 你的情况 | 选 |
|---|---|
| 只想跑一次、不想污染环境 | A（`uvx`）或 B（`npx`） |
| 要天天用、希望 `PATH` 里有命令 | A 的 `uv tool install` / B 的 `npm i -g` |
| 公司机器不能装东西、需离线 | D（下载 Release 预编译包 + 校验和） |
| 需要在 CI 里用 | D（固定版本号，勿用 `latest`/`main.zip`） |

---

## 兼容性

| 平台 | 状态 |
|---|---|
| Windows 10 / 11 | 已验证 |
| macOS / Linux | 未验证 |

<!-- 判据：只列你真的跑过的平台；没测过的写"未验证"而不是删掉该行 -->

## 📥 现代终端安装与运行方式 (按技术栈针对性选择)

### 选项 A：Python 现代环境运行 (推荐 uv / pipx)
```bash
# 🚀 uvx 免安装即时秒开 (最推荐)
uvx {pkg-name}

# 📦 uv tool 持久隔离安装
uv tool install {pkg-name}

# 传统 pipx 隔离安装
pipx install {pkg-name}
```

### 选项 B：Node.js / 前端环境运行
```bash
# 🚀 npx / pnpm / bun 免安装即时运行
npx {pkg-name}
pnpm dlx {pkg-name}
bunx {pkg-name}

# 全局安装
npm install -g {pkg-name}
```

### 选项 C：跨平台单行脚本直装（**先审后跑**，别直接把管道当默认姿势）
```bash
# Linux / macOS：先下载、看一眼、再执行；有条件就校验 SHA-256
curl -fsSL https://{domain}/install.sh -o install.sh && less install.sh && sh install.sh

# Windows PowerShell：同理先落盘审阅
irm https://{domain}/install.ps1 -OutFile install.ps1
Start-Process notepad install.ps1 -Wait   # 看完、关掉记事本后才继续
powershell -ExecutionPolicy Bypass -File .\install.ps1
```
<!-- 判据：给出校验和文件或 Release 资产链接；写清脚本会改哪些路径、是否需要管理员权限、如何卸载 -->

### 选项 D：系统级包管理器
| 操作系统 | 推荐包管理器 | 安装命令 |
|---|---|---|
| **Windows** | **Winget** | `winget install {owner}.{repo}` |
| **Windows** | **Scoop** | `scoop install {repo}` |
| **macOS / Linux** | **Homebrew** | `brew install {owner}/tap/{repo}` |
| **跨平台** | **Release 预编译包** | [下载 .exe / .zip / .tar.gz 资产](https://github.com/{owner}/{repo}/releases) |
````
