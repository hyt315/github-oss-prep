# 品类 3：AI 模型权重与数据集 (Model & Dataset / GGUF) 完整模板

> 先读 [README 模板总纲](../readme-template.md) 的「前置事实清单」「通用底座 12 节」和「品类增量」表，再用本骨架。
> 只取与你项目相符的这一份，不要跨品类拼接。


````markdown
# 🧠 模型名称 / Model Name (GGUF & Safetensors)

<div align="center">

**高性能量化开源大模型 · 支持多硬件档位 · 低显存极速推理**

<!-- 边界：本骨架只覆盖【模型权重】。数据集请按 category-map `dataset` 的增量写：来源与采集方法、再分发许可、去标识与撤回、schema + 一行样例、切分与版本、偏倚声明 -->
<!-- 判据：任何跑分都必须给复现命令与评测环境（harness 版本、commit、随机种子、硬件、采样参数），否则删表 -->
<!-- 判据：许可必须写清"跟随基础模型许可链"，不得默认 MIT -->

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face-yellow)](https://huggingface.co/{owner}/{repo})
[![Ollama Ready](https://img.shields.io/badge/Ollama-Ready-black)](https://ollama.com/{owner}/{repo})
[![License](https://img.shields.io/github/license/{owner}/{repo})](LICENSE)

</div>

---

## ⚡ 极速开始 (One-liner Quickstart)

```bash
# 🚀 Ollama 一键拉取并运行
ollama run {owner}/{repo}

# 📦 llama.cpp 极速推理
llama-cli -m {model-name}-q4_k_m.gguf -p "你好，请做个自我介绍"
```

---

## 📊 硬件显存配置与量化矩阵 (VRAM Matrix)

| 量化版本 (Quant) | 文件大小 | 推荐显存 (VRAM) | 适用场景 |
|---|---|---|---|
| **Q4_K_M** (推荐) | ~4.2 GB | **6 GB+** (RTX 3060/4060) | 日常开发、平衡速度与精度 |
| **Q5_K_M** | ~5.1 GB | **8 GB+** | 高精度推理要求 |
| **Q8_0** | ~7.8 GB | **12 GB+** | 接近全精度基线 |
| **FP16** | ~14.5 GB | **24 GB+** (RTX 3090/4090) | 原始模型权重 |

---

## 🏆 基准评测排行榜 (Benchmark Leaderboard)

| 评测集 (Benchmark) | 本模型跑分 | 基线模型对比 | 提升幅度 |
|---|---|---|---|
| **MMLU (综合知识)** | **74.8** | 71.2 | +3.6% |
| **GSM8K (数学推理)** | **82.3** | 77.5 | +4.8% |
| **HumanEval (代码能力)** | **68.4** | 62.1 | +6.3% |

<!-- 示例（复现）：`lm_eval --model hf --model_args pretrained={repo},dtype=auto --tasks mmlu --seed 0`；
     基线同命令、同种子、同硬件；报告需注明样本数与置信区间 -->

---

## 💬 提示词模版 (Prompt Format - ChatML)

```text
<|im_start|>system
你是一个专业的技术助手。<|im_end|>
<|im_start|>user
{user_query}<|im_end|>
<|im_start|>assistant
```
````
