# 品类 5：类库与核心 SDK 型 (Library / SDK) 完整模板

> 先读 [README 模板总纲](../readme-template.md) 的「前置事实清单」「通用底座 12 节」和「品类增量」表，再用本骨架。
> 只取与你项目相符的这一份，不要跨品类拼接。


````markdown
# 📚 SDK 名称 / Library Name

<div align="center">

**轻量、高效、类型安全的跨平台核心 SDK · 零外部冗余依赖**

[![npm](https://img.shields.io/npm/v/{pkg-name}.svg)](https://www.npmjs.com/package/{pkg-name})
[![PyPI](https://img.shields.io/pypi/v/{pkg-name}.svg)](https://pypi.org/project/{pkg-name}/)
[![Crates.io](https://img.shields.io/crates/v/{pkg-name}.svg)](https://crates.io/crates/{pkg-name})

</div>

---

## ⚡ 5 行极简极速示例 (Hello World)

```typescript
import { createClient } from '{pkg-name}';

const client = createClient({ apiKey: process.env.API_KEY });
const result = await client.execute({ prompt: "Hello World" });
console.log(result.data);
```

<!-- 判据：示例之后必须给真实返回值；库类 README 的第一价值就是"调用形状 + 返回形状" -->
```json
{ "data": "Hello World", "usage": { "prompt_tokens": 3, "completion_tokens": 12 }, "latency_ms": 412 }
```

## 🧯 错误语义

| 情况 | 抛出 | 建议处置 |
|---|---|---|
| 未配置密钥 | `MissingCredentials` | 设 `API_KEY` 环境变量，勿写进代码 |
| 网络超时 | `TimeoutError`（默认 30s） | 用 `client.execute({ timeout: 60_000 })` 或加重试 |
| 上游限流 | `RateLimited`（含 `retryAfterMs`） | 按 `retryAfterMs` 退避 |

## 📥 安装

| 包管理器 | 命令 |
|---|---|
| **npm** | `npm install {pkg-name}` |
| **pnpm** | `pnpm add {pkg-name}` |
| **bun** | `bun add {pkg-name}` |
| **pip** | `pip install {pkg-name}` |
| **cargo** | `cargo add {pkg-name}` |

## 📖 API 参数表格

| 方法 | 参数 | 返回值 | 说明 |
|---|---|---|---|
| `execute(options)` | `RequestOptions` | `Promise<Response>` | 执行核心请求 |
````
