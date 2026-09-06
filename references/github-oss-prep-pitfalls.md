# github-oss-prep 核心避坑库与官方规范基线

<!-- skill-doctor: allow-block SEC002 -->

> 本指南聚合 GitHub 官方 2026 社区健康度标准、OpenSSF 供应链安全规范、顶级开源项目最佳实践与【冷门长尾探索池】中的生产级故障，为开源项目发布准备、安全脱敏与全渠道分发提供全景避坑与工业级基线。

---

## 目录

- 一、 GitHub 官方规范与社区健康度基线 (GitHub Official Baselines)
- 二、 【冷门长尾探索池】极端特异性杀手坑 (Fringe Edge Cases & Killer Pitfalls)
- 三、 GitHub 顶级开源工程与同类 Agent 技能对标经验 (Peer Skills & Top OSS)
- 四、 自动化安全核验探针与检测算法 (Safety Probes)

---

## 一、 GitHub 官方规范与社区健康度基线

### 1. Insights → Community 100% 完整门禁准则
- **官方考评维度**：GitHub Insights 的 Community Standards 模块会实时检测仓库的 7 项核心基础设施，只有全量达标才能获得 100% 社区健康评级：
  1. **Description**: 仓库首页右上角「About」简述与 Topics 主题标签；
  2. **README**: 根目录或 `.github/` 下的标准项目门面；
  3. **CODE_OF_CONDUCT**: 社区行为准则（推荐 Contributor Covenant 2.1）；
  4. **CONTRIBUTING**: 贡献指南（开发环境搭建、分支规范、PR 提交流程）；
  5. **LICENSE**: 明确的开源许可证（必须匹配 SPDX 标识符）；
  6. **SECURITY.md**: 安全漏洞披露与响应策略；
  7. **Issue / Pull Request Templates**: 规范化的问题报告与 PR 模板。
- **全局 `.github` 组织继承与覆盖机制**：
  - 可以在组织或个人账户下创建名为 `.github` 的特殊公开仓库，将 `CODE_OF_CONDUCT.md`、`CONTRIBUTING.md`、`SECURITY.md` 以及默认模板放入其中作为全账号全局兜底；
  - **⚠️ 踩坑警示**：Issue 和 PR 模板要实现跨仓库继承，`.github` 仓库必须是**公开（Public）**状态；如果目标仓库自身存在同名文件，将无条件覆盖全局默认配置。

### 2. YAML Issue Forms 官方标准规范
- **传统 Markdown 模板的致命痛点**：传统的 `.md` 模板属于自由编辑文本，提问者经常随意删改标题、破坏注释结构或留白，导致维护者收集不到必要的复现日志与环境信息。
- **现代 YAML Issue Forms 标准**（存放于 `.github/ISSUE_TEMPLATE/*.yml`）：
  - 强结构化字段：`type: input`、`type: textarea`、`type: dropdown`、`type: checkboxes`；
  - 语法高亮与格式约束：使用 `render: shell` 或 `render: text` 自动将粘贴的崩溃堆栈包裹为代码块；
  - 必填校验：通过 `validations: { required: true }` 强制要求填写复现步骤与最小重现代码；
  - 自动打标与路由：在表单头部设置 `labels: ["bug", "triage"]` 与 `assignees: []` 实现提交即自动分类；
  - 禁用自由 Issue：在 `.github/ISSUE_TEMPLATE/config.yml` 中配置 `blank_issues_enabled: false`，杜绝用户绕过模板提交空白 Issue。

### 3. SECURITY.md 漏洞披露与响应底线
- **官方规范要求**：
  - 明确支持维护的版本矩阵（Supported Versions table），标明哪些旧版本已停止接收安全更新；
  - 明确私有漏洞报告渠道：引导至 GitHub Private Vulnerability Reporting（安全公告通道）或专用安全邮箱（如 `security@example.com`）；
  - **🚨 致命禁区**：严禁在 SECURITY.md 中让用户在 Public Issues 中提交安全漏洞与零日漏洞（0-day），这会导致安全问题瞬间公之于众，危害所有下游用户；
  - 承诺响应 SLA：标明收到报告后的初步确认时限（建议 ≤ 48 小时）与修复进展通报周期。

