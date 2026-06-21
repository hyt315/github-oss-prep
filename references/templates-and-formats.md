# 模板和格式规范

> 本文件包含开源项目中常用的配置文件模板和格式规范。SKILL.md 直接引用本文件。

---

## 目录

- [CHANGELOG.md 格式（代码项目）](#changelogmd-格式代码项目)
- [Issue 模板格式详解](#issue-模板格式详解)
- [.editorconfig 模板](#editorconfig-模板)
- [.gitattributes 模板](#gitattributes-模板)
- [GitHub Actions CI/CD 模板](#github-actions-cicd-模板)
- [Dependabot 完整配置示例](#dependabot-完整配置示例)
- [什么项目不需要这么全](#什么项目不需要这么全)

---

## CHANGELOG.md 格式（代码项目）

推荐使用 **Conventional Commits** 格式，与 Semantic Versioning 配合：

**Commit 格式**：`<type>(<scope>): <description>`

| Type | 说明 | 版本影响 |
|------|------|----------|
| `feat` | 新功能 | minor |
| `fix` | Bug 修复 | patch |
| `docs` | 文档变更 | — |
| `style` | 代码格式（不影响功能） | — |
| `refactor` | 重构（无功能变更） | — |
| `perf` | 性能优化 | patch |
| `test` | 测试相关 | — |
| `build` | 构建系统变更 | — |
| `ci` | CI 配置变更 | — |
| `chore` | 其他杂项 | — |

**CHANGELOG 示例**：
```markdown
# Changelog

## [1.2.0] - 2026-06-06

### Added
- feat: 新增 YAML 表单支持 (#123)

### Fixed
- fix: 修复 Windows 路径解析问题 (#124)

### Changed
- docs: 更新 README 安装说明

## [1.1.0] - 2026-05-01

### Added
- feat: 新增批量处理功能 (#120)

### Fixed
- fix: 修复内存泄漏问题 (#121)
```

**GitHub 自动生成 Release Notes**：
- 创建 Release 时点击 "Generate release notes" 按钮
- 基于 PR 标题和标签自动生成
- 可自定义模板：`.github/release.yml`

---

## Issue 模板格式详解

GitHub Issue 模板使用 `.github/ISSUE_TEMPLATE/` **目录**（不是单个文件），支持两种格式：

**目录结构**：
```
.github/
└── ISSUE_TEMPLATE/
    ├── bug_report.md          # Markdown 格式模板
    ├── feature_request.yml    # YAML 表单格式（推荐）
    └── config.yml             # 可选：模板选择器配置
```

**Markdown 模板示例**（`.md`）：
```markdown
---
name: Bug Report
about: Report a bug
title: '[BUG] '
labels: bug
assignees: ''
---

## Bug Description
<!-- Describe the bug -->

## Steps to Reproduce
1. 
2. 

## Expected Behavior
<!-- What should happen -->

## Actual Behavior
<!-- What actually happened -->
```

**YAML 表单示例**（`.yml`，推荐）：
```yaml
name: Bug Report
description: Report a bug
title: "[BUG] "
labels: ["bug"]
body:
  - type: textarea
    id: description
    attributes:
      label: Bug Description
      description: Describe the bug
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: Steps to Reproduce
      description: Steps to reproduce the behavior
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: Version
      description: What version are you using?
      placeholder: "v1.0.0"
  - type: dropdown
    id: os
    attributes:
      label: Operating System
      options:
        - Windows
        - macOS
        - Linux
  - type: upload
    id: screenshot
    attributes:
      label: Screenshot
      description: Attach a screenshot if applicable (images max 10MB)
  - type: checkboxes
    id: terms
    attributes:
      label: Code of Conduct
      description: By submitting, you agree to follow our Code of Conduct
      options:
        - label: I agree to follow this project's Code of Conduct
          required: true
```

> `upload` 类型支持文件上传：图片（png/jpg/gif/svg/webp，10MB）、文档（pdf/docx/xlsx，25MB）、视频（mp4/mov/webm，100MB）、压缩包（zip/gz，25MB）。

**config.yml 配置**（可选）：
```yaml
blank_issues_enabled: false  # 禁用空白 Issue
contact_links:
  - name: Documentation
    url: https://example.com/docs
    about: Check the documentation first
```

---

## .editorconfig 模板

```ini
# EditorConfig: https://editorconfig.org
# 统一缩进、行尾、编码，确保多人协作代码风格一致

root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true

[*.{js,ts,jsx,tsx,json,yml,yaml,css,html,md}]
indent_style = space
indent_size = 2

[*.py]
indent_style = space
indent_size = 4

[Makefile]
indent_style = tab
```

---

## .gitattributes 模板

```gitattributes
# 自动检测文本文件并统一行尾
* text=auto

# 明确标记文本文件
*.md text
*.js text
*.ts text
*.py text
*.json text
*.yml text
*.yaml text
*.css text
*.html text

# 二进制文件（不做行尾转换）
*.png binary
*.jpg binary
*.jpeg binary
*.gif binary
*.ico binary
*.pdf binary
*.zip binary
*.gz binary

# 语言统计修正（排除 vendored 代码）
docs/* linguist-documentation
*.min.js linguist-vendored
```

---

## GitHub Actions CI/CD 模板

### Node.js CI 模板

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, master]
  pull_request:
    branches: [main, master]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [18, 20, 22]

    steps:
      - uses: actions/checkout@v4
      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
      - run: npm ci
      - run: npm run build --if-present
      - run: npm test
```

### Python CI 模板

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, master]
  pull_request:
    branches: [main, master]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.9', '3.10', '3.11', '3.12']

    steps:
      - uses: actions/checkout@v4
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -e ".[dev]"  # 或 pip install -r requirements-dev.txt
      - name: Run tests
        run: |
          pytest --cov=. --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v4
        if: matrix.python-version == '3.12'
```

---

## Dependabot 完整配置示例

```yaml
# .github/dependabot.yml
version: 2
updates:
  # npm 依赖
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
    # 分组更新：减少 PR 数量
    groups:
      development-dependencies:
        applies-to: "version-updates"
        dependency-type: "development"
        patterns: ["*"]
      production-dependencies:
        applies-to: "version-updates"
        dependency-type: "production"
        patterns: ["*"]
    # 冷却期：延迟版本更新 3 天（仅版本更新，安全更新不受影响）
    cooldown:
      default-days: 3
    # 提交信息前缀
    commit-message:
      prefix: "deps"
      include: "scope"
    reviewers: ["your-github-username"]
    labels: ["dependencies"]

  # GitHub Actions 版本更新
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
    labels: ["github-actions"]

  # Python 依赖（如有）
  # - package-ecosystem: "pip"
  #   directory: "/"
  #   schedule:
  #     interval: "weekly"
  #   groups:
  #     python-dependencies:
  #       applies-to: "version-updates"
  #       patterns: ["*"]
```

**关键选项说明**：

| 选项 | 说明 |
|------|------|
| `groups` | 分组更新，将多个依赖合并到一个 PR，减少 PR 噪音 |
| `cooldown.default-days` | 冷却期，延迟版本更新若干天（仅版本更新，安全更新不受影响） |
| `applies-to` | `version-updates` 或 `security-updates`，控制分组作用范围 |
| `dependency-type` | `development` 或 `production`，按依赖类型分组 |
| `patterns` | 匹配依赖名称的通配符列表 |

---

## 什么项目不需要这么全

| 场景 | 最少需要 |
|------|----------|
| 纯个人使用 | LICENSE + README + .gitignore |
| 方法论/文档类（无代码） | SECURITY 可极简，不需要 CHANGELOG、CI/CD、Dependabot |
| Skill 项目 | 不需要 .editorconfig、.gitattributes、CI/CD、Dependabot |
