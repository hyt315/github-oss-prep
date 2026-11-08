# 品类 6：基础设施代码与配置集 (IaC / Dotfiles / Helm) 完整模板

> 先读 [README 模板总纲](../readme-template.md) 的「前置事实清单」「通用底座 12 节」和「品类增量」表，再用本骨架。
> 只取与你项目相符的这一份，不要跨品类拼接。


````markdown
# 🏗️ 基础设施模块 / Cloud Infrastructure

<div align="center">

**生产级声明式基础设施模块 · 版本约束明确 · 变更可预览**

<!-- 边界：本骨架只覆盖【Terraform 模块】。 -->
<!-- Helm Chart 必写：values 契约表、`helm lint`/`ct lint`、默认资源与 SLO、升级与回滚（helm upgrade --atomic / helm rollback） -->
<!-- dotfiles/devcontainer 必写：密钥绝不入库（`.env`、`.env.*` 一律进 .gitignore，只提交 `.env.example`）、机器绑定与 stow 流程、bootstrap 失败的手动步骤、"这不是可分发软件"声明 -->

[![Terraform](https://img.shields.io/badge/Terraform-%3E%3D1.6.0-623CE4)](https://terraform.io)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-%3E%3D1.28-326CE5)](https://kubernetes.io)

</div>

---

## 🚀 一键自动化部署 (Quick Start)

```bash
# 1. 初始化模块
terraform init

# 2. 预览计划
terraform plan -out=tfplan

# 3. 执行应用
terraform apply tfplan
```

---

## 🗺️ 资源拓扑架构与清单

```
[Internet] ──> [Cloudflare / ALB] ──> [EKS / K8s Cluster]
                                              │
                                   ┌──────────┴──────────┐
                                   ▼                     ▼
                             [App Pods]            [PostgreSQL RDS]
```

## ⚙️ 核心参数配置清单 (`variables.tf` / `values.yaml`)

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|---|---|---|---|---|
| `cluster_name` | `string` | 是 | - | Kubernetes 集群名称 |
| `node_count` | `number` | 否 | `3` | 工作节点副本数 |
| `enable_ssl` | `bool` | 否 | `true` | 是否自动开启 Let's Encrypt 证书 |
````
