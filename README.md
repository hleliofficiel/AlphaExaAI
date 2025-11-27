# **AlphaExaAI**
_Distributed Deep Learning Simulator & Benchmarking Framework for Exascale AI Systems_

![Python](https://img.shields.io/badge/python-3.10+-blue.svg?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.3+-ee4c2c.svg?logo=pytorch)
![CUDA](https://img.shields.io/badge/CUDA-11.8-green.svg?logo=nvidia)
![MPI](https://img.shields.io/badge/MPI4Py-enabled-orange.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

---
#ProjectaExaAI — 250B Exascale Foundation Model**
**Next-generation open-source agentic intelligence designed for exascale supercomputing systems.**  
Built to surpass Gemini 3, Claude Sonnet 4.5, GPT-5 class models in reasoning, planning, scientific analysis, and code execution.

---

<p align="center">
  <img src="https://www.pngkey.com/png/full/894-8943983_artificial-intelligence-png.png"130">
</p>

---

##  Overview

**AlphaExaAI** is a large-scale foundation model (**250B parameters**) engineered for exascale distributed training across GPU supercomputers.  
It combines:

- **Hybrid Mixture-of-Experts (MoE) + Dense Transformers**
- **Agentic Intelligence Layer**
- **1M-token context window**
- **Scientific reasoning modules**
- **Fully distributed execution across 64–512 GPUs**

AlphaExaAI aims to be the **strongest open-source agentic AI framework in the world**, optimized for HPC centers such as:

- Polaris (A100)
- Aurora
- ILABT
- EGI Federation
- LUMI
- EuroHPC systems

---

## 🌟 Project Mission

AlphaExaAI is designed to:

1. Deliver an *exascale-ready* open-source AI model at 250B parameters  
2. Provide an **agentic system** capable of tool use, planning, coding, mathematics, and physics  
3. Offer a **transparent training blueprint** for HPC researchers  
4. Release **public benchmarks, datasets, logs, and scaling results**  
5. Act as a research-grade alternative to closed frontier models  

---

# 🔗 Official Resources

| Item | Link |
|------|------|
| 📦 GitHub Repository | https://github.com/hleliofficiel/AlphaExaAI |
| 🌐 Website (activation pending) | https://alphaexa.ai |
| 📚 Documentation | `docs/` folder |
| 📝 Technical Specification | `docs/AlphaExaAI_Model_Spec_250B.md` |
| 📈 Benchmarks | `docs/Benchmarks_Initial.md` |
| ⚙️ Scaling Guide | `docs/Scaling_Strategy_Polaris_Aurora.md` |

---

# 🧬 Model Architecture (High Overview)

AlphaExaAI-250B uses a **Hybrid MoE Transformer** featuring:

- **250B total parameters**
- 32 MoE experts (6.5B each)
- 120 transformer layers
- 128 attention heads
- Extended RoPE positional embeddings
- 1M token context capability
- FlashAttention-3 kernels
- Reinforced planning module (AgentCore)

<p align="center">
  <img src="https://camo.githubusercontent.com/4d76569b4d17ab35fbf2de42aa02b56a65ad0549812be2c96875dcde39824ece/68747470733a2f2f68756767696e67666163652e636f2f64617461736574732f68756767696e67666163652f646f63756d656e746174696f6e2d696d616765732f7261772f6d61696e2f7472616e73666f726d6572732d6c6f676f2d6461726b2e737667" width="380">
</p>

---

# 🔥 Key Capabilities

### 🧠 **Agentic Intelligence**
- Multi-step planning  
- Tool + API calling  
- Memory optimization  
- Code execution engine  
- Autonomous research workflows  

### 📘 **Scientific & Mathematical Reasoning**
- Physics modeling  
- Equation solving  
- Symbolic algebra  
- Multi-document analysis  

### 🖥 **Exascale Optimization**
- FSDP  
- ZeRO-3  
- MoE parallelism  
- Tensor + pipeline parallel  
- Recovery-aware checkpointing  

---

# 📊 Expected Performance Targets

| Capability | Expected Level | Equivalent To |
|------------|----------------|----------------|
| Code Reasoning | Very High | GPT-5, Sonnet 4.5 |
| Math & Logic | Extremely High | Gemini 3 Pro |
| Long Context | 1,000,000 tokens | Claude 3.5 class |
| Multi-Agent Ops | Advanced | GPT-5 / DeepSeek-R1 |
| Physics & Engineering | HPC-enhanced | Research-grade |

---
# 🏗 Repository Structure
AlphaExaAI/ │ ├── docs/ │   ├── AlphaExaAI_Model_Spec_250B.md │   ├── Architecture_Details.md │   ├── Training_Plan_Exascale.md │   ├── Scaling_Strategy_Polaris_Aurora.md │   ├── Benchmarks_Initial.md │   └── Research_Objectives.md │ ├── src/ │   ├── modeling/ │   ├── agents/ │   ├── training/ │   ├── data/ │   └── utils/ │ ├── scripts/ │   ├── run_distributed.sh │   └── slurm/ │ ├── requirements.txt └── README.md

---

# ⚡ Why HPC Resources Are Required

AlphaExaAI needs supercomputing power because it involves:

- Training a **250B parameter MoE foundation model**  
- Running **multi-node distributed experiments**  
- 24/7 fault-tolerant long runs  
- 50GB+ checkpoints  
- 15T+ training tokens  
- High-speed interconnect (>1 TB/s aggregated)  

Cloud systems cannot support sustained training of this scale — HPC is mandatory.

---

# 📈 Early Benchmarks (Prototype)

| Model | GPUs | Throughput | Notes |
|-------|------|------------|--------|
| 1B prototype | 32 A100 | 220K tok/s | Stable |
| 7B prototype | 64 A100 | 680K tok/s | Full attention |
| 30B prototype | 128 A100 | 1.4M tok/s | Distributed stable |
| 250B (target) | 1024 A100 | ~4.0M tok/s | Projection |

Full results in:  
`docs/Benchmarks_Initial.md`

---

# 🎯 Roadmap

### **Phase 1 — Core Development (done)**
- Tokenizer  
- Dataset processing  
- Prototype 1B/7B models  

### **Phase 2 — Distributed Scaling (in progress)**
- NCCL + FSDP  
- Multi-node MoE  

### **Phase 3 — Full AlphaExaAI-250B Training**
- 64 → 256 nodes  
- 24/7 training  
- Evaluation + RLHF  

### **Phase 4 — Release**
- Public inference API  
- Model weights  
- Web demo  
- Benchmark papers  

---

# 👤 Project Lead & Contact

- **Lead Researcher:** *Mohammed Hleli*  
- **Email:** *h.hleli@tuta.io*  
- **GitHub:** https://github.com/hleliofficiel  
- **Location:** Tunisia — HPC Open Researcher  

---

<p align="center">
  <img src="https://i0.wp.com/www.wi6labs.com/wp-content/uploads/2019/12/Machine-learning-logo-1.png" width="150">
</p>

---

# 🟦 License

This project is released under the **MIT License**.  
All contributions and research outputs remain open to the scientific community.

---

**AlphaExaAI — The future of open, exascale, agentic intelligence.**