---

## 二、 【冷门长尾探索池】极端特异性杀手坑

### 1. Git 历史深水凭据残留与“已删除”假象
- **病症**：在代码或配置文件中误提交了 `.env`、API Key、数据库密码或私有 Token，随后在下一个 Commit 中将该文件删除并提交。开发者误以为“文件已经没了，仓库很安全”。
- **底层机理与致命风险**：
  - Git 是基于快照与对象图存储（Content-Addressable Storage）的版本控制系统，所有历史上提交过的 Blob 对象均永久固化在 `.git/objects` 历史树中；
  - 公网爬虫、黑客工具（如 TruffleHog、Gitleaks）以及 GitHub Secret Scanning 在仓库转为 Public 或 Push 的 2 秒内就会完成全历史爬取并自动利用泄露的凭据；
  - 单纯执行 `git rm` 毫无防范效果！
- **防御与处置三铁律**：
  1. **第一动作：立即轮转吊销（Rotate & Revoke）**！一旦推送到远程仓库，无论是否立即撤回，一律视为凭据已泄露，必须先在云平台将密钥失效，再进行技术清理；
  2. **第二动作：使用现代工具重写历史**：严禁使用陈旧且极易破坏仓库引用的 `git filter-branch`，统一使用现代标准工具 **`git-filter-repo`** 或 **BFG Repo-Cleaner** 物理清除敏感文件与字符串；
  3. **第三动作：防范协作者二次污染**：历史重写会导致所有 Commit 的 SHA 哈希发生突变。若团队成员本地持有旧 Clone 并执行 `git pull`，旧脏历史会瞬间被合并带回！必须通知所有协作者删除本地副本重新 `git clone`，并联系 GitHub 支持清理服务器端的 PR 缓存视图。

### 2. CI/CD 供应链投毒与 GITHUB_TOKEN 权限过大
- **病症**：直接在 GitHub Actions workflow 中使用第三方社区 Action，且未显式声明权限，依赖默认权限运行。
- **供应链攻击路径**：
  - GitHub 仓库默认赋予 `GITHUB_TOKEN` 过大的读写权限（默认可 push、release、写入 packages）；
  - **标签漂移攻击（Tag Mutability）**：攻击者控制或劫持某个常用 Action 仓库后，恶意篡改已有标签（如强制覆盖 `v3` 或 `v4` tag），注入窃密恶意代码；
  - 恶意 Action 在 Runner 中直接读取环境变量中的所有 Secrets 或借由可写的 `GITHUB_TOKEN` 篡改 Release 构件与发布资产。
- **防御对策**：
  - **最小特权原则（Least Privilege）**：在 workflow 文件顶层强制声明只读基线：
    ```yaml
    permissions:
      contents: read
    ```
    仅在真正需要创建 Release 或部署的特定 Job 下窄幅开启 `contents: write`；
  - **Pin 完整 40 位 Commit SHA**：在生产级 CI 中，所有第三方 Action 严禁直接使用分支或易变 tag，必须锁定不可变的 Git Commit SHA，并附带注释版本号：
    ```yaml
    uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
    ```
  - **警惕 `pull_request_target` 触发器**：该触发器运行在目标基准分支上下文并拥有仓库 Secrets 访问权，严禁在此触发器下 checkout 并运行来自 Fork 分支的未审查代码；
  - **防范 Bash 脚本注入**：严禁直接在 `run:` 中拼接不可信输入（如 `${{ github.event.issue.title }}`），必须通过 `env:` 映射后在脚本中以环境变量（`$ISSUE_TITLE`）引用。

