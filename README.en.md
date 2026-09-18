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

It covers far more than "filling in missing files" — it delivers the complete open-source delivery loop: **positioning → scanning → assembling → verifying → facade → publishing → distribution → growth**, and **every stage has an independent authorization boundary**: local preparation, remote push, Release publication, and external promotion are confirmed separately, never chained without consent.

## 🎯 When to use it

| What you say | What the skill does |
|---|---|
| "Help me prepare this repo for open source" | Runs the full Step 0–7 flow, starting from a positioning card |
| "Polish this project" / "The README is rough" | Detects the archetype → loads only the matching template → rebuilds the README |
| "Check whether anything sensitive would leak" | Runs the 5-layer privacy scan plus Git history credential residue checks |
| "Community profile isn't 100%" | Works through the GitHub Insights seven-item checklist |
| "How do I publish to PyPI / npm / HuggingFace?" | Loads the all-ecosystem distribution guide and emits the exact commands |
| "Write the repo description and topics" | Applies the 120-char rule to produce a Description plus 5–12 Topics |
| "Push it" / "Create a Release" | Shows a confirmation checklist first, and acts only after explicit approval |

> Local preparation, scanning, document generation, and ZIP packaging **require no GitHub authentication at all**. Authentication is only checked when you explicitly say "publish to GitHub now".

## ✨ Key Features

| Core Capability | What It Does | Value Delivered |
|---|---|---|
| **10 Universal Archetype Engines** | Tailored, copy-paste-ready Markdown skeletons for AI Skills, MCP Servers, Models/GGUF, CLI tools, Multimedia, SDKs, Extensions, IaC, Web Apps, Awesome Lists | Replaces generic templates with concrete structures and package manager matrices |
| **Progressive Disclosure Architecture** | Loads only the specific archetype template matched in Step 0 | Eliminates context bloat and prevents cross-archetype pollution |
| **5-Layer Deep Security Net** | Scans API keys, local path fingerprints, session IDs, Git remote tokens, build caches with real-leak comparison table | 100% prevention of credentials and private environment leakage |
| **2026 Community & CI Profile Pack** | Interactive YAML Issue Forms (`bug_report.yml`), PR template, `SECURITY.md`, Node/Python Matrix CI, Dependabot | Guarantees 100% GitHub Community Standards score and automated dependency maintenance |
| **All-Ecosystem Distribution Guides** | Practical publishing workflows for uv/PyPI, npm, Hugging Face, Chrome Web Store, Docker, Homebrew, Crates.io, Release Checksums | End-to-end guidance from local source to global package registries |
| **Complete Delivery Loop** | Positioning → scanning → assembling → verifying → facade → publishing → distribution → growth, 8 stages in total | Not just "all files present", but "a stranger can actually run it and adopt it" |
| **Staged Authorization & Safe Push** | Four operation classes approved independently; `public-safe` branch/PR flow by default, `solo-fast` direct push optional | High-risk actions (push, release, promotion) always need a human on the final trigger |
| **Lightweight Architecture** | Slim main definition, single-layer reference map, automated regression tests | Strict engineering discipline, 100% PASS on `skill-doctor` audits |

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

Expected output:

```
SELFTEST PASS (all AST syntax, positive, negative, and integration checks passed)
```

Suggested first prompt after installing:

> Use github-oss-prep to scan this project. Output only the positioning card and the gap list — do not modify any files yet.

---

## 🔄 Open-Source Preparation Architecture

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

## 🧭 Seven Non-Negotiable Principles

1. **Audit before change, never blind overwrite**: preserve what works; if an existing file is outdated, incomplete, or risky, show the diff and rationale and wait for approval.
2. **Adapt to the project archetype**: Skills, code projects, and documentation projects each have different priorities — no generic template dumping.
3. **Align with GitHub community file standards**: the goal is a 100% score under Insights → Community.
4. **Runnable beats "complete"**: verify installation, minimal examples, tests, and packaging paths in a clean environment.
5. **PR by default, direct push optional**: publicly maintained projects go through branches, PRs, CI, and human review; solo bootstrap projects may push directly with explicit consent.
6. **Confirm before publishing**: show generated content for confirmation; remote repo, Release, package registries, and external promotion are each authorized separately.
7. **Existence is not quality**: never mark a file as acceptable just because it exists, and never erase a project's own voice to fit a template.

