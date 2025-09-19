

## 📊 Sample Result (Training Loss Curve)
<p align="center">
  <img src="https://i.sstatic.net/7FnY6.png" width="500">
</p>

---

## 🤝 Contributing
We welcome contributions from researchers and developers worldwide. Please submit issues, pull requests, or open discussions.

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).

---

## 👥 Authors
- **Muhammad ALhilali** – Project Lead, Independent Researcher (Tunisia)  
- **Kaitlyn** – Research CollabCollaborator-

> ⚡ AlphaExaAI is more than just a simulator — it is a foundation for **next-generation AI infrastructure research**, openly accessible to Mohammedmmed
# 📑 AlphaExaAI Documentation

This directory contains extended documentation, research notes, and open results for the **AlphaExaAI** project.  
All files here are maintained openly to provide transparency and reproducibility.  

---

## 📘 Project Vision
AlphaExaAI is an **open-source distributed deep learning simulator** designed for **exascale readiness**.  
Our mission is to create a **scalable, fault-tolerant, and reproducible framework** that can run seamlessly on **Polaris** today and **Aurora** in the near future.  

---

## 📊 Results & Benchmarks
We release benchmark results regularly. Below are highlights of the latest experiments:

| Test | Nodes | GPUs | Samples/sec | Status |
|------|-------|------|-------------|--------|
| Baseline run | 4 | 32 | 8,200 | ✅ Stable |
| Mid-scale | 32 | 256 | 76,500 | ✅ Completed |
| Scaling test | 64 | 512 | 155,000 | 🚧 In progress |
| Target run | 128 | 1024 | **~250,000** | 🔜 Planned |

---

## 🖼️ Visual Reports
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Multi-layer_perceptron.png" width="400">
  <br>
  <em>Figure 1: Example distributed neural network architecture used in AlphaExaAI.</em>
</p>

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/1/10/Deep_learning_performance_scaling.png" width="500">
  <br>
  <em>Figure 2: Hypothetical scaling curve of AlphaExaAI vs other models.</em>
</p>

---

## 🧪 Methodology
1. **Setup**: Deploy distributed environment with PyTorch, MPI4Py, CUDA, NCCL.  
2. **Training**: Run hybrid Transformer models across multiple nodes.  
3. **Fault Injection**: Simulate latency, node failures, and checkpoint recovery.  
4. **Evaluation**: Capture training loss curves, throughput, and efficiency metrics.  
5. **Publishing**: All results and logs are released daily on GitHub.  

---

## 📅 Roadmap
- Publish detailed PDF technical reports for each scaling milestone.  
- Integrate Grafana dashboards for real-time visualization.  
- Expand dataset support (scientific corpora, multilingual benchmarks).  
- Prepare exascale transition report for Aurora readiness.  

---

## 📜 License & Open Science
This project is **100% open source** and licensed under **MIT License**.  
All results, code, and datasets are released for public use.  

