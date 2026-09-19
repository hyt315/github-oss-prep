# Changelog

All notable changes to `github-oss-prep` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

_No unreleased changes._

## [3.3.1] - 2026-09-19

### Fixed

- `.github/dependabot.yml` 收敛为仅 `github-actions`：本仓库没有 `package.json`/`pyproject.toml`，而 `v3.3.0` 的快照照抄了模板里的 `npm` 与 `pip` 段，导致 `bec570b` 上 `pip` 与 `npm_and_yarn` 各 2 次 Dependabot 任务 failure（`github-actions` 两次均 success，已 API 回读确认）。`v3.3.1` 的 tag 快照即为修好的配置。
- `references/community-templates.md` 补记该教训：**只声明项目里真实存在的包生态**，删掉用不到的段落而不是留作示例。

### Changed

- 发布纪律：`v3.3.0` 只推了 tag、没有 Release 对象（发行版页面停留在 v3.2.0），本轮补上 `v3.3.1` 的 GitHub Release，并把"tag + Release 两步都要做、且回读"写进流程。

## [3.3.0] - 2026-09-19

### Added

- **Taxonomy router**: new `references/category-map.md` is now the single classification source (12 archetypes + audience/lifecycle axes + flags + decision algorithm + router regression cases), replacing the three non-mapping schemes (4 / 9 / 10 types) that previously coexisted.
- **README template judgement layer**: 12-section universal base, pre-flight fact checklist, and per-blank `<!-- 判据 / 反例 / 可删 -->` guidance; a 品类增量 table mapping `category_id` → skeleton or deltas; `dataset`, `env-config` and `ci-automation` are explicitly marked as having no dedicated skeleton.
- **Template quality gates** in the validator: `tpl-guidance-density`, `tpl-real-output`, `tpl-hardcoded-license`, `tpl-badge-semantics`, `placeholder-unresolved` (shipped docs must resolve `{owner}`/`{repo}`) and `anchor-missing`.
- **Single-source secret scanning**: `scripts/secret-rules.json` is now the only place scanner patterns live; coverage extended to `sk-proj-`/`sk-ant-`, AWS `AKIA`/`ASIA`, Google `AIza`, Hugging Face, npm, PyPI, Slack, SendGrid, Telegram, JWT, Azure keys, PKCS#8 private-key blocks, credential-in-URL and blocked filenames.
- **Regression fixtures**: `tests/fixtures/leaked-repo/` proves real-format credentials are detected; `tests/fixtures/clean-repo/` guards against false positives.
- **Explicit suppression mechanism**: inline `<!-- scan-ignore: <rule-id> (reason) -->`; every suppression is reported as a P2 finding.
- **Generic validator**: `scripts/validate_repo.py` now accepts any target directory, reports severity-graded findings (`P0/P1/P2`, `--strict`, `--format text|json|md`), scans placeholders repo-wide and resolves relative Markdown links.
- **Publishing probe**: Step 5 starts with a read-only environment probe (connector / `gh` / network / token) and hands off to the sibling `github-upload` flow when the local path cannot work.

### Changed

- **Community-health wording** rewritten to the official baseline (README / CODE_OF_CONDUCT / LICENSE / CONTRIBUTING, issue templates counted; no "7-piece / 100%" claim).
- **Delivery fact card** values are now placeholders with a "measure-or-say-unmeasured" rule instead of hard-coded green marks.
- **Refreshed commands and versions**: `hf auth login` / `hf upload` (replaces the retired `huggingface-cli`), Node CI matrix `[22.x, 24.x]`, Python `["3.11"–"3.14"]`, Actions pinned to full SHAs (checkout v7.0.1, setup-node/setup-python v7.0.0), Contributor Covenant 3.0, Keep a Changelog 1.1.0, removed the dead `ghproxy.com` suggestion.
- **SemVer table** completed with 0.y.z, pre-release and build-metadata rules; Topics guidance unified to 5–10.
- **Placeholders normalized** to `{owner}` / `{repo}` across the repository, and the two shipped files that need concrete values (`SECURITY.md`, `CONTRIBUTING.md`) now carry the real repository URLs.
- **Dead template anchors fixed**: the category-1 skeleton linked `English`/`Chinese` to headings that do not exist there; it now points at the bilingual README files, and the Awesome-list skeleton gained the two sections its own table of contents promised.
- **Badge semantics fixed**: License badges derive from the taxonomy's default column instead of hard-coding MIT; platform badges point at a real compatibility section and release badges at the releases page.
- **Dogfooding**: README gains "Known limitations" and "Support" sections (the skill's own §9/§11 rule), and `README.en.md` was re-synced with the Chinese README (table header, sizes, new sections).
- RFC1918 scanner rule now validates octets (previously `10.669.606.225` matched); the link checker ignores inline code spans.
- **Two adversarial review rounds** were run against this plan set and are recorded in `优化参考/15-核查对照表.md`; five claims of mine were refuted there and corrected across the docs.

### Fixed

- `SECURITY.md` / `CONTRIBUTING.md` no longer ship unresolved owner/repo placeholder tokens, and the dangling "Question issue template" reference was removed.
- `CHANGELOG.md` link definitions aligned with actual sections.

### Security

- Scanner now catches current credential formats that previously bypassed the gate (proven by fixtures); historical `skill-doctor: allow` markers replaced by the explicit, reported suppression syntax.

---

## [3.2.0] - 2026-09-18

### Added

- **Complete 7-step workflow** with Step 0 (positioning) and Step 7 (discovery & growth)
- **Adoption-safe launch patterns**: `public-safe` branch/PR workflow and explicit `solo-fast` option
- **Comprehensive promotion strategy**: Stranger test, Launch Kit, channel selection, release rhythm
- **CI automation**: GitHub Actions workflow for automated validation
- **Topics verification mechanism**: Mandatory metadata publication and read-back verification
- **Provenance and reproducibility gates**: Asset licensing, clean-clone verification, version consistency

### Changed

- **Updated SKILL.md**: Streamlined from 420 to 291 lines while preserving all essential content
- **Enhanced validate_repo.py**: Added JSON output support and improved secret detection exclusions
- **Refined selftest.py**: Fixed parameter passing and adjusted line count limit to 300

### Merged Improvements

- Integrated improvements from `feat/open-source-adoption-flow` branch
- Integrated fixes from `fix/require-topics-publication` branch
- Cleaned up feature branches after merging

---

## [3.1.0] - 2026-09-06

### Added

- Added `Prepare only`, official GitHub connector, GitHub CLI and manual handoff modes.
- Added Codex-compatible `agents/openai.yaml` metadata.
- Added a guaranteed local ZIP delivery path when GitHub authentication is unavailable.

### Changed

- Made authentication optional for scanning, privacy checks, documentation generation and packaging.
- Switched publishing guidance to GitHub's maintained `github/github-mcp-server` or browser-based `gh auth login --web`.
- Updated the bilingual README to explain safe authentication and offline delivery.

### Security

- Removed automatic token discovery from user directories and MCP configuration files.
- Removed token-bearing Git remote URLs and instructions that display credentials.

[3.3.1]: https://github.com/hyt315/github-oss-prep/releases/tag/v3.3.1
[3.3.0]: https://github.com/hyt315/github-oss-prep/releases/tag/v3.3.0
[3.2.0]: https://github.com/hyt315/github-oss-prep/releases/tag/v3.2.0
[3.1.0]: https://github.com/hyt315/github-oss-prep/releases/tag/v3.1.0
