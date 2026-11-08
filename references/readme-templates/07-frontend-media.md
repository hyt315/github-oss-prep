# 品类 7：前端与多媒体生成型 (Frontend / Media Generator) 完整模板

> 先读 [README 模板总纲](../readme-template.md) 的「前置事实清单」「通用底座 12 节」和「品类增量」表，再用本骨架。
> 只取与你项目相符的这一份，不要跨品类拼接。


````markdown
# 🎬 项目名称 / Media Generator

<div align="center">

**高质量多媒体生成与渲染引擎 · 支持多画布比例 · 宽泛框架兼容**

<!-- 边界：本骨架面向【产出媒体的工具】。若是组件库/站点（产给人看而非文件），改用：Storybook/文档站入口、SSR 与构建产物、键盘可达性与对比度 -->

[![License](https://img.shields.io/github/license/{owner}/{repo})](LICENSE)
[![npm version](https://img.shields.io/npm/v/{pkg-name}.svg)](https://www.npmjs.com/package/{pkg-name})

</div>

---

## 🎨 视觉效果预览 (Gallery)

![生成的竖版卡片示例：上标题下正文，暖色渐变背景](docs/images/preview-card.webp)
![30 秒演示：改文案后重新导出 PNG](docs/images/demo.webp)
<!-- 判据：必须有真实产物图/视频（非设计稿），每张带 alt；图片走 Git LFS 或 Release 资产，勿塞进仓库历史 -->

## 📐 画布多比例适配矩阵

| 画布比例 | 分辨率 | 适用场景 |
|---|---|---|
| **16:9** | 1920x1080 | 横屏视频 / 讲座演练 |
| **9:16** | 1080x1920 | 手机竖屏短视频 |
| **4:3** | 1440x1080 | 传统复古演示 |
| **3:4** | 1080x1440 | 社交图文短视频 |

## 📦 依赖兼容性区间

```json
{
  "dependencies": {
    "react": "^18.2.0 || ^19.0.0",
    "react-dom": "^18.2.0 || ^19.0.0",
    "remotion": "^4.0.0"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
```

## 🚀 极速开始

```bash
npm install {pkg-name}
pnpm add {pkg-name}
bun add {pkg-name}
```
````
