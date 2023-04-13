#!/bin/bash
#SBATCH --partition=cpu_infn
#SBATCH --output=output.txt
#SBATCH --mail-user=riccardo.aiudi@unipr.it
#SBATCH --mail-type=BEGIN
#SBATCH --time=0-00:10:00

actual_T=0.5

first_test=0
last_test=3
simulation=test
sigma=1.80
num_temperatures=0

num_tests=$(( $last_test - $first_test + 1))

 module load miniconda3
 source "$CONDA_PREFIX/etc/profile.d/conda.sh"
 conda activate base


for test in $(eval echo "{$first_test..$last_test}")
do
 
 python3 make_files.py  $sigma $simulation $test

done



conda deactivate

for T_idx in $(eval echo "{0..$num_temperatures}")
do

   sbatch  --job-name=outs/${sigma}_lastTest_${last_test}_sim_${simulation}_T_${actual_T}     run_noOMP_bis.sbatch $sigma $first_test $last_test $simulation $actual_T

done