### 3. 开源许可证冲突与“无许可”法律悬崖
- **常识误区与陷阱**：
  - **陷阱 1：“代码公开即开源”误区**：未放置 LICENSE 文件的公共代码，在法律上属于“保留所有权利（All Rights Reserved）”。其他人无权合法使用、修改、分发甚至编译该代码；
  - **陷阱 2：MIT 许可证的“专利真空”**：MIT 许可证极为短小精悍，但不包含显式专利授权条款（Patent Grant）。在企业级软件、云原生、AI 算法与基础设施项目中，若作者后续主张软件专利，使用者将面临侵权诉讼风险。企业级和重型开源项目推荐优先选择包含明确专利授权与商标限制的 **Apache 2.0**；
  - **陷阱 3：强传染性许可证污染（Copyleft Trap）**：项目中若直接嵌入或静态链接了 GPL-3.0 / AGPL-3.0 许可的代码模块，整个衍生工程在发布时均必须开源为同等强 Copyleft 许可。在 SaaS 场景下，**AGPL-3.0** 进一步关闭了网络服务漏洞，即使仅通过云端接口提供服务，也强制要求公开服务端完整源码；
  - **陷阱 4：缺失第三方版权声明（Attribution Missing）**：即使引入最宽松的 MIT/BSD 依赖，其协议条款依然强制要求“在衍生代码或文档中保留原作者版权声明与许可全文”。

### 4. 多生态发布不可变性与版本脱节陷阱
- **病症**：在准备发布到 PyPI (`uv publish`)、npm (`npm publish`) 或 Docker Hub 时，因网络闪退、构件缺陷或配置文件错误导致发布中途失败，修改后再次上传时报错 `400 / 403 Version already exists`。
- **底层机理**：
  - 现代官方包注册中心（PyPI, npm, RubyGems 等）为了防范供应链篡改（Dependency Confusion / Package Tampering），全面实施**包版本不可变原则（Immutability）**；
  - 任何已被注册过的版本号（甚至中途上传失败的部分 wheel）均永久锁定，严禁覆盖、更新或替换！
- **防御对策**：
  - **单一真相来源（Single Source of Truth）**：版本号严禁在 README、`pyproject.toml`、`package.json`、`manifest.json` 与 Git Tag 中手动到处抄写，推荐使用动态版本派生（如基于 git tags 的构建工具）或自动化版本发布工具；
  - **发版前强制 `--dry-run` 预检**：在正式向远程 registry 上传前，必须先在本地执行 `uv build` 或 `npm pack`，检查打包出来的 tarball / wheel 文件清单是否无意中包含了敏感文件（如测试凭据、开发配置）；
  - **采用 OIDC Trusted Publishing**：淘汰长期保存在 GitHub Secrets 中的静态 API Token，改用基于 OpenID Connect 的短期临时凭据交换机制。

### 5. 极端隐蔽脱敏陷阱：会话指纹、绝对路径与 Git Remote 凭据
- **本地绝对路径污染**：
  - Windows 环境下的 `C:\Users\<用户名>\`、Linux/macOS 下的 `/home/<username>/`，不仅破坏跨平台可移植性，还会直接泄露作者的真实姓名或公司内网主机命名规则；
  - 必须使用相对路径或系统环境变量（如 `$HOME` / `%USERPROFILE%`）替代。
- **`.git/config` 内嵌明文 Token 泄漏**：
  - 开发者通过带有 Token 的 URL（如 `https://<token>@github.com/org/repo.git`）克隆或推送代码；
  - 该 Token 会以明文形式永久固化在本地 `.git/config` 中，若后续打包整个项目（如 ZIP）交付或误将 `.git` 文件夹公开，特权 Token 就会直接泄露。
- **AI Agent 会话标记与调试元数据污染**：
  - 包含各类 AI 编程助手（如 Antigravity, Claude Code, Cursor 等）的内部调试标记、Conversation ID、Workspace 绝对路径与隐藏的 `.doctor/`、`.system_generated/` 临时追踪目录，必须在开源前彻底纳入 `.gitignore` 或物理清理。

---

## 三、 GitHub 顶级开源工程与同类 Agent 技能对标经验

