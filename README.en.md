# 📦 GitHub OSS Prep

<div align="center">

**Lightweight AI Agent Skill for GitHub open-source prep: deterministic secret & hygiene audit, must-have vs optional polish, and approval-gated publishing.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/hyt315/github-oss-prep?sort=semver)](CHANGELOG.md)
[![Validate skill](https://github.com/hyt315/github-oss-prep/actions/workflows/validate.yml/badge.svg)](https://github.com/hyt315/github-oss-prep/actions)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1f6feb)](SKILL.md)

[English](./README.en.md) | [中文](./README.md)

</div>

## What is it?

Modern AI coding agents can draft clean READMEs and config files without rigid fill-in-the-blank templates. What still breaks open-source launches is leaking local paths, personal emails, API keys, or secrets buried in git history—and bloating small repos with unused governance boilerplate.

`github-oss-prep` splits open-source prep into two layers:
- **Deterministic audit script**: Zero-dependency `scripts/validate_repo.py` checks working files, `.git/config`, git history (streaming), commit emails, GitHub Actions supply-chain hygiene, and baseline OSS files on any target repository.
- **Lean, layered guidance**: Separates **must-have basics** (clean secret scan, runnable README, `LICENSE`, `.gitignore`, Description/Topics) from **on-demand enhancements** (community files, SHA-pinned CI, bilingual docs, multi-channel release, promotion), guarded by two approval gates.

## Quick Start

### Option A: Send one sentence to your AI agent (easiest)

> Please install the `github-oss-prep` skill from `https://github.com/hyt315/github-oss-prep` into your skills directory and confirm it is ready.

Then ask your agent: *"Audit this repo and prepare it for GitHub open-source release."*

### Option B: Install via `npx skills` (90+ agents)

```bash
# Project-level install
npx skills add hyt315/github-oss-prep

# Global install (recommended)
npx skills add hyt315/github-oss-prep -g
```

### Option C: Manual clone

```bash
# Claude Code
git clone https://github.com/hyt315/github-oss-prep.git ~/.claude/skills/github-oss-prep

# Cursor
git clone https://github.com/hyt315/github-oss-prep.git ~/.cursor/skills/github-oss-prep

# Codex / generic Agents directory
git clone https://github.com/hyt315/github-oss-prep.git ~/.agents/skills/github-oss-prep
```

### Run the validator directly

```bash
# Audit any target repository (working tree + git history + CI security + baseline files)
python3 scripts/validate_repo.py /path/to/your-repo --strict --history

# Run regression tests
python3 -m unittest discover -s tests -v
```

## Workflow

1. **Audit & Scope**: Run `validate_repo.py --strict --history`, review manual blind spots, identify project archetype → **Gate 1 (before editing files)**.
2. **Must-Have Polish**: Clear P0/P1 findings, write a concise runnable README (for Skills: copy-to-AI prompt + `npx skills add` + manual clone), ensure `LICENSE` and `.gitignore`, draft Description (≤120 chars) & Topics (5–10), verify clean-directory run.
3. **On-Demand Enhancements**: Add `SECURITY.md`, `CONTRIBUTING.md`, YAML Issue Forms, SHA-pinned CI, Dependabot (only for ecosystems present in the repo), bilingual README, or package distribution only when the project needs them.
4. **Approval-Gated Publish**: → **Gate 2 (before publishing)** Read-only environment probe (connector / `gh` / `GITHUB_TOKEN` / offline ZIP), push, set and read back Description/Topics, and optionally cut a SemVer Release.

## Repository Structure

```text
github-oss-prep/
├── SKILL.md                             # Core skill workflow (4 steps + 2 approval gates)
├── scripts/
│   ├── secret-rules.json                # Single source of truth for secret/privacy patterns
│   └── validate_repo.py                 # Zero-dependency repository auditor
├── references/
│   ├── readme-and-archetypes.md         # Must-have vs optional README guide & 6 archetypes
│   ├── security-and-pitfalls.md         # Scan blind spots, git history cleanup, CI & license traps
│   ├── community-and-ci.md              # On-demand community files & SHA-pinned CI snippets
│   └── publishing-and-release.md        # Read-only probe, one-shot credential push, Release & promo
├── tests/
│   ├── test_skill.py                    # Unified stdlib unittest suite
│   └── fixtures/                        # Positive leak & clean regression fixtures
└── .github/workflows/validate.yml       # CI validation workflow
```

## Known Limitations

- **Pattern-based scanning**: Detects major cloud/AI keys, local paths, proxy fingerprints, personal emails/CN mobile numbers, `.git/config` tokens, and streaming git history, without entropy analysis; pair with `gitleaks` or `trufflehog` for high-sensitivity repos.
- **No runtime execution in script**: Clean-clone install and test execution are performed by the agent or project CI.
- **License guidance is not legal advice**: Verify upstream model/dataset license chains independently.

## License

[MIT](LICENSE). See [CHANGELOG.md](CHANGELOG.md) for version history.
