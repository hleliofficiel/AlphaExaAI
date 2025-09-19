# **AlphaExaAI**
_Distributed Deep Learning Simulator for Exascale AI_

![Python](https://img.shields.io/badge/python-3.10+-blue.svg?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.3+-ee4c2c.svg?logo=pytorch)
![CUDA](https://img.shields.io/badge/CUDA-11.8-green.svg?logo=nvidia)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🌍 Project Overview
**AlphaExaAI** is an open-source initiative focused on simulating and benchmarking large-scale distributed AI training on exascale-class supercomputers such as **Aurora** and **Polaris**.  

The project builds on prior work with DDLSim and extends it into a hybrid **multi-node, multi-GPU framework** designed for **fault tolerance, reproducibility, and scalability**.  

All results are released **openly** to support global research efforts in distributed deep learning.  

---

## 📊 Motivation & Goals
- Prepare an **exascale-ready AI training framework**.
- Benchmark **scaling performance** across 64–128+ GPU nodes.
- Validate **checkpoint/restart strategies** for long-running training.
- Provide **open-source reproducibility** for the research community.

---

## 🔑 Key Features
| Feature | Description |
|---------|-------------|
| **Multi-node Training** | Distributed PyTorch + MPI/NCCL backend |
| **Fault Tolerance** | Robust checkpoint & restart for week-long runs |
| **Visualization** | Metrics exported to Prometheus & Grafana dashboards |
| **Hybrid Simulation** | Simulates failures, latency, and node variability |
| **Open Source** | Daily publishing of results and logs |

---

## 🏗️ Architecture Diagram
<p align="center">
  <img src="https://raw.githubusercontent.com/github/explore/main/topics/deep-learning/deep-learning.png" width="400">
</p>

---

## 📈 Preliminary Comparisons
| Model | Nodes | GPUs | Training Speed (samples/sec) |
|-------|-------|------|-------------------------------|
| GPT-3 baseline | 32 | 256 | ~50k |
| LLaMA-2 (70B) | 64 | 512 | ~120k |
| **AlphaExaAI** (target) | 128 | 1024 | **~250k** |

---

## 🚀 Roadmap
- **Phase 1 (Now):** Initial debugging and single-node tests ✅  
- **Phase 2:** Scaling to 64 nodes on Polaris 🔜  
- **Phase 3:** Performance benchmarking and Aurora readiness 🔜  
- **Phase 4:** Open results publication and community engagement 🌍  

---

## 📂 Repository Structure
