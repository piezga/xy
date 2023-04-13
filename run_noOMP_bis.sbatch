#!/bin/bash
 
#SBATCH --qos=cpu_infn

#SBATCH --partition=cpu_infn

#SBATCH --output=%x.o
#SBATCH --error=%x.e

#SBATCH --ntasks=4

#SBATCH --cpus-per-task=1 
#SBATCH --mem-per-cpu=1G 




#SBATCH --time=3-00:00:00
#SBATCH --mail-user=riccardo.aiudi@unipr.it --mail-type=END




sigma=$1
first_test=$2
last_test=$3
simulation=$4
actual_T=$5




for test in $(eval echo "{$first_test..$last_test}")
do

g++ -fopenmp -o executables/main_sigma_${sigma}_simulation_${simulation}_test_${test}_T_${actual_T} -O3 -std=c++11 -DSFMT_MEXP=607 SFMT.c main_bis.cpp
srun --ntasks=1 --nodes=1 --cpus-per-task=$SLURM_CPUS_PER_TASK  --job-name=outs/${sigma}_test_${test}_sim_${simulation}_T_${actual_T} ./executables/main_sigma_${sigma}_simulation_${simulation}_test_${test}_T_${actual_T} ./data/sigma_${sigma}/simulation_${simulation}/parameters_test_${test}.txt  ${simulation} ${test}  > ./data/sigma_${sigma}/simulation_${simulation}/outputs/output_${test}_T_${actual_T}.txt &




done
wait
