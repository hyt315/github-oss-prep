# GitHub 2026 官方社区健康文件库与模板规范

> 对标：GitHub 官方社区健康文件口径（README/CODE_OF_CONDUCT/LICENSE/CONTRIBUTING 为点名文件、issue 模板可计分）与最小权限自动化流水线。**不要写"满分/百分比"这类非官方表述。**

---

## 目录

1. [现代交互式 YAML Issue Forms](#1-现代交互式-yaml-issue-forms)
   - [Bug 反馈表单 (`bug_report.yml`)](#11-bug-反馈表单-githubissue_templatebug_reportyml)
   - [需求建议表单 (`feature_request.yml`)](#12-需求建议表单-githubissue_templatefeature_requestyml)
   - [模板全局配置 (`config.yml`)](#13-模板全局配置-githubissue_templateconfigyml)
2. [合并请求模板 (`pull_request_template.md`)](#2-合并请求模板-githubpull_request_templatemd)
3. [安全策略 (`SECURITY.md`)](#3-安全策略-securitymd)
4. [GitHub Actions CI/CD 多版本矩阵工作流](#4-github-actions-cicd-多版本矩阵工作流)
5. [Dependabot 自动化依赖安全更新 (`dependabot.yml`)](#5-dependabot-自动化依赖安全更新-githubdependabotyml)
6. [代码规范与换行符文件 (`.editorconfig` / `.gitattributes`)](#6-代码规范与换行符文件-editorconfig--gitattributes)

---

## 1. 现代交互式 YAML Issue Forms

GitHub 官方已全面推荐使用 YAML 格式的 Issue Forms 替代传统 Markdown 模板。

### 1.1 Bug 反馈表单 (`.github/ISSUE_TEMPLATE/bug_report.yml`)
```yaml
name: "🐛 Bug 反馈 / Bug Report"
description: "报告一个错误或非预期行为 / Report a bug or unexpected behavior"
title: "[Bug]: "
labels: ["bug", "triage"]
body:
  - type: markdown
    attributes:
      value: |
        感谢提交 Bug 反馈！请尽可能提供可复现的详细信息。
  - type: textarea
    id: what-happened
    attributes:
      label: "问题描述 / Description"
      description: "发生了什么异常现象？"
      placeholder: "请详细描述问题的具体表现..."
    validations:
      required: true
  - type: textarea
    id: reproduction
    attributes:
      label: "复现步骤 / Reproduction Steps"
      description: "如何复现此问题？"
      placeholder: |
        1. 运行命令 '...'
        2. 传入参数 '...'
        3. 观察到错误 '...'
    validations:
      required: true
  - type: dropdown
    id: os
    attributes:
      label: "操作系统 / Operating System"
      options:
        - "Windows"
        - "macOS"
        - "Linux"
        - "Docker / 容器"
        - "其他 / Other"
    validations:
      required: true
  - type: checkboxes
    id: checklist
    attributes:
      label: "自查清单 / Checklist"
      options:
        - label: "我已确认使用的为最新版本"
          required: true
        - label: "我已在现有 Issue 中检索过，未发现重复问题"
          required: true
```

### 1.2 需求建议表单 (`.github/ISSUE_TEMPLATE/feature_request.yml`)
```yaml
name: "💡 功能建议 / Feature Request"
description: "提出新特性或优化建议 / Suggest a new feature or improvement"
title: "[Feature]: "
labels: ["enhancement"]
body:
  - type: markdown
    attributes:
      value: |
        感谢提出改进建议！请描述你的使用场景与预期方案。
  - type: textarea
    id: problem
    attributes:
      label: "背景与痛点 / Context & Problem"
      description: "在什么场景下遇到了什么困难？"
      placeholder: "当我尝试进行...时，发现缺少..."
    validations:
      required: true
  - type: textarea
    id: solution
    attributes:
      label: "建议的解决方案 / Proposed Solution"
      description: "你希望如何实现或改进？"
      placeholder: "建议增加...功能，或者优化..."
    validations:
      required: true
```

### 1.3 模板全局配置 (`.github/ISSUE_TEMPLATE/config.yml`)
**写法一（默认）：保留自由 Issue 入口**——模板没覆盖的反馈仍可提交。
```yaml
blank_issues_enabled: true
contact_links:
  - name: "📖 项目文档 / Documentation"
    url: "https://github.com/{owner}/{repo}#readme"
    about: "在提交 Issue 前请先查阅官方文档"
```

**写法二（强制走模板）：仅当已有第三种入口时使用**——必须同时提供 Question 模板，或把用户导向 Discussions；
否则等于堵住所有非模板反馈（本仓库采用写法二，因为 `config.yml` 里配了 Questions→Discussions 链接）。
```yaml
blank_issues_enabled: false
contact_links:
  - name: "💬 Questions & Discussions"
    url: "https://github.com/{owner}/{repo}/discussions"
    about: "提问请到 Discussions，不要开 Issue。"
```

---

## 2. 合并请求模板 (`.github/pull_request_template.md`)

```markdown
## 📝 变更说明 / Description

简要说明本次 PR 解决的问题或引入的新特性。

## 🎯 变更类型 / Type of Change

- [ ] 🐛 Bug 修复 (Bug fix)
- [ ] ✨ 新特性 (New feature)
- [ ] 📝 文档更新 (Documentation update)
- [ ] 🚀 性能优化 (Performance improvement)
- [ ] 🧪 测试用例 (Tests)
- [ ] ⚠️ Breaking Change (破坏性变更)

## 🧪 验证与测试 / Verification

- [ ] 本地自测通过 (`python scripts/selftest.py` 或对应测试套件)
- [ ] 文档与注释已同步更新
- [ ] 经确认无任何敏感信息或私有环境路径残留
```

---

## 3. 安全策略 (`SECURITY.md`)

```markdown
# 安全策略 / Security Policy

> 私有漏洞报告按钮需要在仓库 **Settings → Code security** 中启用（`GitHub Private Vulnerability Reporting`）；仅提交本文件不会自动开启该入口。

## 支持版本 / Supported Versions

| 版本 (Version) | 支持状态 (Supported) | 停止支持 (EOL) |
|---|---|---|
| 2.x（当前） | :white_check_mark: 接收修复 | 待定 |
| 1.x | :warning: 仅安全修复 | 2026-12-31 |
| < 1.0 | :x: 不接收 | 已停止 |

## 报告安全漏洞 / Reporting a Vulnerability

发现漏洞或敏感信息泄露风险时，**请勿公开发布 Issue**。请通过以下任一渠道私密通报：
- [GitHub Private Vulnerability Reporting](https://github.com/{owner}/{repo}/security/advisories/new)
- 邮件：`security@example.com`（若提供 PGP，请在此给出公钥指纹）

**受理范围**：本仓库代码与发布产物；**不在范围**：依赖项自身的已知漏洞（请上报上游）。
**响应节奏（按实际能力填写，不要承诺做不到的时限）**：确认收到 {N} 个工作日内；修复或缓解目标 90 天内，期间通过私密通报同步进展。
```

---

## 4. GitHub Actions CI/CD 多版本矩阵工作流

### 4.1 Node.js 矩阵 CI (`.github/workflows/ci-node.yml`)
```yaml
name: CI (Node.js)

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        # Node 18/20 均已 EOL（20 的 EOL 为 2026-04-30）；26 于 2026-10-28 转 LTS 后可加入
        # 滚动来源：https://endoflife.date/nodejs
        node-version: [22.x, 24.x]
    steps:
      # 外部 Action 一律锁定完整 commit SHA；由 Dependabot(github-actions) 负责滚动
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
      - name: Setup Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@820762786026740c76f36085b0efc47a31fe5020 # v7.0.0
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
      - run: npm ci
      - run: npm test
```

### 4.2 Python 矩阵 CI (`.github/workflows/ci-python.yml`)
```yaml
name: CI (Python)

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        # 3.10 的 EOL 为 2026-10-31，故从 3.11 起；3.14 于 2025-10-07 发布
        # 滚动来源：https://endoflife.date/python
        python-version: ["3.11", "3.12", "3.13", "3.14"]
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
      - name: Setup Python ${{ matrix.python-version }}
        uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97 # v7.0.0
        with:
          python-version: ${{ matrix.python-version }}
      - run: python -m unittest discover tests
```

---

## 5. Dependabot 自动化依赖安全更新 (`.github/dependabot.yml`)

> 限额口径（官方 options reference）：`open-pull-requests-limit` **只作用于版本更新**，默认 **5**、可调（设大值等于取消限制）；**安全更新不受该限制、无数量上限**。
> ⚠️ **只声明项目里真实存在的生态**：给没有 `package.json` 的仓库配 `npm`、没有 `pyproject.toml`/`requirements.txt` 的仓库配 `pip`，Dependabot 任务会以 failure 收场（本仓库实测踩过）。删掉用不到的段落，而不是留着当示例。

```yaml
version: 2
updates:
  # 监控 GitHub Actions
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
    groups:
      actions-dependencies:
        patterns:
          - "*"

  # ↓↓ 以下两段仅在项目真的存在对应清单文件时保留，否则删除（否则任务失败）
  # 监控 npm（需 package.json / package-lock.json）
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10

  # 监控 pip（需 pyproject.toml / requirements.txt）
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
```

---

## 6. 代码规范与换行符文件 (`.editorconfig` / `.gitattributes`)

### `.editorconfig`
```ini
root = true

[*]
charset = utf-8
end_of_line = lf
indent_size = 2
indent_style = space
insert_final_newline = true
trim_trailing_whitespace = true

[*.py]
indent_size = 4
```

### `.gitattributes`
```gitattributes
* text=auto eol=lf
*.png binary
*.jpg binary
*.webp binary
*.mp4 binary
*.zip binary
*.tar.gz binary
```
