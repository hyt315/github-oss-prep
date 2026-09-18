# Changelog

All notable changes to `github-oss-prep` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

[1.3.0]: https://github.com/hyt315/github-oss-prep/releases/tag/v1.3.0
[1.4.0]: https://github.com/hyt315/github-oss-prep/releases/tag/v1.4.0
[1.4.1]: https://github.com/hyt315/github-oss-prep/releases/tag/v1.4.1