## 🧩 Step 0–7 Walkthrough

### Step 0 · Positioning and success criteria

Before touching any file, answer four questions from the project's existing material:

| # | Question | Requirement |
|---|---|---|
| 1 | **Who uses it** | Exactly one primary user group; at most two secondary groups |
| 2 | **What it solves** | Describe as "in situation X, it used to take N painful steps, now it takes M" |
| 3 | **Five-minute proof** | Define the minimal example a new user can reproduce, and its expected output |
| 4 | **Scope of this round** | Separate "prepare for open source", "publish to GitHub", "create a Release", and "promote externally" — never extend one approval into the next |

Output: a short **positioning card** — target users, core promise, minimal example, evidence, non-goals. See [`references/discovery-and-promotion.md`](references/discovery-and-promotion.md).

### Step 1 · Scanning the project

**1.1 Archetype detection**

| Signal | Archetype | Extra checks |
|------|------|-----------|
| `SKILL.md` present | AI Agent Skill | YAML frontmatter, references/ layout |
| `package.json` / `setup.py` / `Cargo.toml` present | Code project | CI/CD, build instructions, dependency declarations |
| Markdown only (no code) | Documentation / methodology | README quality and content structure |
| SKILL.md plus code | Skill + tooling | Treat as a Skill, plus executable script checks |

**1.2 Check against the official GitHub Community Profile**

| # | File | Location |
|---|------|------|
| 1 | Description | Set via GitHub UI / API at creation |
| 2 | README.md | Root / `.github/` / `docs/` |
| 3 | LICENSE | Root / `.github/` / `docs/` |
| 4 | CODE_OF_CONDUCT.md | Root / `.github/` / `docs/` |
| 5 | CONTRIBUTING.md | Root / `.github/` / `docs/` |
| 6 | SECURITY.md | Root / `.github/` / `docs/` |
| 7 | Issue / PR Templates | `.github/ISSUE_TEMPLATE/` |

### Step 2 · Assembling and improving files

> **Checkpoint**: show the Step 1 results (archetype + gap list) and wait for confirmation before creating files.

**Generation rules**
- Bilingual (Chinese-first projects may stay Chinese-only, but keep an English summary)
- Content precisely adapted to the archetype, never a generic template
- Briefly explain what will be created before creating it
- Score existing files on "accurate, clear, runnable, maintainable"; propose changes only when there is real benefit, with a summary or diff
- Never treat an existing file as acceptable just because it exists, and never flatten the project's original voice to match a template

| File | Key points |
|------|----------|
| README.md | Archetype-adapted, leads with core value, includes quick start and usage examples |
| LICENSE | Choose per archetype (MIT / Apache 2.0 recommended) |
| CODE_OF_CONDUCT.md | Contributor Covenant 2.1 |
| CONTRIBUTING.md | Contribution flow, branch conventions, PR guidelines |
| SECURITY.md | Private vulnerability reporting channel, response SLA, supported versions |

### Step 3 · Verification and review

> **Checkpoint**: show the files generated in Step 2 with content summaries, then run the review.

**3.1 Content quality review**

- [ ] README is understandable within 5 seconds and contains at least one runnable example
- [ ] No sensitive information (API keys, emails, internal paths)
- [ ] File references use correct relative paths; bilingual structures correspond
- [ ] Emoji icons improve readability; core capabilities are presented in tables
- [ ] README references LICENSE and stays under 512 KB
- [ ] No unresolved repository owner/name placeholders remain
- [ ] Download links target the repository's actual default branch

