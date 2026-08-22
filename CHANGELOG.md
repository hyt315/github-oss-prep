# Changelog

## [1.7.0] - 2026-08-22

### Fixed

- SKILL.md 中 4 处"给用户项目生成的目标文件"裸路径（dependabot.yml / ci.yml / release.yml / .obsidian/workspace.json）改为明确的"写入目标仓库"表述——此前会被误读为本仓库缺失的文件（skill-doctor LK002 检出）。
- 隐私扫描章节"扫描文件过多"措辞调整，消除与 PAT 数量上限的数字对撞误报（CK001）。

### Added

- readme-template 与 SKILL.md：Skill 类项目 README 必须含「复制一段话给 Agent 自装」引导，并逐字核对（2026-08-21 定稿，随本版本正式发版）。

## [1.6.2] - 2026-08-21

### Fixed

- **README 双语切换链接颠倒**：语言切换的链接文字与目标文件写反（在中文页点"简体中文"会进英文页、在英文页点"English"会回中文页）。已改为「当前页语言 = 纯文本、目标语言 = 可点链接且链接文字写目标语言」：中文页 `简体中文 · [English](README.en.md)`、英文页 `English · [简体中文](README.md)`；同步修正 `references/readme-template.md` 的语言切换规则，避免今后生成的仓库再犯同类错误。

## [1.6.0] - 2026-08-21

### Fixed

- **CI 模板版本矩阵去 EOL**：Node `[18,20,22]` → `[22,24]`（18/20 已停止安全支持）；Python `[3.9,...]` → `[3.10,3.11,3.12,3.13]`（3.9 EOL）；`requires-python >=3.8` → `>=3.10`；Docker `node:18-alpine` → `node:22-alpine`。
- **`validate_repo.py` 隐私门禁盲区**：扫描后缀扩展到源码（`.js/.ts/.sh/.toml/.env` 等）并纳入 AWS/私钥等密钥模式，修复"核心卖点是隐私扫描却漏检 `.env` 和源码"的问题。
- **`validate_repo.py` 与项目类型规则冲突**：按 SKILL.md 的项目类型（skill/code/docs）条件校验强制文件，文档项目不再因缺 COC/SECURITY/CHANGELOG 而误报；CHANGELOG 缺失时容错。
- **裸宽 except 收敛**：`except Exception` → `except OSError`（读文件容错更明确，不再吞一切异常）。

### Added

- **`scripts/selftest.py`** 回归入口（好夹具全绿 + 负向夹具必须 FAIL），并在 SKILL.md 新增「维护者自测」节挂载 `validate_repo.py`（修掉"脚本在 CI 跑、文档从不提"的孤儿状态）。
- **Git 作者隐私审计**（`privacy-scan.md`）：`git log` 作者身份核查、noreply 匿名邮箱、`git filter-repo` 历史清理。
- **License 决策补全**（SKILL.md）：加入 GPL/AGPL/LGPL（copyleft）、CC0/CC BY-SA（内容），并将 Apache 2.0 的卖点修正为"专利授权"，而非笼统"代码保护"。
- **演示素材真实性规则**：禁单帧静态图冒充 GIF、禁挪用/杜撰跨平台与性能数据。
- **可选自动化发布**（SKILL.md 6.1a）：release-please / semantic-release 与既有 Conventional Commits 闭环。
- **中文 Windows 用户名路径检测**（`privacy-scan.md` + `validate_repo.py`）：覆盖 `C:\Users\张三` 形态，并把 `YourName` 占位符例子从"泄露"修正为"占位符安全"。
- `SUPPORT.md`、`.github/CODEOWNERS` 交付模板；`.gitignore` 补 `.mimosa/`、`audit-report.txt`、`nul`、`__pycache__`。

### Changed

- Topics 推荐统一为 5–10 个（原 SKILL.md 5–12 / description-guide 5–8 打架）。
- README 徽章示例改为动态 shields 标签（`/github/v/release/...`），避免版本写死失真。
- 技能自身 README 补齐第 6 种下载方式（curl 单文件）与文件结构（agents/、scripts/、workflows/、CHANGELOG 等漏列项）。
- Go 发布命令修正为完整模块路径 + `@version`（裸 `go install xxx` 无效）。

## [1.5.0] - 2026-07-26

### Added

- Repository setup now recommends a tag-protection Ruleset (`refs/tags/v*`, block deletion and forced updates) after the first release, so published version tags cannot be accidentally removed or rewritten.
- Release gate note: dependency vulnerability audits (e.g. `npm audit`) must run against the official registry or inside CI — mirror registries commonly lack the audit endpoint and fail silently, hiding high-severity advisories until CI.

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
[1.5.0]: https://github.com/hyt315/github-oss-prep/releases/tag/v1.5.0
[1.6.0]: https://github.com/hyt315/github-oss-prep/releases/tag/v1.6.0
