# 社区健康文件与 CI 按需参考（锦上添花项）

> 个人小工具或早期原型不需要一次性塞满所有治理文件；仅在项目准备长期维护、接受外部 PR 或多人协作时按需添加。

## 1. 按需清单与 GitHub 官方口径

GitHub 的 community profile 健康百分比只看文件是否存在，**不以刷满百分比为目标**。按实际需要选用：

- **`LICENSE`（必选，不可省略）**：每个仓库必须自带，不能靠组织级 `.github` 仓库继承。
- **`SECURITY.md`（推荐）**：说明支持的版本与私有漏洞报告入口（`https://github.com/{owner}/{repo}/security/advisories/new`），禁止引导用户在公开 Issue 披露漏洞；注意还需在仓库 **Settings → Advanced Security** 开启 Private Vulnerability Reporting。
- **`CONTRIBUTING.md`（接受外部 PR 时添加）**：写清本地开发、测试命令、分支与 PR 要求。
- **`CODE_OF_CONDUCT.md`（多人社区时添加）**：采用 Contributor Covenant 3.0 并附版本 URL。
- **Issue 表单与 PR 模板（活跃项目按需添加）**：放在 `.github/ISSUE_TEMPLATE/` 与 `.github/pull_request_template.md`。若在 `config.yml` 中设 `blank_issues_enabled: false`，必须同时提供 Discussions 或提问入口，避免堵死非模板反馈。

## 2. YAML Issue Forms 精简示例（`.github/ISSUE_TEMPLATE/bug_report.yml`）

```yaml
name: "Bug Report"
description: "Report a bug or unexpected behavior"
title: "[Bug]: "
labels: ["bug"]
body:
  - type: textarea
    id: what-happened
    attributes:
      label: "What happened?"
      placeholder: "Describe the unexpected behavior..."
    validations:
      required: true
  - type: textarea
    id: reproduction
    attributes:
      label: "Steps to reproduce"
      render: shell
    validations:
      required: true
```

## 3. 加固版 GitHub Actions CI 样例

所有外部 Action 均锁定 40 位完整 commit SHA（实际写入时用 `gh api repos/<owner>/<repo>/commits/<tag> --jq .sha` 取最新值，不要死抄旧 SHA），并声明顶层只读权限。

### Python CI（`.github/workflows/ci.yml`）

```yaml
name: CI

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
        python-version: ["3.11", "3.12", "3.13", "3.14"]
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
      - uses: actions/setup-python@6d4fd22b20465ccc0f7354476588e8df7c9ca0e0 # v7.1.0
        with:
          python-version: ${{ matrix.python-version }}
      - run: python -m unittest discover -s tests -v
```

### Node.js CI（`.github/workflows/ci.yml`）

```yaml
name: CI

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
        node-version: [22.x, 24.x, 26.x]
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
      - uses: actions/setup-node@820762786026740c76f36085b0efc47a31fe5020 # v7.0.0
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
      - run: npm ci
      - run: npm test
```

## 4. Dependabot 配置（`.github/dependabot.yml`）

> **踩坑提醒**：只声明仓库里**真实存在**的包生态。给没有 `package.json` 的仓库配 `npm`、或没有 `pyproject.toml`/`requirements.txt` 的仓库配 `pip`，会导致 Dependabot 任务持续失败。

```yaml
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
    groups:
      actions-dependencies:
        patterns:
          - "*"
```