**3.2 Second-pass privacy verification** (final check before pushing, to catch leaks introduced in Step 2)

- [ ] No real API keys / tokens / secrets anywhere
- [ ] No real emails, phone numbers, national IDs, or file paths containing real usernames
- [ ] No private IPs, internal domains, or database connection strings
- [ ] Placeholders (such as `YOUR_API_KEY`, `example@xxx.com`) are not leaks — keep them

**3.3 Provenance, licensing and reproducibility gates**

- [ ] Code, reverse-engineering artifacts, images, fonts, audio, datasets, and sample content are all legally distributable
- [ ] Third-party dependencies, NOTICE, font/asset attributions and license files are complete
- [ ] Scan not just the working tree but the Git tree and reachable history that will be committed
- [ ] Install, run the minimal example, test, and build from a clean directory or a fresh clone, following the README
- [ ] Windows/macOS/Linux support is stated explicitly; untested platforms are flagged as unverified
- [ ] Every one-liner script has documented manual fallback steps and troubleshooting

> **P0 gates**: leaked secrets, unclear licensing, or irreproducible builds **block public release**. Methods and gates: [`references/pr-and-release-workflow.md`](references/pr-and-release-workflow.md).

### Step 4 · Repository facade and Description

Generate the repo summary by rule. **Rules + templates + examples + Topics guidance** live in [`references/description-guide.md`](references/description-guide.md).

Principles in short:
- Under 120 characters, shaped as `capability + highlight`
- No "a project for..." filler, no version numbers
- Pick the template matching the archetype

Also prepare:
- 5–12 accurate Topics, preferring terms your target users actually search
- A 1280×640 social preview plan that shows the purpose or the result
- Above-the-fold README content: one-line value + result image/GIF + shortest install + minimal example
- 3 real examples, or one 60–90 second demo

### Step 5 · Pushing to GitHub

**5.1 Show the confirmation checklist**: repo name, Description, Topics, file list — then **wait for explicit confirmation**.

**5.2 Create the repository and push**

Prefer the official GitHub connector already installed on your platform; otherwise use a GitHub CLI that has completed `gh auth login --web`; if neither is available, deliver a ZIP and web-upload instructions. Full flow: [`references/mcp-push-guide.md`](references/mcp-push-guide.md).

> **Repository metadata is mandatory, not optional**: after the remote repo is created or code is pushed, the confirmed Description and Topics must actually be set and read back from GitHub to verify. Listing topics in a reply is not enough. If the current auth method cannot modify metadata, mark each item `manual setup required` with the exact value and the web path.

Minimum post-publish verification: repository URL, visibility, default branch, Description, Topics, README/file tree, and latest CI status.

**5.3 Choose the change path**

| Path | When it applies | Flow |
|---|---|---|
| **`public-safe` (default)** | Publicly maintained projects, multiple collaborators | Short-lived branch off the latest default branch → AI edits, verifies, commits → push branch and open a Draft PR → present diff, verification results, remaining risk → human review → Squash Merge after CI passes |
| **`solo-fast` (optional)** | Single maintainer, low-risk change, explicit user consent | Push directly to the default branch |

**5.4 Authentication safety policy**

1. Prefer the official GitHub connector already installed on the current platform
2. If using a local GitHub CLI, only run `gh auth status` to check state
3. **Never** scan the user's home directory, editor config, or MCP config looking for tokens
4. If the user explicitly chooses a PAT, guide them to create a least-privilege credential on GitHub's official page

Credential options compared: [`references/github-pat-comparison.md`](references/github-pat-comparison.md). Least-privilege setup steps: [`references/github-pat-setup.md`](references/github-pat-setup.md).

### Step 6 · Release and multi-platform distribution

**6.1 Create the first GitHub Release**

Semantic versioning (SemVer): `vMAJOR.MINOR.PATCH`

| Change type | Version impact | Example |
|----------|----------|------|
| New feature | Minor bump | v1.0.0 → v1.1.0 |
| Bug fix | Patch bump | v1.1.0 → v1.1.1 |
| Breaking change | Major bump | v1.1.0 → v2.0.0 |

