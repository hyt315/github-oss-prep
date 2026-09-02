# GitHub 2026 官方社区健康文件库与模板规范

> 对标：GitHub Insights → Community Standards 100% 满分考核标准。

---

## 目录

1. [现代交互式 YAML Issue Forms](#1-现代交互式-yaml-issue-forms)
   - [Bug 反馈表单 (`bug_report.yml`)](#11-bug-反馈表单-githubissue_templatebug_reportyml)
   - [需求建议表单 (`feature_request.yml`)](#12-需求建议表单-githubissue_templatefeature_requestyml)
   - [模板全局配置 (`config.yml`)](#13-模板全局配置-githubissue_templateconfigyml)
2. [合并请求模板 (`pull_request_template.md`)](#2-合并请求模板-githubpull_request_templatemd)
3. [安全策略 (`SECURITY.md`)](#3-安全策略-securitymd)
4. [编码规范与换行符文件](#4-编码规范与换行符文件)

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
        - "Windows 11 (24H2)"
        - "Windows 11 (22H2 / 23H2)"
        - "Windows 10"
        - "macOS"
        - "Linux"
        - "Other"
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
```yaml
blank_issues_enabled: false
contact_links:
  - name: "📖 项目文档 / Documentation"
    url: "https://github.com/{owner}/{repo}#readme"
    about: "在提交 Issue 前请先查阅官方文档"
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

## 支持版本 / Supported Versions

| 版本 (Version) | 支持状态 (Supported) |
|---|---|
| 最新版本 (Latest) | :white_check_mark: |
| 旧版本 (< Latest) | :x: |

## 报告安全漏洞 / Reporting a Vulnerability

如果发现任何安全漏洞或敏感信息泄露风险，**请勿公开发布 Issue**。
请通过 GitHub 官方的 [Private Vulnerability Reporting](https://github.com/{owner}/{repo}/security/advisories/new) 提交私密通报，维护者将在 48 小时内进行响应与修复。
```

---

## 4. 编码规范与换行符文件

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
