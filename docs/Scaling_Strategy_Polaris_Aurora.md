# Scaling Strategy — Polaris → Aurora

## Goals
- Achieve high scaling efficiency from 32 → 256 GPU nodes  
- Optimize NCCL, PCIe, and interconnect utilization  
- Validate distributed parallel strategies  
- Prepare for Aurora-class architecture  

---

## Scaling Plan
### Scaling steps:
| Nodes | GPUs | Purpose |
|-------|------|---------|
| 8     | 64   | Baseline throughput |
| 16    | 128  | Early scaling |
| 32    | 256  | Tensor parallel validation |
| 64    | 512  | MoE expert scaling |
| 128   | 1024 | Full training stage |
| 256   | 2048 | Aurora transition |

---

## NCCL Optimization
- `NCCL_SOCKET_IFNAME=ib0`  
- Enable NVLink affinity tuning  
- Use hierarchical all-reduce strategy  
- Overlap compute/communication using CUDA Graphs  

---

## Failure Recovery
- Kill-node simulation every 24–48 hours  
- Automatic resume from last checkpoint  
- Node-drop tolerant elastic scaling  

---

## Transition to Aurora
- Adapt TP/PP layers to match Aurora tile topology  
- Retune kernels for Xe architecture  
- Test memory-bandwidth-bound operations  
- Validate FP8 mixed precision support  