**Release contents**
- Title: `v version - short description`
- Notes: new features, fixes, known limitations, upgrade guidance
- Assets: source ZIP, checksums file, installers (if any)

**6.2 Multi-platform distribution**: match the publishing workflow to the archetype — `uv publish`, `npm publish`, `huggingface-cli upload`, Chrome Web Store submission, or Release assets. See [`references/release-and-distribution.md`](references/release-and-distribution.md).

**6.3 Version consistency verification**: the version number, CHANGELOG, badges, tags, Release title, and install links must all agree.

> Documentation-only or methodology projects may skip 6.2–6.3 and do 6.1 alone.

### Step 7 · Discovery and growth

**7.1 Prepare the Launch Kit** — rewrite from the same fact card per channel instead of copy-pasting one ad:

1. **One-liner**: user + pain + verifiable result
2. **Short post**: problem, demo, link, one clear question
3. **Long post**: why it exists, key trade-offs, demo, limitations, roadmap
4. **Assets**: social card, GIF/video, 3 screenshots, alt text
5. **Support**: install, FAQ, known issues, Issue/Discussion links

**7.2 Channel selection**

| Target users | Priority channels | Content focus |
|---|---|---|
| Developers / Agent users | GitHub Topics, technical communities, Show HN | Runnable demo, architecture, limitations, contribution entry points |
| Chinese developers | Juejin, V2EX, Zhihu, WeChat public accounts | Use cases, tutorials, real results, source links |
| Creators / non-technical users | Bilibili, Xiaohongshu, Product Hunt | Before/after comparison, demo video, templates, onboarding cost |

> Pick only **2–3** launch channels where your target users actually are, and follow each community's self-promotion rules.

**7.3 Release rhythm**

| Timing | Action |
|---|---|
| **T-7 to T-1** | Stranger testing, fix installation issues, prepare demo and FAQ |
| **T0** | Publish the Release, refresh Topics and the social card, then post to the first channels |
| **T+1 to T+7** | Answer issues quickly, log installation failure points, publish one improvement note |
| **T+30** | Set the roadmap from real feedback — never substitute star counts for real adoption |

> For early projects, **three strangers getting it running** is worth more than one short burst of exposure.

## 🚦 Checkpoints and Authorization Boundaries

| Stage | User confirmation | GitHub auth |
|---|---|---|
| Step 0–1 Positioning and scanning | Confirm the output | ❌ Not needed |
| Step 2 Generating community health files | **Checkpoint: confirm the gap list first** | ❌ Not needed |
| Step 3 Verification and privacy scan | **Checkpoint: confirm the file list first** | ❌ Not needed |
| Step 4 README / Description / Topics | Present values to be set | ❌ Not needed |
| Step 5 Pushing to GitHub | **Checkpoint: confirm repo name, Description, Topics, file list** | ✅ Needed |
| Step 6 Creating a Release / registry publish | **Checkpoint: authorize per platform** | ✅ Needed |
| Step 7 External promotion | **Checkpoint: authorize per channel** | ❌ Not needed |
| ZIP delivery / local packaging | No extra authorization | ❌ Not needed |

## 🧪 Built-in Tooling and Regression Tests

The skill ships with offline quality gates — no network, no third-party dependencies:

| Tool | Purpose | Command |
|---|---|---|
| `scripts/validate_repo.py` | Validates required files, relative-path references, leftover placeholders, and secrets; supports JSON output | `python scripts/validate_repo.py`<br>`python scripts/validate_repo.py --json` |
| `scripts/selftest.py` | Regression suite: AST syntax checks + positive validation + negative security assertions + pitfall-library depth assertions + integration test | `python scripts/selftest.py` |
| `tests/test_skill.py` | Pytest-discoverable entry wrapping the full selftest suite | `pytest tests/` |

