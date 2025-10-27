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


