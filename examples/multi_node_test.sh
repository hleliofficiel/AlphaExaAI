#!/bin/bash
#PBS -l select=2:ncpus=32:ngpus=4
#PBS -l walltime=01:00:00
#PBS -q debug

module load conda
conda activate base

mpirun -np 8 python src/train.py --config configs/config_baseline.yaml