### 1. README 15 秒黄金法则（Above the Fold）
- **第一屏法则**：访客在进入仓库后的前 15 秒内就会决定是否 Star 或离开：
  1. **一句话价值主张**：用大号粗体直击痛点，阐述“这个项目解决了什么别人解决不了的问题”；
  2. **视觉化实证（Visual Proof）**：嵌入一张不超过 5MB 的高质量 GIF 动图、SVG 流程图或 ASCII 交互录屏，胜过千言万语；
  3. **30 秒开箱即用体验**：优先展示免安装运行命令（如 `uvx <tool>`、`npx <tool>`、`docker run`）；
  4. **权威状态徽章（Badges）**：配置精准的 Shields.io 动态徽章（CI Build Status, Latest Release, License, Python/Node Version），拒绝无效或报错的死链徽章。

### 2. GitHub 发现度（SEO）与 Topics 优化矩阵
- **About 描述黄金长度**：控制在 100~140 个字符，包含核心痛点动词与搜索关键词，不要堆砌无意义的形容词；
- **Topics 标签工业级标准**：
  - 必须使用全小写连字符命名（kebab-case）；
  - 配备 5~8 个核心标签，覆盖：1) 核心功能（如 `open-source`, `security-scanning`）；2) 目标生态（如 `github`, `cli`, `agent-skill`）；3) 语言/架构（如 `python`, `mcp`）。

### 3. 就近内联动作与渐进式披露（Progressive Disclosure）
- **根除弱引用漂移**：主工作流中禁止出现“详见某某文档”、“可参考某某文件”等非确定性弱引导；
- **强指令闭环**：在具体阶段步骤下，必须以明确的就近动作指令引导 Agent 读取指定文档与锚点章节：
  ```markdown
  👉 动作：读取 references/github-oss-prep-pitfalls.md#一-github-官方规范与社区健康度基线
  ```

---

## 四、 自动化安全核验探针与检测算法

为保证开源发布前的绝对只读安全性，以下核心安全核验算法作为 scripts/ 辅助工具的标准规范：

### 1. 凭据与敏感路径只读扫描探针 (Python 原生无依赖)
```python
import re
from pathlib import Path

# 经典高危敏感正则指纹
SENSITIVE_PATTERNS = {
    "GitHub PAT": re.compile(r"gh[pousr]_[A-Za-z0-9_]{36,255}"),
    "OpenAI/Claude API Key": re.compile(r"sk-[a-zA-Z0-9_-]{20,}"),
    "Slack/Discord Webhook": re.compile(r"https://(?:hooks\.slack\.com|discord\.com/api/webhooks)/[A-Za-z0-9/_.-]+"),
    "Windows User Path": re.compile(r"[A-Za-z]:\[Uu]sers\[a-zA-Z0-9_.-]+\?[a-zA-Z0-9_.-]*"),
    "Git Credential in URL": re.compile(r"https://[^:\s]+:[^@\s]+@github\.com"),
}

def scan_file_safety(file_path: Path) -> list[str]:
    violations = []
    text = file_path.read_text(encoding="utf-8", errors="ignore")
    for name, pattern in SENSITIVE_PATTERNS.items():
        if pattern.search(text):
            violations.append(name)
    return violations
```

### 2. GitHub Actions 供应链安全审计探针
```python
import yaml
from pathlib import Path

def audit_workflow_security(workflow_path: Path) -> list[str]:
    issues = []
    text = workflow_path.read_text(encoding="utf-8", errors="ignore")
    
    # 检查是否缺少 top-level permissions: contents: read
    if "permissions:" not in text:
        issues.append("缺少顶层 permissions 声明，存在过度提权风险")
        
    # 检查是否存在未锁定 SHA 的社区 Action
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("uses:"):
            action = line.split("uses:")[1].strip()
            if not action.startswith("actions/") and not action.startswith("./"):
                if "@" in action and len(action.split("@")[1]) != 40:
                    issues.append(f"第三方 Action 未锁定 40 位 Commit SHA: {action}")
                    
    return issues
```
