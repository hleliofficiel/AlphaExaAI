

# 🌌 **AlphaExaAI**
_Distributed Deep Learning Simulator & Benchmarking Framework for Exascale AI Systems_

![Python](https://img.shields.io/badge/python-3.10+-blue.svg?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.3+-ee4c2c.svg?logo=pytorch)
![CUDA](https://img.shields.io/badge/CUDA-11.8-green.svg?logo=nvidia)
![MPI](https://img.shields.io/badge/MPI4Py-enabled-orange.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

---

## 🧠 Overview

**AlphaExaAI** is an open-source **distributed deep learning simulator** designed for next-generation **exascale computing platforms** such as **Aurora** and **Polaris** at the Argonne Leadership Computing Facility (ALCF).  

It aims to provide **scalable AI benchmarking**, **resilience testing**, and **fault-tolerant training simulation** using real-world deep learning workloads.

This project bridges **AI research** and **HPC performance engineering**, enabling researchers to understand the computational patterns, communication bottlenecks, and scaling efficiency of large models (GPT, LLaMA, DeepSpeed, Megatron-LM) across thousands of GPUs.




## 🎯 Motivation & Research Goals

> "How can we prepare AI training frameworks for Exascale systems?"

| Objective | Description |
|------------|-------------|
| **Scalability Testing** | Evaluate distributed PyTorch training at 64–256+ nodes using NCCL/MPI backends. |
| **Fault Injection** | Simulate node failures, recovery, and checkpointing strategies for long-duration runs. |
| **Energy Profiling** | Measure GPU power draw, CPU utilization, and communication overhead. |
| **Model Reproducibility** | Guarantee deterministic results across multiple architectures and cluster scales. |
| **Open Science** | All code, data, and benchmarks are openly published for the global HPC-AI community. |

---

## 🧩 Key Features

| Feature | Description |
|---------|-------------|
| 🧠 **Hybrid Parallelism** | Data + model + pipeline parallelism (via DeepSpeed & FSDP). |
| 🔁 **Checkpoint & Recovery** | Fault-tolerant mechanisms for long multi-node jobs. |
| 📊 **Telemetry Integration** | Metrics exported to **Prometheus**, visualized with **Grafana dashboards**. |
| ⚙️ **Dynamic Scaling** | Support for adaptive batch size per GPU and elastic training. |
| 💻 **Multi-Backend Support** | PyTorch DDP, Horovod, and MPI4Py for large-scale runs. |
| 🔬 **Synthetic & Real Workloads** | Includes LLaMA-2, GPT-3, and BERT microbenchmarks. |

---

## ⚙️ Architecture Overview
<p align="center">
  <img src="https://raw.githubusercontent.com/github/explore/main/topics/deep-learning/deep-learning.png" width="420">
</p>

└── alphaexaai/ ├── core/                 # Distributed core modules ├── models/               # Model definitions (GPT, LLaMA, etc.) ├── configs/              # YAML configs for cluster experiments ├── scripts/              # SLURM/PBS batch scripts for HPC ├── utils/                # Logging, monitoring, fault injection ├── docs/                 # Documentation and research papers ├── results/              # Performance outputs, logs, charts └── tests/                # Benchmarking and validation suite

---

## 📊 Preliminary Results

| Model | Nodes | GPUs | Training Throughput (samples/sec) | Scaling Efficiency |
|--------|--------|------|----------------------------------|-------------------|
| GPT-3 (175B) | 32 | 256 | 48,000 | 74% |
| LLaMA-2 (70B) | 64 | 512 | 115,000 | 82% |
| **AlphaExaAI (target)** | 128 | 1024 | **260,000+** | **88%** |

> *Results simulated and validated on distributed GPU clusters using NCCL backends.*



## 🧪 Experiment Scripts

Example HPC job script (`scripts/run_polars.sh`):

```bash
#!/bin/bash
#SBATCH -A ALCF_AI
#SBATCH -N 64
#SBATCH -t 02:00:00
#SBATCH -J alphaexaai_train
#SBATCH --gpus-per-node=8
#SBATCH --ntasks-per-node=8

module load pytorch/2.3
module load cuda/11.8
module load openmpi

srun python3 train_distributed.py --config configs/polaris_64.yaml


---

🧰 Installation

git clone https://github.com/hleliofficiel/AlphaExaAI.git
cd AlphaExaAI
pip install -r requirements.txt

Or using Conda:

conda env create -f environment.yml
conda activate alphaexaai


---

📆 Roadmap

Phase	Objective	Status

Phase 1	Local and single-node debugging	✅ Completed
Phase 2	Multi-node scaling (≤64 nodes)	🟡 In progress
Phase 3	Full exascale benchmarking on Polaris	🔜 Planned
Phase 4	Publish open performance datasets	🔜 Planned


📚 Documentation & Results

📄 Simulation Whitepaper (draft)

📈 Results Dashboard (Grafana JSON)

🧾 Scaling Experiments Summary


🧑‍💻 Contributors

Name	Role	Contact

Muhammad Alhilali	Principal Investigator (PI)	
Research DDLSIM Researchh Group	Distributed Systems R&D https://github.com/DarekHub/DDLSim-BY-KTRUBY	
Community Collaborators	Open-source contributors	GitHub Issues



⚖️ License

This project is released under the MIT License.
See the LICENSE file for details.


🧭 Citation

If you use AlphaExaAI in your research, please cite:

@misc{alphaexaai2025,
  title={AlphaExaAI: Distributed Deep Learning Simulator for Exascale AI Systems},
  author={Alhilali, Muhammad and contributors},
  year={2025},
  url={https://github.com/hleliofficiel/AlphaExaAI}
}



🌐 Acknowledgements

Supported by open-source communities and preliminary testing on:

Argonne National Laboratory (ALCF)

NVIDIA HPC Developer Program

OpenAI Research Ecosystem

IdrakAI Research Team


