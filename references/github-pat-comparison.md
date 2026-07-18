# Fine-grained PAT vs Classic PAT 对比

> 以下信息来自 GitHub 官方文档（Managing your personal access tokens）。供需要了解 PAT 能力与不足的用户参考，正常使用本 Skill 无需深读本文件。

---

## 目录

- [GitHub 官方立场](#github-官方立场)
- [Fine-grained PAT 的优势](#fine-grained-pat-的优势)
- [Fine-grained PAT 的当前限制](#fine-grained-pat-的当前限制官方明确列出)
- [Classic PAT 仍必要的场景](#classic-pat-仍必要的场景)
- [本 Skill 的选择](#本-skill-的选择)

---

## GitHub 官方立场

GitHub **推荐使用 Fine-grained PAT 而非 Classic PAT**，但明确承认 Fine-grained 尚有功能缺口，正在逐步补齐。方向是持续收窄 Classic、补齐 Fine-grained 缺口。

---

## Fine-grained PAT 的优势

- 每个 token 限定访问**单一用户或组织**的资源
- 可进一步限定到**特定仓库**
- 授予**细粒度权限**（比 Classic 的 scope 更精细）
- 组织所有者可要求对访问组织资源的 Fine-grained PAT **审批**
- 支持设置过期时间（允许无限期，但可被组织/企业的最大生命周期策略阻止）
- **数量上限**：每个用户最多 50 个 Fine-grained PAT，超过建议改用 GitHub App

---

## Fine-grained PAT 的当前限制（官方明确列出）

- 无法用于向**非成员的公开仓库**贡献
- 无法用于用户是**外部协作者或仓库协作者**的仓库贡献
- 无法**同时访问多个组织**
- 无法访问 **Packages**
- 无法调用 **Checks API**
- 无法访问**用户账户拥有的 Projects**

---

## Classic PAT 仍必要的场景

- 对**非自己拥有/非所属组织**的公开仓库有写权限
- 外部协作者访问组织仓库
- 少数 REST API 端点仅支持 Classic（需查端点文档确认）
- 注意：Classic PAT 会授予你可访问的**所有组织仓库 + 所有个人仓库**的访问权，风险更高

---

## 本 Skill 的选择

本 Skill 默认不直接处理 PAT，而是使用 GitHub 连接器或已登录的 `gh` CLI。只有用户明确需要为其他受信任工具选择 PAT 类型时，才参考以下差异：

- 需要 `repo` scope 来**创建新仓库 + 推送代码**，Classic PAT 授权流程最简单
- Fine-grained PAT 虽然也能创建仓库（`POST /user/repos` 已支持），但需要预先配置仓库权限范围，且**无法跨组织操作**，多仓库场景下配置繁琐
- Fine-grained PAT 无法贡献非成员公开仓库、无法访问 Packages 等限制（见上方列表），在开源发布场景中可能受限
