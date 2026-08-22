<div align="center">

# 🚀 GitHub OSS Prep

**One-click polish any project into a professional GitHub open-source repo.**

**一键把任意本地项目，变成专业级 GitHub 开源仓库。**

[![CI](https://github.com/hyt315/github-oss-prep/actions/workflows/validate.yml/badge.svg)](https://github.com/hyt315/github-oss-prep/actions)
[![Release](https://img.shields.io/github/v/release/hyt315/github-oss-prep?sort=semver)](https://github.com/hyt315/github-oss-prep/releases)
[![License: MIT](https://img.shields.io/github/license/hyt315/github-oss-prep)](LICENSE)
[![Stars](https://img.shields.io/github/stars/hyt315/github-oss-prep?style=social)](https://github.com/hyt315/github-oss-prep/stargazers)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1f6feb)](SKILL.md)
[![skills.sh](https://skills.sh/b/hyt315/github-oss-prep)](https://skills.sh/hyt315/github-oss-prep)

**English · [简体中文](./README.md)**

</div>

> **Status:** v1.7.0 · Local packaging & ZIP delivery need **no GitHub Token** · Publishing to GitHub requires your explicit approval · Read-only audit, never auto-pushes.

---

## 📖 What is this?

Want to open-source a local project, but worried about a leaked API key, a bare README, or release gates you don't know?
**GitHub OSS Prep** is an AI Agent Skill that **scans → fills community health files → scans for secrets → validates adoptability → publishes safely** — turning "open sourcing" from a pile of chores into a single action.

### ✨ Core Features

| Feature | Description |
|---------|-------------|
| 🔍 **Smart Scanning** | Identifies project type (Skill / Code / Docs) and checks against GitHub Community Profile standards |
| 📝 **Audit & Improve** | Fills missing files; also flags outdated/broken/unrunnable docs and improves them after your approval |
| 🛡️ **Privacy Protection** | Scans for API keys, emails, private IPs, real paths — with pre-push verification |
| ✅ **Adoptability Check** | Clean-clone validation of install, minimal example, tests, build, provenance & version consistency |
| 📤 **Flexible Delivery** | Always produces a local ZIP even without auth; publishes via official GitHub connector or `gh` CLI |
| 🔀 **Safe Publishing** | Public projects default to branch + Draft PR + CI + human merge; solo low-risk changes may push directly |
| 📣 **Discovery & Promotion** | Topics, social preview, demo assets, Launch Kit, channel plan & feedback loop |
| 🔎 **Metadata Closure** | Actually writes and reads back Description & Topics; hands off manual todos when unauthenticated |
| 🌐 **Bilingual** | All generated files support Chinese/English, matching global GitHub best practice |
| 📦 **Multi-Platform** | Code projects can publish to npm, PyPI, crates.io, Docker Hub, Homebrew |

---

### 😰 Why? (does this sound like you?)

The real fear of open-sourcing isn't writing code — it's these **invisible pitfalls**:

- **Secret leakage**: hardcoded API keys / local private paths sneaking into commits
- **Identity exposure**: company email / employee ID living forever in git history
- **Junk files**: `.idea`, `.vscode`, `.env` accidentally pushed
- **Weak first impression**: monolingual README, no license, no contributing guide
- **Broken release**: can't tag, version mismatch, download links 404

GitHub OSS Prep is built for exactly these five problems — it scans, fills, and validates to minimize the chance of an accident.

---

## 🚀 Quick Start

This is an AI Agent Skill — install it into any AI assistant and you're ready.

### Option A: Paste one sentence into any Agent (recommended, most universal)

Send this to your AI assistant and it will detect the platform and clone to the right skills directory:

> Please install the GitHub OSS Prep Skill: clone `https://github.com/hyt315/github-oss-prep`
> into your skills directory (e.g. `~/.claude/skills/github-oss-prep`) and confirm it works.

> 💡 **Works with smaller models too**: once installed, just say "help me open-source this project" and it triggers.

### Option B: GitHub CLI 2.90+ (one command)

```bash
gh skill install hyt315/github-oss-prep github-oss-prep --agent claude-code --scope user
# swap claude-code for codex / cursor / github-copilot, etc.
```

### Option C: Claude Code / Codex plugin marketplace

```bash
/plugin marketplace add hyt315/github-oss-prep
```

### Option D: Manual per-platform install

| Platform | Command |
|----------|---------|
| **Claude Code** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.claude/skills/github-oss-prep` |
| **Codex** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.codex/skills/github-oss-prep` |
| **Cursor** | `git clone https://github.com/hyt315/github-oss-prep.git ~/.cursor/skills/github-oss-prep` |

> After install you can scan, organize, privacy-check and ZIP-deliver **without any GitHub Token**; only final publishing needs auth.

### How to use

Once installed, tell your AI assistant what you want. It runs: **Position → Scan → Improve → Validate → Repository Surface → PR/Publish → Release → Discover**. Preparation and ZIP delivery don't need GitHub auth; remote publication, releases and external promotion are **approved separately** — no scope creep.

---

## 🔒 Safety & Privacy

- **Read-only audit by default** — never auto-pushes or rewrites your files (it *reports* problems to you, it doesn't "fix" them silently)
- **Never reads** your source, `.env`, secrets, home directory, or MCP config
- Public projects default to **branch + Draft PR + human merge** — never straight to your `main`
- Packaging & ZIP delivery **need no Token**; auth flow only starts when you explicitly say "publish"
- Publish, Release, package registry and external promotion are **four separate approvals** — one never grants the next

---

## 📥 Download

| Method | Command / Link |
|--------|----------------|
| **HTTPS** | `git clone https://github.com/hyt315/github-oss-prep.git` |
| **SSH** | `git clone git@github.com:hyt315/github-oss-prep.git` |
| **GitHub CLI** | `gh repo clone hyt315/github-oss-prep` |
| **ZIP** | [Download ZIP](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.zip) |
| **Tarball** | [Download Tar](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.tar.gz) |
| **Single file (SKILL.md)** | `curl -O https://raw.githubusercontent.com/hyt315/github-oss-prep/main/SKILL.md` |

### GitHub publish auth (only for final publish)

1. Use your AI platform's official GitHub connector;
2. or run `gh auth login --web` in a trusted terminal;
3. otherwise the skill still produces the full source dir, ZIP, Description and Topics for manual web upload.

Never put a PAT in a public repo, chat log, or Git remote URL. For MCP, use GitHub's maintained [`github/github-mcp-server`](https://github.com/github/github-mcp-server); the old `@modelcontextprotocol/server-github` npm package is unmaintained.

---

## 💡 Core Philosophy

- **Audit before change**: keep valid content; surface diffs before improving weak/broken existing files
- **Type-aware**: Skill / Code / Docs projects get tailored treatment
- **Runnable first**: Community Profile is the floor, not the goal — installable, runnable, contributable in a clean env
- **PR by default**: public maintained projects use branch, Draft PR, CI, and human review
- **Staged approval**: push, Release, package registry and external promotion are never implied by each other

---

## 📁 File Structure

```
github-oss-prep/
├── SKILL.md                          # Core skill definition
├── README.md                         # This file (Chinese)
├── README.en.md                      # English version
├── CHANGELOG.md                      # Version history
├── LICENSE                           # MIT License
├── .gitignore                        # Git ignore rules
├── CONTRIBUTING.md                   # Contribution guide
├── CODE_OF_CONDUCT.md                # Code of conduct
├── SECURITY.md                       # Security policy
├── SUPPORT.md                        # Support channels
├── agents/
│   └── openai.yaml                   # Codex/OpenAI skill metadata
├── scripts/
│   ├── validate_repo.py              # Structure/secret/version self-check
│   └── selftest.py                   # Regression tests (run after changes)
├── .github/
│   ├── CODEOWNERS                    # Auto-assign reviewers
│   ├── pull_request_template.md      # PR template
│   ├── workflows/
│   │   └── validate.yml              # CI: runs validate_repo.py
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.yml            # Bug report form
│       ├── feature_request.yml       # Feature request form
│       ├── doc_improvement.yml       # Docs improvement form
│       └── config.yml                # Template selector config
└── references/                       # Reference docs
    ├── readme-template.md            # README template
    ├── description-guide.md          # Description guide
    ├── privacy-scan.md               # Privacy scan rules
    ├── mcp-push-guide.md             # Push guide
    ├── templates-and-formats.md      # Templates & formats
    ├── release-and-distribution.md   # Release & distribution
    ├── pr-and-release-workflow.md    # PR, CI, validation & release gates
    ├── discovery-and-promotion.md    # Discoverability, Launch Kit & promotion
    ├── github-pat-setup.md           # PAT setup
    └── github-pat-comparison.md      # PAT type comparison
```

---

## 📚 Examples

A local Markdown docs project wants to go open-source:

1. **Install**: paste the Quick-Start sentence to your AI assistant → auto-installed
2. **Scan**: detected as docs project → missing LICENSE, README, .gitignore
3. **Fill**: generated files tailored to the project
4. **Review**: privacy scan clean, content confirmed
5. **Deliver**: confirm repo name & Topics → connector/`gh` publish, or ZIP handoff
6. **Done**: local open-source package is always deliverable; GitHub publication follows when auth is available

---

## ❓ FAQ

- **Q: Can I install it without knowing the command line?** A: Yes. Use Option A — paste that sentence into any AI assistant and it installs for you.
- **Q: Does it work with smaller / weaker models?** A: Yes. The trigger is simple (e.g. "help me open-source this project"), no complex config.
- **Q: Will it push to my GitHub without asking?** A: No. Read-only by default, never auto-pushes; publication requires your explicit confirmation.
- **Q: Can I use it without a GitHub Token?** A: Yes. Scanning, organizing and ZIP delivery need no token — only final publish needs auth.
- **Q: How does it keep my project safe?** A: Read-only audit, never reads source/`.env`/secrets, Draft-PR for public projects. See "Safety & Privacy".

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). If this skill helped you, please [Star ⭐](https://github.com/hyt315/github-oss-prep/stargazers) or open an [Issue](https://github.com/hyt315/github-oss-prep/issues).

---

## 📄 License

[MIT](LICENSE)

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

> 🌏 **中文版: [README.md](./README.md)**
