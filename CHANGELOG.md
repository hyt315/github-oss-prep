# Changelog

## [1.4.1] - 2026-07-18

### Fixed

- Made repository Topics and Description mandatory publication actions rather than recommendations.
- Added post-publish metadata read-back verification for connector and GitHub CLI modes.
- Required manual handoff to mark unset Topics as pending with copy-ready values instead of silently reporting completion.

## [1.4.0] - 2026-07-18

### Added

- Added project positioning, five-minute proof and adoption-readiness checks before repository publication.
- Added a `public-safe` branch/Draft PR/CI workflow and an explicit low-risk `solo-fast` option.
- Added provenance, asset licensing, clean-clone reproducibility and version-consistency release gates.
- Added repository discoverability, Launch Kit, channel selection and post-launch feedback guidance.
- Added self-modification safeguards for skills that prepare or publish themselves.

### Changed

- Replaced the rigid “only fill missing files” rule with approval-gated audits and improvements of weak existing files.
- Separated authorization for repository publishing, Releases, package registries and external promotion.
- Reframed Community Profile completeness as a baseline rather than the definition of release readiness.

### Security

- Removed the remaining example that embedded a GitHub Token in a remote URL.

## [1.3.0] - 2026-07-18

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
