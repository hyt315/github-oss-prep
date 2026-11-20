# Changelog

All notable changes to `github-oss-prep` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

_No unreleased changes._

## [3.4.0] - 2026-11-20

Major simplification and scanner bug-fix release. Replaced rigid template-heavy rules with a lightweight "must-have baseline + on-demand enhancements" architecture suited to modern AI models, while hardening `validate_repo.py` for real external repositories.

### Fixed

- **User-repo `tests/fixtures/` leak bypass**: Removed `"tests/fixtures"` from global `skip_paths` in `scripts/secret-rules.json`. Skipping fixtures now applies only when self-checking this skill repository, so secrets inside a user project's `tests/fixtures/` are caught as P0.
- **Target-repo baseline file reporting**: `validate_repo.py` now checks `README.md`, `LICENSE`, and `.gitignore` (plus optional community health files) on *any* target repository instead of only on `github-oss-prep` itself.
- **Streaming history scan**: Rewrote `scan_history()` to stream `git log -p` line-by-line via `Popen` while skipping lockfiles and ultra-long minified lines, preventing OOM/hangs on large repositories.
- **Hardened GitHub Actions checks**: Added detection for `permissions: write-all`, `pull_request_target`, and direct `${{ github.event.* }}` interpolation inside `run:` blocks.
- **Dangling references & doc drift**: Removed stale `见 13`, `github-upload`, empty `--pin`, outdated `scan_file_safety` snippet, and contradictory automation claims.

### Changed

- **Lightweight 4-step workflow & 2 gates**: Simplified `SKILL.md` into "must-have baseline" (security scan, runnable README, LICENSE, `.gitignore`, metadata) vs "on-demand enhancements" (community files, CI, multi-channel distribution, promotion).
- **Consolidated `references/` (22 files → 4 files)**: Replaced 10 rigid README skeletons (`references/readme-templates/`), the 12×3×7 taxonomy router, and 3 overlapping push/PAT docs with 4 concise guides (`readme-and-archetypes.md`, `security-and-pitfalls.md`, `community-and-ci.md`, `publishing-and-release.md`).
- **Modern Agent Skill install paradigm**: Added `npx skills add` alongside copy-to-AI one-liner installation and manual `git clone`, and added `agentskills.io` frontmatter key validation for any target repo containing `SKILL.md`.
- **Single test entry**: Merged `scripts/selftest.py` into `tests/test_skill.py` and simplified `.github/workflows/validate.yml` to run `unittest` once plus `validate_repo.py --strict --history`.

### Removed

- `references/readme-templates/` (10 rigid skeleton files) and `check_template_quality` / `reference-size-drift` self-linting checks in `validate_repo.py`.
- `scripts/selftest.py` (consolidated into `tests/test_skill.py`).

## [3.3.3] - 2026-11-12

Patch release: scanner calibration. The release gate `validate_repo.py --strict --history` now passes on clean projects and catches personal data it used to miss.

### Fixed

- **Placeholders no longer block a release.** The `<owner>`/`<repo>` rule raised P0 even inside code blocks, although SKILL.md treats placeholders as safe. It is removed; `{owner}`/`{repo}` left in shipped docs are still caught by `placeholder-unresolved`.
- **Path rules ignore placeholders and system folders.** `windows-user-profile-path` skips `<user>`, `YourName`, `username`, `%USERNAME%`, `Public`, `Default` and similar; `unix-home-path` skips `user`, `you`, `runner` and similar. `windows-absolute-path` is now P2 (informational) and ignores `C:\Windows`, `C:\ProgramData`, `C:\Program Files`. On a real Windows-tooling project, strict tree P1 dropped from 92 to 1. <!-- scan-ignore: windows-absolute-path (规则说明本身) -->
- **`--strict` no longer fails on history it cannot fix.** P1 found only in git history is reported but does not block; P0 in history still blocks. The documented gate `--strict --history` failed on this repository itself (24 history P1); CI now runs it as one step.

### Added

- `personal_patterns` in `secret-rules.json`: personal mailbox addresses (qq, 163, 126, foxmail, gmail, outlook, …) and mainland China mobile numbers, both P1. SKILL.md has always required both to be absent; until now neither was scanned.
- A non-noreply commit email on a personal mailbox domain is now P1 in the history scan (was P2).
- Tree, `.git/config` and history scans share one matcher (`_match_line`), so a rule behaves the same everywhere.

## [3.3.2] - 2026-11-08

Patch release: fixes and tightening only, no new workflow steps.

### Security

- Rewrote environment-specific push docs into conditional, machine-neutral steps; moved tokens out of argv into one-shot credential helpers and stdin headers.
- Added `local_env_patterns`, `--history` scanning, `.git/config` remote token check, and CI SHA pinning checks. <!-- scan-ignore: machine-specific-claim (规则说明本身) -->

## [3.3.1] - 2026-09-19

- Scoped `.github/dependabot.yml` to `github-actions` only and enforced creating GitHub Release objects alongside tags.

## [3.3.0] - 2026-09-19

- Introduced `scripts/secret-rules.json` as single source of truth, regression fixtures, explicit `scan-ignore` suppression reporting, and generic `validate_repo.py <dir>` support.

## [3.2.0] - 2026-09-18

- Added `public-safe` / `solo-fast` launch modes, CI validation workflow, and metadata read-back checks.

## [3.1.0] - 2026-09-06

- Made GitHub authentication optional for local preparation and added offline ZIP handoff.

[3.4.0]: https://github.com/hyt315/github-oss-prep/releases/tag/v3.4.0
[3.3.3]: https://github.com/hyt315/github-oss-prep/releases/tag/v3.3.3
[3.3.2]: https://github.com/hyt315/github-oss-prep/releases/tag/v3.3.2
[3.3.1]: https://github.com/hyt315/github-oss-prep/releases/tag/v3.3.1
[3.3.0]: https://github.com/hyt315/github-oss-prep/releases/tag/v3.3.0
[3.2.0]: https://github.com/hyt315/github-oss-prep/releases/tag/v3.2.0
[3.1.0]: https://github.com/hyt315/github-oss-prep/releases/tag/v3.1.0
