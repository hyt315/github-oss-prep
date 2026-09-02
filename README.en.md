# 📦 GitHub OSS Prep / github-oss-prep

<div align="center">

**Turn any project into a polished, GitHub-ready open-source repository with full community health files and tailored facade.**

**将任意项目美化为适合 GitHub 发布的专业级开源版本，补齐全套社区健康文件，构建专属针对性门面。**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/hyt315/github-oss-prep?sort=semver)](CHANGELOG.md)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1f6feb)](SKILL.md)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Python)-brightgreen)](SKILL.md)
[![GitHub Stars](https://img.shields.io/github/stars/hyt315/github-oss-prep?style=social)](https://github.com/hyt315/github-oss-prep/stargazers)

[English](./README.en.md) | [中文](./README.md)

</div>

---

## 📖 What is this?

When open-sourcing projects on GitHub, developers frequently hit these hurdles:
- Missing required `LICENSE`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, or modern YAML Issue Forms, preventing the repo from reaching 100% in GitHub Insights → Community profile;
- Generic, one-size-fits-all README layouts that fail to highlight the distinct value of AI Agent Skills, system CLI tools, multimedia engines, or developer SDKs;
- Accidental leaks of local machine paths, private agent session fingerprints, API tokens, or Git credentials into public repositories.

**`github-oss-prep`** is a professional-grade GitHub open-source preparation skill designed for AI Agents and open-source creators. It features **6 project archetype-tailored README engines**, a **5-layer deep environment and credential security scanner**, and the **GitHub 2026 Community Profile pack** for seamless, professional repo releases.

---

## ✨ Key Features

| Core Module | Capabilities | Value Delivered |
|---|---|---|
| **6 Archetype README Engines** | Tailored structures for AI Skills, CLI tools, Multimedia, SDKs, Fullstack Apps, Docs | Replaces generic templates with precise positioning and quick-start matrices |
| **5-Layer Deep Security Net** | Scans API keys, local path fingerprints, session IDs, Git remote tokens, build caches | 100% prevention of credentials and private environment leakage |
| **2026 Community Profile Pack** | Interactive YAML Issue Forms (`bug_report.yml`), PR template, `SECURITY.md` | Guarantees 100% GitHub Community Standards score |
| **Multi-Channel Distribution** | `gh skill install`, one-sentence agent auto-install, Release binary assets with SHA-256 | Flawless, instant installation for users and downstream AI agents |
| **Lightweight Architecture** | Slim main definition, single-layer reference map, automated regression tests | Strict engineering discipline, 100% PASS on `skill-doctor` audits |

---

## 🚀 Quick Start

This is an AI Agent Skill — install it into your AI assistant and you're ready.

### Option A: Paste one sentence into any Agent (recommended, most universal)

Send this to your AI assistant and it will detect the platform and clone to the right skills directory:

> Please install the github-oss-prep skill: clone `https://github.com/hyt315/github-oss-prep` into your skills directory (e.g. `~/.claude/skills/github-oss-prep` or `~/.agents/skills/github-oss-prep`) and confirm it works.

> 💡 **Works with smaller models too**: once installed, just say "help me open-source this project" or "prepare this repo for GitHub" to trigger the complete workflow.

### Option B: GitHub CLI 2.90+ (one command)

```bash
gh skill install hyt315/github-oss-prep github-oss-prep --agent claude-code --scope user
# swap claude-code for codex / cursor / github-copilot, etc.
```

### Option C: Manual per-platform install

| Platform | Command |
|---|---|
| **Claude Code** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.claude/skills/github-oss-prep` |
| **Codex** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.codex/skills/github-oss-prep` |
| **Cursor** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.cursor/skills/github-oss-prep` |
| **General Agents** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.agents/skills/github-oss-prep` |

### Option D: Run local regression selftest

```powershell
python scripts/selftest.py
```

---

## 🔒 Safety & Privacy Principles

- **Audit Before Change**: Reads and audits locally by default, generating diffs before creating or modifying any files.
- **5-Layer Deep Defense**: Comprehensive scans across code, docs, `.git/config`, and commit history to prevent leaks.
- **Staged Approvals**: Local preparation, remote repo creation, Release packaging, and external promotion are approved independently.

---

## 📥 Download

| Method | Command / Link |
|---|---|
| **HTTPS** | `git clone https://github.com/hyt315/github-oss-prep.git` |
| **SSH** | `git clone git@github.com:hyt315/github-oss-prep.git` |
| **GitHub CLI** | `gh repo clone hyt315/github-oss-prep` |
| **ZIP** | [Download ZIP](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.zip) |
| **Tarball** | [Download Tar](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.tar.gz) |
| **Single file (SKILL.md)** | `curl -O https://raw.githubusercontent.com/hyt315/github-oss-prep/main/SKILL.md` |

---

## 📁 File Structure

```
github-oss-prep/
├── SKILL.md                          # Core skill definition and lightweight workflow
├── README.md                         # Chinese documentation
├── README.en.md                      # English documentation
├── CHANGELOG.md                      # Version history
├── LICENSE                           # MIT License
├── .gitignore                        # Git ignore rules
├── CONTRIBUTING.md                   # Contribution guide
├── CODE_OF_CONDUCT.md                # Code of conduct
├── SECURITY.md                       # Security policy
├── SUPPORT.md                        # Support channels
├── manifest.json                     # Skill manifest
├── agents/                           # Multi-agent metadata
├── scripts/
│   ├── validate_repo.py              # Structure, hygiene & security validator
│   └── selftest.py                   # Automated regression test runner
├── .github/
│   ├── CODEOWNERS                    # Code owners config
│   ├── pull_request_template.md      # Standard PR template
│   ├── workflows/                    # CI workflows
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.yml            # Interactive Bug report form
│       ├── feature_request.yml       # Interactive Feature request form
│       └── config.yml                # Template selector config
└── references/                       # In-depth reference guides
    ├── readme-template.md            # 6 Archetype README template engines
    ├── privacy-scan.md               # 5-Layer deep privacy and environment scan guide
    ├── community-templates.md        # GitHub 2026 Community Profile pack
    ├── release-and-distribution.md   # Multi-channel distribution matrix
    ├── description-guide.md          # Description & Topics optimization guide
    ├── discovery-and-promotion.md    # Open-source discoverability & Launch Kit
    ├── mcp-push-guide.md             # GitHub push & MCP guide
    ├── pr-and-release-workflow.md    # PR, CI & release gates
    ├── github-pat-setup.md           # GitHub PAT setup guide
    └── github-pat-comparison.md      # GitHub PAT comparison
```

---

## ❓ FAQ

- **Q: Do I need a GitHub Token for preparation and packaging?**  
  A: No. Scanning, privacy audits, community file generation, README creation, and ZIP packaging run entirely locally without tokens.
- **Q: Will it rewrite my codebase without asking?**  
  A: Never. The skill follows strict "audit before change" principles, requiring explicit approval before modifying any files.
- **Q: Does it support non-AI projects?**  
  A: Absolutely. It features 6 dedicated archetype engines covering CLI tools, multimedia projects, SDK libraries, fullstack apps, and docs.

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md). If this skill helped you, please give it a [Star ⭐](https://github.com/hyt315/github-oss-prep/stargazers)!

---

## 📄 License

Licensed under the [MIT License](LICENSE).

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

> 🌏 **中文版: [README.md](./README.md)**
