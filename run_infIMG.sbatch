#!/bin/bash

#SBATCH --partition=cpu

#SBATCH --output=%x.o
#SBATCH --error=%x.e

#SBATCH --mem=32G

#SBATCH --nodes=1

#SBATCH --cpus-per-task=10


#SBATCH --time=3-00:00:00

#SBATCH --mail-user=pietro.zgaga@studenti.unipr.it
#SBATCH --mail-type=END,FAIL




echo "#SLURM_JOB_NODELIST: $SLURM_JOB_NODELIST"

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

echo "#OMP_NUM_THREADS : $OMP_NUM_THREADS"

echo $*


g++ -fopenmp -o executables/main_sigma_$1_simulation_$2_test_$3 -O3 -std=c++11 -DSFMT_MEXP=607 SFMT.c main_infIMG.cpp

./executables/main_sigma_$1_simulation_$2_test_$3 ./data/sigma_$1/simulation_$2/parameters_test_$3.txt  $2 $3  > ./data/sigma_$1/simulation_$2/outputs/output_$3.txt

