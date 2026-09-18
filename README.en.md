# 📦 GitHub OSS Prep / github-oss-prep

<div align="center">

**Turn any project into a polished, GitHub-ready open-source repository with full community health files, CI automation, and tailored multi-channel distribution.**

**将任意项目美化为适合 GitHub 发布的专业级开源版本，补齐全套社区健康文件与 CI 自动化，构建专属针对性门面与全生态分发。**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/hyt315/github-oss-prep?sort=semver)](CHANGELOG.md)
[![Validate skill](https://github.com/hyt315/github-oss-prep/actions/workflows/validate.yml/badge.svg)](https://github.com/hyt315/github-oss-prep/actions)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1f6feb)](SKILL.md)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Python)-brightgreen)](SKILL.md)
[![GitHub Stars](https://img.shields.io/github/stars/hyt315/github-oss-prep?style=social)](https://github.com/hyt315/github-oss-prep/stargazers)

[English](./README.en.md) | [中文](./README.md)

</div>

---

## 📖 What is this?

When open-sourcing projects on GitHub, developers frequently hit these hurdles:
- Missing required `LICENSE`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, or modern YAML Issue Forms, preventing the repo from reaching 100% in GitHub Insights → Community profile;
- Generic, one-size-fits-all README layouts that fail to highlight the distinct value of AI Agent Skills, MCP Servers, Model weights/GGUF, system CLI tools, browser extensions, or fullstack apps;
- Missing concrete publishing instructions for `uvx`, `bunx`, `pnpm dlx`, Hugging Face, Chrome Web Store, or CI matrix testing;
- Accidental leaks of local machine paths, private agent session fingerprints, API tokens, or Git credentials into public repositories.

**`github-oss-prep`** is a professional-grade GitHub open-source preparation skill designed for AI Agents and open-source creators. Grounded in the **Progressive Disclosure Principle**, it features **10 Universal Archetype-tailored README engines**, **all-ecosystem package distribution guides**, a **5-layer deep environment and credential security scanner**, and the **GitHub 2026 Community Profile & CI pack** for seamless, professional repo releases.

---

## ✨ Key Features

| Core Module | Capabilities | Value Delivered |
|---|---|---|
| **10 Universal Archetype Engines** | Tailored, copy-paste-ready Markdown skeletons for AI Skills, MCP Servers, Models/GGUF, CLI tools, Multimedia, SDKs, Extensions, IaC, Web Apps, Awesome Lists | Replaces generic templates with concrete structures and package manager matrices |
| **Progressive Disclosure Architecture** | Loads only the specific archetype template matched in Step 0 | Eliminates context bloat and prevents cross-archetype pollution |
| **5-Layer Deep Security Net** | Scans API keys, local path fingerprints, session IDs, Git remote tokens, build caches with real-leak comparison table | 100% prevention of credentials and private environment leakage |
| **2026 Community & CI Profile Pack** | Interactive YAML Issue Forms (`bug_report.yml`), PR template, `SECURITY.md`, Node/Python Matrix CI, Dependabot | Guarantees 100% GitHub Community Standards score and automated dependency maintenance |
| **All-Ecosystem Distribution Guides** | Practical publishing workflows for uv/PyPI, npm, Hugging Face, Chrome Web Store, Docker, Homebrew, Crates.io, Release Checksums | End-to-end guidance from local source to global package registries |
| **Lightweight Architecture** | Slim main definition, single-layer reference map, automated regression tests | Strict engineering discipline, 100% PASS on `skill-doctor` audits |

---

## 📊 Complete Open-Source Preparation Architecture

```
[Input: Any local project / directory to open-source]
                         │
      [Step 0: Positioning (target users + core value + verifiable result)]
      Detect: AI Skill / MCP Server / Model weights / CLI tool / Browser extension / IaC / ...
                         │
      [Step 1: Scanning (archetype detection + gaps, weaknesses, risks)]
      Check against the GitHub Community Profile requirements
                         │
      [Step 2: Assembling (create missing files + improve weak ones after approval)]
      Generate bilingual community health files
                         │
      [Step 3: Verification (content + privacy + provenance/licensing + clean-environment run)]
      5-layer deep scan to guarantee no sensitive information leaks
                         │
      [Step 4: Repository facade (README + Description + Topics + social preview)]
      Progressive disclosure: load only the dedicated archetype skeleton
                         │
      [Step 5: Publish confirmation → branch/PR (default) or solo direct push (optional)]
      public-safe or solo-fast
                         │
      [Step 6: Release + multi-platform distribution + version consistency check]
      uv/PyPI/npm/HuggingFace/ChromeStore/Docker/Homebrew/Crates.io
                         │
      [Step 7: Discovery & growth (Launch Kit + targeted channels + feedback loop)]
      Stranger Test, channel selection, release rhythm
```

---

## 🚀 Quick Start

This is an AI Agent Skill — install it into your AI assistant and you're ready.

### Option A: Paste one sentence into any Agent (recommended, most universal)

Send this to your AI assistant and it will detect the platform and clone to the right skills directory:

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

### Option D: Run local regression selftest

```bash
python scripts/selftest.py
```

---

## 📚 End-to-End Practical Walkthrough

Suppose you have a local Python CLI utility, MCP Server, or browser extension ready to open-source:

1. **Trigger & Scan**: Send "help me prepare this project for open-source" → Auto-detects archetype, executes 5-layer privacy audit, and cleans build caches;
2. **Generate Community & CI Files**: Creates GitHub 2026-compliant YAML Issue Forms, `SECURITY.md`, `LICENSE`, and Node/Python matrix CI workflows;
3. **Progressive Facade Rendering**: Progressively loads dedicated archetype template, generating bilingual READMEs with modern CLI matrices (`uvx`/`bunx`) and config blocks;
4. **Validate & Distribute**: Runs `selftest.py` locally, outputs clean reviewable project bundle, and publishes to GitHub, Release assets, and global registries upon explicit approval.

---

## 🔒 Safety & Privacy Principles

- **Audit Before Change**: Reads and audits locally by default, generating diffs before creating or modifying any files.
- **Progressive Isolation**: Only loads relevant archetype references, preventing context pollution.
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

## 📖 In-Depth Technical References

| Reference Guide | Core Focus | When to Read | Estimated Time |
|---|---|---|---|
| 📑 [**10 Universal Archetype README Engines (`readme-template.md`)**](references/readme-template.md) | Complete copy-pasteable Markdown skeletons and 2026 CLI runner tables | When generating or rewriting READMEs | 4 mins |
| 🚨 [**OSS Prep Killer Pitfalls & Baselines (`github-oss-prep-pitfalls.md`)**](references/github-oss-prep-pitfalls.md) | GitHub Insights 100% gates, Git history secret scrubbing & CI supply-chain action pinning | When auditing safety baselines and avoiding deep pitfalls | 4 mins |
| 🛡️ [**5-Layer Deep Privacy Scanner (`privacy-scan.md`)**](references/privacy-scan.md) | 5-layer interception rules, real-leak comparison table, and sanitization | When performing security audits and sanitization | 3 mins |
| 🏛️ [**Community Profile & CI Pack (`community-templates.md`)**](references/community-templates.md) | Interactive YAML Issue Forms, Node/Python matrix CI, and Dependabot | When completing GitHub Community Standards & CI | 3 mins |
| 🚀 [**All-Ecosystem Distribution (`release-and-distribution.md`)**](references/release-and-distribution.md) | uv, npm, HuggingFace, ChromeStore, Docker publishing, and Checksums | When publishing to registries or GitHub Release | 4 mins |
| 🏷️ [**Description & Topics Guide (`description-guide.md`)**](references/description-guide.md) | Concise 120-char repository description and topic selection | When configuring repo surface metadata | 3 mins |
| 🌐 [**Discoverability & Launch Kit (`discovery-and-promotion.md`)**](references/discovery-and-promotion.md) | Promotion strategies, social previews, and channel checklists | When launching or publicizing a project | 3 mins |
| 🔐 [**GitHub Push & MCP Guide (`mcp-push-guide.md`)**](references/mcp-push-guide.md) | Official MCP server setup and standard CLI push workflows | When pushing code and creating remote repos | 2 mins |
| 🚦 [**PR, CI & Release Gates (`pr-and-release-workflow.md`)**](references/pr-and-release-workflow.md) | Branches, PRs, CI testing, and release gating rules | When establishing CI pipelines and release gates | 3 mins |
| 🔑 [**GitHub Credential Comparison (`github-pat-comparison.md`)**](references/github-pat-comparison.md) | Permission and security comparison across the official connector, GitHub CLI, and PATs | When choosing a push authentication method | 2 mins |
| 🔒 [**Least-Privilege PAT Setup (`github-pat-setup.md`)**](references/github-pat-setup.md) | Creating a least-privilege personal access token on GitHub's official page | When a PAT is explicitly chosen | 1 min |

---

## 📁 File Structure

```
github-oss-prep/
├── SKILL.md                          # Core skill definition, progressive disclosure & lightweight workflow
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
├── tests/
│   └── test_skill.py                 # Pytest automated test suite entry
├── .github/
│   ├── CODEOWNERS                    # Code owners config
│   ├── pull_request_template.md      # Standard PR template
│   ├── workflows/                    # CI workflows
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.yml            # Interactive Bug report form
│       ├── doc_improvement.yml       # Documentation improvement form
│       ├── feature_request.yml       # Interactive Feature request form
│       └── config.yml                # Template selector config
└── references/                       # In-depth reference guides
    ├── github-oss-prep-pitfalls.md   # OSS Prep Killer Pitfalls & Baselines
    ├── readme-template.md            # 10 Universal Archetype complete README template engines
    ├── privacy-scan.md               # 5-Layer deep privacy and environment scan guide
    ├── community-templates.md        # GitHub 2026 Community Profile & CI pack
    ├── release-and-distribution.md   # All-ecosystem package distribution guides
    ├── description-guide.md          # Description & Topics optimization guide
    ├── discovery-and-promotion.md    # Open-source discoverability & Launch Kit
    ├── mcp-push-guide.md             # GitHub push & MCP guide
    ├── pr-and-release-workflow.md    # PR, CI & release gates
    ├── github-pat-setup.md           # GitHub PAT setup guide
    └── github-pat-comparison.md      # GitHub PAT comparison
```

---

---

## 🌐 GitHub Open Source Lifecycle Suite

A complete, production-ready toolchain for open-source maintainers and contributors:

| Stage / Role | Recommended Skill | Core Mission & Capabilities | GitHub Repository |
|---|---|---|---|
| 📦 **Pre-Launch Prep** | [**`github-oss-prep`**](https://github.com/hyt315/github-oss-prep) | Automated repository scaffolding, bilingual READMEs, CI workflows, and compliance checks | [hyt315/github-oss-prep](https://github.com/hyt315/github-oss-prep) |
| 🩺 **Quality Doctor** | [**`skill-doctor`**](https://github.com/hyt315/skill-doctor) | 50+ industrial static rules + dynamic selftest runner for 100% reliable Agent Skills | [hyt315/skill-doctor](https://github.com/hyt315/skill-doctor) |
| ⚙️ **Post-Launch Ops** | [**`github-oss-ops`**](https://github.com/hyt315/github-oss-ops) | Issue triage, AI hallucination defense, PR review, GHSA vulnerability SOP, and multi-channel broadcasting | [hyt315/github-oss-ops](https://github.com/hyt315/github-oss-ops) |
| 🚀 **Contributor Navigator** | [**`github-oss-contribute`**](https://github.com/hyt315/github-oss-contribute) | End-to-end contributor guide: Fork syncing, Rebase conflict resolution, DCO signing, and anti-AI slop gates | [hyt315/github-oss-contribute](https://github.com/hyt315/github-oss-contribute) |

---

## ❓ FAQ

- **Q: Do I need a GitHub Token for preparation and packaging?**  
  A: No. Scanning, privacy audits, community file generation, README creation, and ZIP packaging run entirely locally without tokens.
- **Q: Will it rewrite my codebase without asking?**  
  A: Never. The skill follows strict "audit before change" principles, requiring explicit approval before modifying any files.
- **Q: Does it support non-AI projects?**  
  A: Absolutely. It features 10 dedicated archetype engines covering MCP Servers, AI models, CLI tools, extensions, SDK libraries, IaC, fullstack apps, and curated lists.
- **Q: Why does `SKILL.md` remain lightweight?**  
  A: The skill follows the Progressive Disclosure Architecture, encapsulating deep domain templates into modular references to prevent LLM context over-saturation and cross-domain pollution.

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md). If this skill helped you, please give it a [Star ⭐](https://github.com/hyt315/github-oss-prep/stargazers)!

---

## 📄 License

Licensed under the [MIT License](LICENSE).

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

> 🌏 **中文版: [README.md](./README.md)**
