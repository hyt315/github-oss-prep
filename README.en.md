# 📦 GitHub OSS Prep / github-oss-prep

<div align="center">

**Turn any project into a polished, GitHub-ready open-source repository with full community health files, CI automation, and tailored multi-channel distribution.**

**将任意项目美化为适合 GitHub 发布的专业级开源版本，补齐全套社区健康文件与 CI 自动化，构建专属针对性门面与全生态分发。**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/hyt315/github-oss-prep?sort=semver)](CHANGELOG.md)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1f6feb)](SKILL.md)
[![GitHub Stars](https://img.shields.io/github/stars/hyt315/github-oss-prep?style=social)](https://github.com/hyt315/github-oss-prep/stargazers)

[English](./README.en.md) | [中文](./README.md)

**30-second start**: `gh skill install hyt315/github-oss-prep github-oss-prep --agent claude-code --scope user`

**Minimal example**: tell your project "Use github-oss-prep to scan this project. Output only the positioning card and the gap list."

</div>

```text
$ Use github-oss-prep to scan this project

[Step 0] Positioning  → card: target users / core promise / minimal example / scope
[Step 1] Scanning     → archetype + gap list against the Community seven-item set
[Step 2] Assembling   → fill community health files (written only after your OK)
[Step 3] Verification → 5-layer privacy scan + clean-environment reproduction
[Step 4] Facade       → README / Description / Topics / social preview
[Step 5] Publishing   → branch/PR (default) or direct push (approval required)
[Step 6] Distribution → Release + multi-registry publish + version consistency
[Step 7] Growth       → Launch Kit + targeted channels + feedback loop
```

---

## 📖 What is this?

Publishing a code, agent, or knowledge-base project on GitHub tends to stall on the same chores: missing compliant `LICENSE`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, or modern YAML Issue Forms, leaving the repository short of 100% on GitHub Insights → Community; generic README layouts that never convey the distinct value of an AI Skill, MCP Server, model/GGUF release, system CLI tool, browser extension, or fullstack app; and no concrete publishing commands for `uvx`, `bunx`, `pnpm dlx`, Hugging Face, or the Chrome Web Store.

The subtler risk is leakage: local absolute paths, private agent session fingerprints, API keys, and Git credentials are all too easy to push into a public repository without noticing.

**`github-oss-prep`** is a professional-grade GitHub open-source preparation skill built for AI Agents and open-source authors. Following the **Progressive Disclosure Principle**, it ships **10 archetype-specific README template engines**, **all-ecosystem distribution guides**, a **5-layer deep privacy and security audit**, and the **GitHub 2026 community and CI automation pack**, covering the full loop from positioning, scanning, assembling, and verifying to facade, publishing, distribution, and growth. Every stage keeps an independent authorization boundary — local preparation, remote push, Release publication, and external promotion are confirmed separately, never chained without consent.

## ✨ Key Features

| Core Capability | What It Does | Value Delivered |
|---|---|---|
| **10 Universal Archetype Engines** | Tailored, copy-paste-ready Markdown skeletons for AI Skills, MCP Servers, Models/GGUF, CLI tools, Multimedia, SDKs, Extensions, IaC, Web Apps, Awesome Lists | Replaces generic templates with concrete structures and package manager matrices |
| **Progressive Disclosure Architecture** | Loads only the specific archetype template matched in Step 0 | Eliminates context bloat and prevents cross-archetype pollution |
| **5-Layer Deep Security Net** | Scans API keys, local path fingerprints, session IDs, Git remote tokens, build caches with real-leak comparison table | 100% prevention of credentials and private environment leakage |
| **2026 Community & CI Profile Pack** | Interactive YAML Issue Forms (`bug_report.yml`), PR template, `SECURITY.md`, Node/Python Matrix CI, Dependabot | Guarantees 100% GitHub Community Standards score and automated dependency maintenance |
| **All-Ecosystem Distribution Guides** | Practical publishing workflows for uv/PyPI, npm, Hugging Face, Chrome Web Store, Docker, Homebrew, Crates.io, Release Checksums | End-to-end guidance from local source to global package registries |
| **Lightweight Architecture** | Slim main definition, single-layer reference map, automated regression tests | Strict engineering discipline, 100% PASS on `skill-doctor` audits |

---

## 🚀 Quick Start

### Option A: Paste one sentence into any Agent (recommended, most universal)

> Please install the github-oss-prep skill: clone `https://github.com/hyt315/github-oss-prep` into your skills directory (e.g. `~/.claude/skills/github-oss-prep` or `~/.agents/skills/github-oss-prep`) and confirm it works.

### Option B: GitHub CLI 2.90+ (one command)

```bash
gh skill install hyt315/github-oss-prep github-oss-prep --agent claude-code --scope user
```

### Option C: Manual per-platform install

| Platform | Command |
|---|---|
| **Claude Code** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.claude/skills/github-oss-prep` |
| **Codex** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.codex/skills/github-oss-prep` |
| **Cursor** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.cursor/skills/github-oss-prep` |
| **General Agents** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.agents/skills/github-oss-prep` |

### Usage Example (minimal, runnable)

Once installed, say this inside your project directory:

> Use github-oss-prep to scan this project. Output only the positioning card and the gap list — do not modify any files.

Expected output:

| Output | Content |
|---|---|
| **Positioning card** | Target users, core promise, minimal example, scope of this round |
| **Gap list** | Item-by-item against the seven Insights → Community requirements |
| **Fact card** | L1 privacy / L2 community / L3 supply chain verdicts |

---

## 🔒 Safety & Privacy Principles

- **Read-only by default / audit before change**: local preparation scans read-only and reports diffs; any change to an existing file is shown with its rationale first. The user's home directory, editor config, and MCP config are never scanned for tokens.
- **Zero-token local runs**: scanning, privacy audits, community file generation, README authoring, and source packaging all run locally with no credentials and no extra API consumption.

## 📥 Download

| Method | Command / Link |
|---|---|
| **HTTPS** | `git clone https://github.com/hyt315/github-oss-prep.git` |
| **SSH** | `git clone git@github.com:hyt315/github-oss-prep.git` |
| **ZIP** | [Download ZIP](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.zip) |
| **Single file (SKILL.md)** | `curl -O https://raw.githubusercontent.com/hyt315/github-oss-prep/main/SKILL.md` |

## 📄 License

Licensed under the [MIT License](LICENSE).