**Continuous integration**: `.github/workflows/validate.yml` runs validation on every PR and every push to `main`, with permissions pinned to `contents: read` (top-level read-only, mitigating CI supply-chain poisoning).

## 📊 Deliverable Example: Layered Fact Card

After verification, the skill reports results as a standard Markdown layered fact card (example):

### 📊 github-oss-prep repository open-source readiness fact card

| Layer | Check | Measured value | Baseline | Verdict |
|---|---|---|---|:---:|
| L1 Privacy | Sensitive credentials / API keys | 0 hits | 0 leaks | 🟢 Pass |
| L1 Privacy | Local absolute path fingerprints | 0 hits | 0 exposed | 🟢 Pass |
| L2 Community | GitHub Insights seven-item set | 100% present | 100% complete | 🟢 Complete |
| L2 Community | YAML Issue Forms | Configured | Full YAML | 🟢 Standard |
| L3 Supply chain | CI top-level permissions read-only | contents: read | contents: read | 🟢 Safe |
| L3 Automation | scripts/selftest.py regression | 100% PASS | 0 blocked, 0 failed | 🟢 Passing |

【Governance and release recommendations (manual execution only, after explicit user authorization)】:
1. Only after the metrics above pass may the user authorize remote branch pushes and Release packaging
2. If historical commits contain sensitive data, revoke and rotate the token on the cloud platform first, and provide a rollback plan before rewriting history

## 📁 File Structure

```
github-oss-prep/
├── SKILL.md                          # Core skill definition: 7-step workflow, gates and delivery spec
├── README.md                         # Chinese documentation
├── README.en.md                      # English documentation
├── manifest.json                     # Single source of truth for the version (currently 3.2.0)
├── CHANGELOG.md                      # Version history following Keep a Changelog
├── LICENSE                           # MIT License
├── .gitignore                        # Git ignore rules
├── CONTRIBUTING.md                   # Contribution guide
├── CODE_OF_CONDUCT.md                # Code of conduct
├── SECURITY.md                       # Vulnerability disclosure channels and response SLA
├── SUPPORT.md                        # Support channels
├── agents/
│   └── openai.yaml                   # Codex / OpenAI platform metadata
├── references/                       # 11 progressive-disclosure reference guides
├── scripts/
│   ├── validate_repo.py              # Structure, hygiene & security validator
│   └── selftest.py                   # Automated regression test runner
├── tests/
│   └── test_skill.py                 # Pytest automated test suite entry
└── .github/
    ├── CODEOWNERS                    # Code owners config
    ├── pull_request_template.md      # Standard PR template
    ├── ISSUE_TEMPLATE/               # 3 interactive YAML forms + config
    │   ├── bug_report.yml            # Interactive Bug report form
    │   ├── doc_improvement.yml       # Documentation improvement form
    │   ├── feature_request.yml       # Interactive Feature request form
    │   └── config.yml                # Template selector config
    └── workflows/validate.yml        # Read-only permissions CI
```

## 📖 In-Depth Technical References

> Progressive disclosure: read only the guide for the stage you are in — no need to read them all.

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

## 🌐 GitHub Open Source Lifecycle Suite

A complete, production-ready toolchain for open-source maintainers and contributors:

