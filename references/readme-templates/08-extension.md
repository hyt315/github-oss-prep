# 品类 8：浏览器扩展与插件型 (Browser Extension / MV3) 完整模板

> 先读 [README 模板总纲](../readme-template.md) 的「前置事实清单」「通用底座 12 节」和「品类增量」表，再用本骨架。
> 只取与你项目相符的这一份，不要跨品类拼接。


````markdown
# 🧩 扩展名称 / Browser Extension

<div align="center">

**现代轻量级浏览器效率扩展 · 零隐私追踪 · Manifest V3 标准**

[![Chrome Web Store](https://img.shields.io/badge/Chrome%20Web%20Store-Install-blue?logo=googlechrome)](https://chromewebstore.google.com/detail/{id})
[![Edge Add-ons](https://img.shields.io/badge/Edge%20Add--ons-Install-0078D7?logo=microsoftedge)](https://microsoftedge.microsoft.com/addons/detail/{id})
[![License](https://img.shields.io/github/license/{owner}/{repo})](LICENSE)

</div>

---

## 📥 安装方式

### 方式 A：应用商店安装（最推荐）
- [前往 Chrome 网上应用店一键安装](https://chromewebstore.google.com/detail/{id})
- [前往 Edge 外接程序商店一键安装](https://microsoftedge.microsoft.com/addons/detail/{id})

### 方式 B：开发者模式离线加载
1. 在 [Releases 页面](https://github.com/{owner}/{repo}/releases) 下载最新的 `extension.zip` 并解压；
2. 打开 Chrome / Edge 浏览器，访问 `chrome://extensions`；
3. 打开右上角的 **“开发者模式”** 开关；
4. 点击左上角 **“加载已解压的扩展程序”**，选择解压出的文件夹即可。

---

## 🔒 Manifest V3 权限用途声明

| 申请权限 (Permission) | 使用原因与场景说明 |
|---|---|
| `storage` | 仅在本地持久化存储用户的自定义主题与偏好设置 |
| `activeTab` | 仅在用户主动点击扩展图标时读取当前页面标题与 URL |
| `contextMenus` | 在右键菜单中添加快捷搜索动作 |

> 🛡️ **隐私承诺**：本扩展绝不上传用户浏览历史或个人数据；所有偏好只存 `chrome.storage.local`。

## 🧪 兼容性

| 宿主 | 已验证版本 | 状态 |
|---|---|---|
| Chrome / Edge | 130+ | 已验证 |
| Firefox | — | **未验证** |

## 📦 更新与失效

- 更新走商店（推荐）；离线 zip 需自行覆盖并重启浏览器。
- 站点改版导致选择器失效时：先看 [已知问题](../../issues?q=is%3Aissue+label%3Asite-breakage)，附站点 URL 与控制台报错。

<!-- 判据：开发者模式加载必须提示"只加载你信任的来源，加载后会获得你账户的浏览器数据访问面" -->
<!-- 判据：权限声明表每一项都要回答"数据是否离开本机"，商店审核与用户信任都看这一列 -->
````
