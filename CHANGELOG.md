# Changelog

All notable changes to `github-oss-prep` will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-09-02

### Added
- **六大项目品类专属 README 模板引擎 (`references/readme-template.md`)**：全面提供针对 AI Agent 技能、系统与 CLI 工具、前端多媒体渲染、类库与 SDK、全栈 Web 应用、文档知识库的 6 大定制门面，彻底告别千篇一律。
- **五重严密环境与隐私安全审计引擎 (`references/privacy-scan.md` & `scripts/validate_repo.py`)**：深度拦截敏感 API 密钥、私有机器路径指纹 (`<user_home>`)、内部 Agent 会话 ID、Git Remote URL 凭据污染与构建垃圾缓存。
- **GitHub 2026 官方社区健康文件库 (`references/community-templates.md`)**：全面支持交互式 YAML Issue Forms (`bug_report.yml` / `feature_request.yml` / `config.yml`)，保障 100% 满分通过 GitHub Community Profile 考核。
- **全渠道现代分发与下载矩阵 (`references/release-and-distribution.md`)**：原生支持 `gh skill install`、Agent 一句话自装提示词、Release 预编译资产（附带 SHA-256 校验和）与包管理器路由。
- **轻量化主干重构 (`SKILL.md`)**：主文档大幅精简至 120 行以内，彻底消除 `SK005` 告警，规范单层 Reference Map 导航（附带阅读时机与预估耗时）。
- **全量回归自测套件 (`scripts/selftest.py`)**：全面覆盖 6 大品类检查与正反向安全断言，通过 `skill-doctor` 37 项全量规范审查（100% PASS）。

## [1.7.1] - 2026-08-22

### Changed
- Added reading-time guidance to SKILL.md Reference Map so AI models pick reference files predictably.
- Documented single-layer reference reading constraint.

## [1.0.0] - 2026-08-21

### Added
- Initial release of GitHub OSS preparation skill.
