# Changelog

All notable changes to `github-oss-prep` will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.1.0] - 2026-09-06

### Added
- **开源准备核心避坑库与官方规范基线 (`references/github-oss-prep-pitfalls.md`)**：
  - 深度聚合 GitHub 官方 2026 社区健康度 100% 门禁标准与 YAML Issue Forms 强约束规范；
  - 覆盖 Git 历史深水凭据残留机理与 `git-filter-repo` 现代洗库及协作者防二次污染三铁律；
  - 覆盖 GitHub Actions CI/CD 供应链投毒防御（顶层 `permissions: contents: read` 最小特权、锁定 40 位不可变 Commit SHA、防范 `pull_request_target` 与 Bash 注入）；
  - 覆盖开源许可证选型（MIT 专利真空 vs Apache 2.0 显式授权、GPL/AGPL 网络传染陷阱）与多生态发布不可变性（PyPI/npm 封禁覆盖机制）；
  - 覆盖极端特异性隐私脱敏（本地绝对路径、`.git/config` 内嵌 PAT 远程 URL、AI Agent 内部会话与调试标记）。
- **标准分层诊断事实卡 (Fact Card)**：在 `SKILL.md` 中规范标准 Markdown 分层事实卡，涵盖 L1 隐私安全、L2 社区健康、L2 社区规范、L3 供应链安全与 L3 自动化工程，提供确凿指标与授权发布门禁。
- **Pytest 自动化测试入口 (`tests/test_skill.py`)**：提供标准测试套件入口，支持自动化测试框架与 CI 集成。

### Changed
- **指令工程全面升级 (Inline Action Directives)**：彻底消除 `SKILL.md` 中的“详见/可参考”等弱引用，全量升级为 `👉 动作：读取 references/xxx.md` 就近内联动作指令。
- **只读安全原则与授权发布铁律**：严正确立纯只读排查与 Zero-Mutation 原则，破坏性操作与发布操作明确标注须经用户显式授权。
- **审计脚本工程硬化 (`scripts/validate_repo.py`)**：
  - 支持 `--json` 结构化机读导出与 `--quick` 快速采样；
  - 新增 GitHub Actions 供应链安全审计（检查 permissions 与第三方 Action SHA 锁定）；
  - 新增 `.git/config` 敏感远程凭据扫描与 SECURITY.md 检查。
- **自测套件增强 (`scripts/selftest.py`)**：
  - 集成 Python 原生 `ast.parse` 静态语法解析门禁；
  - 注入 `github-oss-prep-pitfalls.md` 存在性及关键避坑概念深度断言；
  - 强化破坏性负向样本测试（DY002）与集成 `validate_repo.py --json` 联测。

## [3.0.0] - 2026-09-02

### Added
- **十大全景开源项目品类覆盖体系 (`references/readme-template.md`)**：新增对 **MCP Server 协议端**、**AI 模型权重与数据集 (GGUF)**、**浏览器扩展与插件 (MV3)**、**基础设施代码与配置集 (IaC/Dotfiles/Helm)** 以及 **Awesome 精选清单** 的完整开箱即用 Markdown 骨架与专属代码块（`claude_desktop_config.json`、显存 VRAM 矩阵、Benchmark 跑分表、Manifest V3 权限表、架构拓扑图）。
- **渐进式披露架构 (Progressive Disclosure)**：确立渐进式披露为技能第一执行铁律——在 Step 3 门面生成时，AI 根据 Step 0 判定结果仅定向调阅对应品类的专属锚点章节，严禁通读全库，彻底杜绝上下文膨胀与跨品类交叉污染。
- **全生态发版实操指南升级 (`references/release-and-distribution.md`)**：扩充 Hugging Face / Ollama 模型发布、Chrome 网上应用店打包、MCP Server 发布与 Terraform/Helm 分发指令。

## [2.2.0] - 2026-09-02

### Added
- 2026 现代终端 CLI 运行器支持 (uvx, uv tool, bunx, pnpm dlx, cargo binstall) 与精准分流矩阵。

## [2.1.0] - 2026-09-02

### Added
- Complete rich fusion of 6 full archetype README skeletons, package guides, CI/Dependabot templates, and privacy scanner.

## [2.0.0] - 2026-09-02

### Added
- Initial 2.0 major overhaul.
