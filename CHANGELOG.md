# Changelog

All notable changes to `github-oss-prep` will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.2.0] - 2026-09-02

### Added
- **2026 现代终端 CLI 运行器全量支持 (`references/readme-template.md` & `references/release-and-distribution.md`)**：新增对 Python 现代免装运行器 `uvx`、持久隔离工具 `uv tool install`、`pipx`，前端即时运行器 `bunx`、`pnpm dlx`、`npx`，以及 Rust `cargo binstall` 预编译直装的全面支持与针对性模版。
- **跨平台单行脚本直装规范**：规范 `curl -fsSL ... | sh` 与 Windows PowerShell `irm ... | iex` 独立二进制安装方案。
- **精准针对性分流矩阵**：严格界定 AI Agent Skill（只走技能协议与 Agent 一句话自装）、Python CLI（走 `uvx/uv tool`）、Node CLI（走 `npx/pnpm dlx/bunx`）与系统二进制工具的分流规则，杜绝不匹配的安装方式。

## [2.1.0] - 2026-09-02

### Added
- Complete rich fusion: 6 full archetype README skeletons, all-channel package guides (npm, PyPI, Docker, Brew, Cargo, Go), CI/Dependabot templates, and real-leak comparison table.

## [2.0.0] - 2026-09-02

### Added
- Initial 2.0 release introducing 6 archetype engines, 5-layer deep security scanner, and YAML Issue Forms.

## [1.7.1] - 2026-08-22

### Changed
- Added reading-time guidance to SKILL.md Reference Map so AI models pick reference files predictably.
- Documented single-layer reference reading constraint.

## [1.0.0] - 2026-08-21

### Added
- Initial release of GitHub OSS preparation skill.