| Stage / Role | Recommended Skill | Core Mission & Capabilities | GitHub Repository |
|---|---|---|---|
| 📦 **Pre-Launch Prep** | [**`github-oss-prep`**](https://github.com/hyt315/github-oss-prep) | Automated repository scaffolding, bilingual READMEs, CI workflows, and compliance checks | [hyt315/github-oss-prep](https://github.com/hyt315/github-oss-prep) |
| 🩺 **Quality Doctor** | [**`skill-doctor`**](https://github.com/hyt315/skill-doctor) | 50+ industrial static rules + dynamic selftest runner for 100% reliable Agent Skills | [hyt315/skill-doctor](https://github.com/hyt315/skill-doctor) |
| ⚙️ **Post-Launch Ops** | [**`github-oss-ops`**](https://github.com/hyt315/github-oss-ops) | Issue triage, AI hallucination defense, PR review, GHSA vulnerability SOP, and multi-channel broadcasting | [hyt315/github-oss-ops](https://github.com/hyt315/github-oss-ops) |
| 🚀 **Contributor Navigator** | [**`github-oss-contribute`**](https://github.com/hyt315/github-oss-contribute) | End-to-end contributor guide: Fork syncing, rebase conflict resolution, DCO signing, and anti-AI-slop gates | [hyt315/github-oss-contribute](https://github.com/hyt315/github-oss-contribute) |

## ❓ FAQ

- **Q: Do I need a GitHub Token for preparation and packaging?**  
  A: No. Scanning, privacy audits, community file generation, README creation, and ZIP packaging run entirely locally without tokens.
- **Q: Will it push anything to my GitHub automatically?**  
  A: No. Pushing, creating a Release, and external promotion are independent checkpoints that require your explicit approval. By default it only prepares locally and reports.
- **Q: Will it rewrite my codebase without asking?**  
  A: Never. The skill follows strict "audit before change" principles, requiring explicit approval before modifying any files.
- **Q: Does it support non-AI projects?**  
  A: Absolutely. It features 10 dedicated archetype engines covering MCP Servers, AI models, CLI tools, extensions, SDK libraries, IaC, fullstack apps, and curated lists.
- **Q: How do I verify the skill itself is healthy?**  
  A: `python scripts/selftest.py` runs syntax, positive, negative-security, and integration checks in one command; CI also runs it on every PR.
- **Q: What if a secret is found in my Git history?**  
  A: Revoke and rotate the credential on the platform first, then evaluate history rewriting — deleting a file is not the same as removing it from Git history. See the pitfalls guide.
- **Q: Why does `SKILL.md` remain lightweight?**  
  A: The skill follows the Progressive Disclosure Architecture, encapsulating deep domain templates into modular references to prevent LLM context over-saturation and cross-domain pollution.

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) first.

Make sure the repository passes its own checks before submitting:

```bash
python scripts/selftest.py
python scripts/validate_repo.py
```

Please do not file public issues for security vulnerabilities — report them privately per [SECURITY.md](SECURITY.md). If this skill helped you, please give it a [Star ⭐](https://github.com/hyt315/github-oss-prep/stargazers)!

## 🔒 Safety & Privacy Principles

- **Read-only by default / Audit Before Change**: local preparation scans read-only and produces a diff report; existing user files are never overwritten unilaterally.
- **Progressive Isolation**: only the relevant archetype references are loaded, preventing context pollution.
- **5-Layer Deep Defense**: comprehensive scans across code, docs, `.git/config`, and commit history to block any sensitive information.
- **Staged Approvals**: local preparation, remote repo creation, Release packaging, and external promotion are approved independently and never chained.
- **Zero token discovery**: never scans the home directory, editor config, or MCP config for credentials; only the official platform connector or an authenticated GitHub CLI is used.
- **Zero-token local runs / zero runtime dependencies**: the bundled scripts use only the Python standard library, adding no third-party packages and incurring no API costs.

## 📥 Download

| Method | Command / Link |
|---|---|
| **HTTPS** | `git clone https://github.com/hyt315/github-oss-prep.git` |
| **SSH** | `git clone git@github.com:hyt315/github-oss-prep.git` |
| **GitHub CLI** | `gh repo clone hyt315/github-oss-prep` |
| **ZIP** | [Download ZIP](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.zip) |
| **Tarball** | [Download Tar](https://github.com/hyt315/github-oss-prep/archive/refs/heads/main.tar.gz) |
| **Single file (SKILL.md)** | `curl -O https://raw.githubusercontent.com/hyt315/github-oss-prep/main/SKILL.md` |

## 📄 License

Licensed under the [MIT License](LICENSE).

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

> 🌏 **中文版: [README.md](./README.md)**