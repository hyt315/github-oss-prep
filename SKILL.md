---
name: github-oss-prep
description: "Use when preparing, auditing, polishing, or publishing a project for open-source release on GitHub. Triggers include GitHub 开源准备、准备发布到 GitHub、开源化、美化仓库、oss prep, publish to GitHub, and prepare for open source."
license: MIT
metadata:
  version: "3.4.0"
---

# GitHub 开源准备

把项目整理成安全、清晰、可运行的 GitHub 开源仓库：**守住安全与可运行底线（必做），按项目体量选配社区与分发增强项（锦上添花），最后按授权推送发版。**

## 核心原则

- **先审后改**：保留项目原有有效内容与表达风格，不为了套模板强行改写。
- **必要项与锦上添花分层**：小项目保持精炼，只补必要项；长期维护或多人协作项目再按需补治理文件、CI 与推广素材。
- **安全与可运行是硬底线**：脚本先做确定性扫描，发现真实凭据或高危风险（P0）直接阻断；干净目录下按 README 能跑通比文件凑满更重要。
- **不带走作者本机信息**：交付物不含真实密钥、个人邮箱/手机号、含真实用户名的本机路径、代理端口和「在我电脑上实测」类环境快照。
- **两道确认闸**：改文件前确认改动清单；对外发布/推送前确认仓库名、可见性、元数据与扫描结果。若用户额外要求推广，再单独确认推广文案。

## 工作流程

```
Step 1 扫描与定边界 →【闸 1：改文件前】→ Step 2 必要项整理 → Step 3 锦上添花（按需）→【闸 2：对外发布前】→ Step 4 授权发布与回读
```

### Step 1：扫描与定边界

1. **运行确定性扫描**：
   ```bash
   python scripts/validate_repo.py <项目目录> --strict --history
   ```
   记录当前树 P0/P1、历史 P0/P1（历史 P1 仅报告，是否重写历史由用户决定）、以及缺失的基础文件清单。
2. **人工复核脚本盲区**：检查自定义密钥、AI 会话标记/临时目录、真实姓名与第三方素材许可链（见 `references/security-and-pitfalls.md`）。
3. **识别形态与边界**：根据仓库代码直接判断所属大类与风险开关（见 `references/readme-and-archetypes.md`），明确本次只做到「本地整理」还是包含「推送 GitHub / 发 Release / 对外推广」。
4. **过【闸 1】**：向用户汇报扫描结果、拟新增/修改文件清单，获批后再动手改文件。

### Step 2：必要项整理（默认必做）

- **清理风险**：修复所有 P0 与当前树 P1；若历史提交含真实凭据，先提醒用户在平台轮换吊销，再经确认决定是否用 `git-filter-repo` 清理。
- **写好 README**：遵循 `references/readme-and-archetypes.md` 的必要项（一句话价值、真实效果图或输出、最短安装与最小可跑示例、协议）和对应形态的现代安装范式（例如 AI Skill 默认提供「一句话发给 AI 自装」+ `npx skills add` + 手动 clone）。
- **补齐基础文件**：确保根目录有合适协议的 `LICENSE`（代码常用 MIT/Apache-2.0；文档与素材用 CC-BY-4.0/CC0；模型遵循上游许可链）和 `.gitignore`。
- **草拟门面元数据**：准备 120 字符以内的 Description 与 5–10 个成熟 Topics。
- **验证可运行**：在干净目录按 README 验证安装与最小示例；未测试的平台或步骤如实标「未验证」，绝不编造输出。

### Step 3：锦上添花项（按需选用，不强行塞满）

仅在项目体量、协作需求或用户明确要求时按需添加：

- **社区治理与 CI**：`SECURITY.md`、`CONTRIBUTING.md`、`CODE_OF_CONDUCT.md`、YAML Issue Forms、PR 模板、锁定 40 位 SHA 且顶层只读的 GitHub Actions CI、以及**仅声明真实存在生态**的 `dependabot.yml`（见 `references/community-and-ci.md`）。
- **双语文档与门面增强**：拆出独立 `README.en.md` / `README.md` 互链、1280×640 社交预览图、有效动态徽章。
- **多生态分发与推广**：PyPI (`uv`) / npm / Hugging Face / Docker / Release 资产校验和，或精简 Launch Kit（见 `references/publishing-and-release.md`）。

### Step 4：授权发布与回读（仅用户要求发布时执行）

1. **过【闸 2】**：复跑 `python scripts/validate_repo.py <项目目录> --strict --history`，向用户展示最新扫描结果、改动摘要、仓库名、可见性、Description、Topics 与版本号。
2. **只读探测选路**：按 `references/publishing-and-release.md` 先做只读环境探测（官方连接器 / `gh` / `GITHUB_TOKEN` / 网络可达性），绝不扫描主目录找 token、绝不把 token 写进 URL 或落盘；无认证时打包干净源码 ZIP 交付。
3. **推送与元数据回读**：已有公开仓默认走分支 + PR（`public-safe`），单人低风险改动经同意可直推（`solo-fast`）；推送后必须设置 Description 与 Topics 并从 GitHub 回读核对。
4. **发版（如需）**：按 SemVer 打 tag 并创建正式 GitHub Release（只推 tag 不算发版），核对版本号与安装命令一致。

## Reference Map

- [README 原则、形态增量与门面规范](references/readme-and-archetypes.md)：必要项 vs 锦上添花、6 大形态与 3 个风险开关、现代安装范式（一句话自装 / `npx skills add` / `uvx`）、Description 与 Topics。
- [安全底线、隐私扫描与高频避坑](references/security-and-pitfalls.md)：脚本自动范围与人工盲区、Git 历史洗库、CI 供应链加固、许可误区。
- [社区健康文件与 CI 按需参考](references/community-and-ci.md)：按需治理文件、YAML Issue Forms、SHA 锁定 CI 样例、Dependabot。
- [发布、推送、发版与推广指引](references/publishing-and-release.md)：只读探测与选路、一次性凭据推送、PAT 速查、Release 规范、多生态分发与可选推广。

> English overview: see [README.en.md](README.en.md).
