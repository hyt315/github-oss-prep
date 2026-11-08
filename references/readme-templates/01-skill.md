# 品类 1：AI Agent 技能型 (Skill / Tool) 完整模板

> 先读 [README 模板总纲](../readme-template.md) 的「前置事实清单」「通用底座 12 节」和「品类增量」表，再用本骨架。
> 只取与你项目相符的这一份，不要跨品类拼接。


````markdown
# 📦 项目名称 / Project Name

<div align="center">

<!-- 判据：首屏三件事缺一不可 —— ①一句话价值（谁+做什么+得到什么）②一条复制即可运行的命令 ③一张带 alt 的结果图；只喊口号视为未完成 -->
**一句话中文功能与价值描述**

**One-liner English description of core capabilities and benefits.**

[![License](https://img.shields.io/github/license/{owner}/{repo})](LICENSE)
[![Release](https://img.shields.io/github/v/release/{owner}/{repo}?sort=semver)](https://github.com/{owner}/{repo}/releases/latest)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1f6feb)](SKILL.md)
[![GitHub Stars](https://img.shields.io/github/stars/{owner}/{repo}?style=social)](https://github.com/{owner}/{repo}/stargazers)

[English](README.en.md) | [中文](README.md)

</div>

---

## 📖 这是什么？

<!-- 判据：2~3 段，第一段必须含"谁 + 在什么场景 + 原来多麻烦 + 现在少几步"；只写特性名不算 -->
<!-- 反例："本技能用于帮助用户更好地准备开源项目，功能强大。" -->
<!-- 可删：若首屏一句话已能自解释，本节可压成 1 段 -->
说明该技能解决的具体痛点场景与核心价值。

## ✨ 核心特性

<!-- 判据：每行"功能说明"必须能指向一处可验证行为（文件、命令或检查项），不能是形容词 -->
| 核心特性 | 功能说明（可验证） | 带来价值 |
|---|---|---|
| **先审后改** | 改动前输出 diff 与理由，获确认后才写文件 | 不怕被覆盖，敢把已有项目交出来 |
| **发布门禁** | P0 检查（凭据/许可/可复现）失败即阻断公开 | 不会把带密钥的仓库推上网 |

---

## 🚀 快速开始

### 方式 A：把一句话发给任意 Agent（最推荐、最通用）

> 请安装 {repo} 技能：克隆 `https://github.com/{owner}/{repo}` 到你的 skills 目录（如 `~/.claude/skills/{repo}` 或 `~/.agents/skills/{repo}`），并确认安装成功。

### 方式 B：GitHub CLI（Public Preview，先 `gh skill --help` 确认）

```bash
# --pin 锁定版本，便于复现安装（官方还有 gh skill publish / search / list）
gh skill install {owner}/{repo} {name} --agent claude-code --scope user --pin
```

### 方式 C：多平台手动安装

| 平台 | 安装命令 |
|---|---|
| **Claude Code** | `git clone https://github.com/{owner}/{repo}.git ~/.claude/skills/{repo}` |
| **Codex** | `git clone https://github.com/{owner}/{repo}.git ~/.agents/skills/{repo}` |
| **Cursor** | `git clone https://github.com/{owner}/{repo}.git ~/.cursor/skills/{repo}` |
| **通用 Agents** | `git clone https://github.com/{owner}/{repo}.git ~/.agents/skills/{repo}` |

---

## 🔒 安全与隐私原则
<!-- 判据：本节要写"能力边界"（会写哪些路径、会执行什么命令、如何回滚、凭据在哪一步才需要），不是写"我们重视安全"的态度话 -->

- **纯只读 / 先审后改**：说明本技能会写哪些路径、会不会执行命令、失败时如何回滚。
- **凭据边界**：说明本地整理为何不需要 token，只有哪一步需要授权（写清"哪一步"）。

## 📥 下载与获取

| 方式 | 命令 / 链接 |
|---|---|
| **HTTPS** | `git clone https://github.com/{owner}/{repo}.git` |
| **SSH** | `git clone git@github.com:{owner}/{repo}.git` |
| **ZIP** | [下载 ZIP](https://github.com/{owner}/{repo}/archive/refs/heads/main.zip) |
| **单文件** | `curl -O https://raw.githubusercontent.com/{owner}/{repo}/main/SKILL.md` |

## 📄 开源协议

本项目采用 [{SPDX_ID}](LICENSE) 许可证开源。
````
