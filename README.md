# **AlphaExaAI — The Omnipotent Agentic Foundation**
_The first open-source, exascale-ready foundation model designed not just to chat, but to **act**, **build**, and **control**._

<p align="center">

![Status](https://img.shields.io/badge/Status-ExaMind_V2_LIVE-brightgreen?style=for-the-badge&logo=statuspage)
![Model](https://img.shields.io/badge/Model-8B_Parameters-blue?style=for-the-badge&logo=brain)
![HuggingFace](https://img.shields.io/badge/🤗_HuggingFace-Available_Now-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-Apache_2.0-orange?style=for-the-badge&logo=apache)
![Context](https://img.shields.io/badge/Context-128K_Tokens-purple?style=for-the-badge&logo=memory)
![CPU](https://img.shields.io/badge/Runs_On-CPU_&_GPU-success?style=for-the-badge&logo=linux)

</p>

---

<div align="center">

## 🎉 ExaMind V2-Final is NOW LIVE on Hugging Face!

### 🧠 [**Download ExaMind →**](https://huggingface.co/AlphaExaAI/ExaMind)

*An advanced open-source AI model — built for programming, reasoning, and security.*
*Made with ❤️ by the AlphaExaAI team.*

</div>

---

## 🚀 What is ExaMind?

**ExaMind** is our first publicly released model — an advanced conversational AI built on the **Qwen2** architecture with **7.62 billion parameters (~8B)**. It was fine-tuned by the AlphaExaAI team with a focus on:

- 🖥️ **Advanced Programming** — Code generation, debugging, architecture design
- 🧩 **Complex Problem Solving** — Multi-step logical reasoning
- 🔒 **Security-First Design** — 92% prompt injection resistance rate
- 🌍 **Multilingual** — Supports all major world languages
- ⚡ **CPU Deployable** — No GPU required

### Quick Start

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("AlphaExaAI/ExaMind")
tokenizer = AutoTokenizer.from_pretrained("AlphaExaAI/ExaMind")

messages = [{"role": "user", "content": "Explain how to secure a REST API."}]
inputs = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True)
outputs = model.generate(inputs, max_new_tokens=512, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

> 📖 **Full documentation, benchmarks, and usage guide:** [huggingface.co/AlphaExaAI/ExaMind](https://huggingface.co/AlphaExaAI/ExaMind)

---

## 📊 ExaMind Benchmarks

| Benchmark | Score |
|-----------|-------|
| **MMLU – World Religions** (0-shot) | **94.8%** |
| **MMLU – Overall** (5-shot) | **72.1%** |
| **HumanEval** pass@1 | **79.3%** |
| **MBPP** pass@1 | **71.8%** |
| **GSM8K** (8-shot CoT) | **82.4%** |
| **ARC-Challenge** (25-shot) | **68.4%** |
| **HellaSwag** (10-shot) | **78.9%** |
| **Prompt Injection Resistance** | **92%** |

---

## 🌌 The Vision: Beyond Chat

The era of "chatbots" is over. **AlphaExaAI** is built for the era of **Agentic Intelligence**. 

While models like GPT-5 or Gemini 3 focus on conversation, AlphaExaAI is engineered for **execution**. It is designed to be the "brain" behind autonomous agents, capable of complex reasoning, software engineering, system control, and multimodal creation.

### 🚀 Key Breakthroughs

#### 1. **128K+ Token Context Window**
ExaMind supports up to 128K tokens with RoPE scaling. Ingest entire codebases, documentation, or datasets in a single prompt.

#### 2. **Eco-Train Efficiency (Green AI)** 🌿
Using advanced **LoRA** and efficient fine-tuning, ExaMind achieves remarkable performance while consuming a fraction of the compute resources.

#### 3. **True Omnipotence (Multimodal Roadmap)**
ExaMind is the foundation. Coming soon:
*   **ExaMind-Code:** Specialized coding variant
*   **ExaMind-Vision:** Multimodal capabilities
*   **ExaMind V3:** Extended context, improved reasoning

#### 4. **The Agentic Core** 🛡️
AlphaExaAI models are trained on real-world operational data, giving them practical intelligence that academic models lack.

---

## 🗺️ Roadmap

- [x] **ExaMind V1** — Initial research release
- [x] **ExaMind V2-Final** — 🎉 **LIVE NOW** on [Hugging Face](https://huggingface.co/AlphaExaAI/ExaMind)
- [ ] **ExaMind V2-GGUF** — Quantized versions for efficient CPU inference
- [ ] **ExaMind V3** — Extended 128K context, enhanced reasoning
- [ ] **ExaMind-Code** — Specialized coding model
- [ ] **ExaMind-Vision** — Multimodal capabilities
- [ ] **AlphaExaAI 250B** — The ultimate open-source frontier model

---

## 🤝 We Welcome Contributors!

**AlphaExaAI is a community-driven project.** We believe the best AI is built together.

### 👥 Who We Welcome

| Who | How You Can Help |
|-----|-----------------|
| 🧑‍💻 **Developers** | Code contributions, bug fixes, tooling |
| 🔬 **Research Teams** | Benchmarking, evaluation, novel training methods |
| 🏫 **Universities** | Academic research, student projects, compute partnerships |
| 🏢 **Organizations** | Resource sponsorship, infrastructure support |
| 🌍 **Community Members** | Documentation, translations, tutorials, feedback |

### How to Contribute

1. **Fork** this repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 💖 Support AlphaExaAI

Building open-source AI requires significant resources. If you believe in our mission, consider supporting us:

### 💰 Donations

| Platform | Link |
|----------|------|
| **GitHub Sponsors** | [Sponsor @hleliofficiel](https://github.com/sponsors/hleliofficiel) |
| **Buy Me a Coffee** | [buymeacoffee.com/alphaexaai](https://buymeacoffee.com/alphaexaai) |
| **Bitcoin (BTC)** | `Coming soon` |
| **Ethereum (ETH)** | `Coming soon` |

### 🖥️ Resource Contributions

We especially welcome **compute resource donations**:
- GPU/TPU cloud credits (AWS, GCP, Azure, Lambda Labs)
- Access to HPC clusters for training
- Storage and bandwidth for model distribution

Every contribution, no matter how small, helps advance open-source AI. ❤️

---

## 🏆 Special Thanks

A heartfelt thank you to everyone who made ExaMind possible:

| Contributor | Role |
|-------------|------|
| **[@hleliofficiel](https://github.com/hleliofficiel)** | Lead Researcher & Founder |
| **[@ilbat](https://github.com/ilbat)** | Resource Contributor & Assistant |
| **[@HuggingFace](https://huggingface.co)** | Model hosting & open-source AI infrastructure |
| **[@DarekHub](https://github.com/DarekHub)** | Data Contributor |
| **Kaitlyn Truby** | Researcher |
| **AlphaExaAI Community** | Testing, feedback, and support |
| **Qwen Team** | Base model architecture |

> *This project was built with love, late nights, and an obsession with pushing the boundaries of open-source AI.* ❤️

---

## 🔗 Links

| Resource | URL |
|----------|-----|
| 🤗 **Hugging Face Model** | [AlphaExaAI/ExaMind](https://huggingface.co/AlphaExaAI/ExaMind) |
| 🤗 **Organization** | [huggingface.co/AlphaExaAI](https://huggingface.co/AlphaExaAI) |
| 💻 **GitHub** | [github.com/hleliofficiel/AlphaExaAI](https://github.com/hleliofficiel/AlphaExaAI) |
| 📧 **Email** | h.hleli@tuta.io |

---

## 📜 License

**Apache License 2.0** — Free for commercial use, modification, and distribution.

- ✅ Commercial use
- ✅ Modification & distribution
- ✅ Patent grant
- ✅ Private use

See [LICENSE](LICENSE) for full text.

---

<p align="center">

**Built with ❤️ by AlphaExaAI Team — 2026**

*Advancing open-source AI, one model at a time.*

![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen?style=for-the-badge&logo=opensourceinitiative)
![License](https://img.shields.io/badge/License-Apache_2.0-yellow?style=for-the-badge&logo=apache)
![Made With Love](https://img.shields.io/badge/Made_With-❤️-red?style=for-the-badge)

</p>
