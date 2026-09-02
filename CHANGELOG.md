# Changelog

All notable changes to `github-oss-prep` will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2026-09-02

### Added
- **六大品类完整 README 模板库 (`references/readme-template.md`)**：提供针对 AI Agent 技能、系统 CLI 工具、前端多媒体生成、类库 SDK、全栈 Web 应用、文档知识库的完整、可直接复制填空的开箱即用 Markdown 骨架与多平台安装表（npm / pip / cargo / winget / scoop / brew / docker / agent 自装）。
- **全平台包管理与多渠道发版实操指南 (`references/release-and-distribution.md`)**：详尽恢复并扩充 npm、PyPI、Docker/ghcr.io、Homebrew、Crates.io、Go 模块的具体发布命令、配置文件示例（`.npmignore` / `pyproject.toml`）、SHA-256 Checksums 校验与国内镜像加速方案。
- **自动化 CI/CD 与 Dependabot 模板 (`references/community-templates.md`)**：新增 Node.js / Python 多版本矩阵测试 GitHub Actions CI 工作流与 `.github/dependabot.yml` 依赖安全自动更新配置。
- **真伪泄露案例比对表 (`references/privacy-scan.md`)**：新增详尽的“真实泄露 vs 安全占位符”实战对照表与白名单判定准则。
- **环境卫生与构建隔离**：`.gitignore` 强化对本地体检报告 (`audit-report.txt`)、临时日志与各语言构建缓存的严格隔离，确保零泄露。

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
