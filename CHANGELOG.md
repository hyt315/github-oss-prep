# Changelog

All notable changes to `github-oss-prep` will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
