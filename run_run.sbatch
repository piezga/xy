#!/bin/bash
#SBATCH --partition=cpu_infn
#SBATCH --output=output.txt
#SBATCH --mail-user=pietro.zgaga@studenti.unipr.it
#SBATCH --mail-type=BEGIN
#SBATCH --time=0-00:10:00
#SBATCH --qos=cpu_infn

actual_T=0.333
first_test=0
last_test=19
simulation=$actual_T
sigma=1.800
num_temperatures=0

num_tests=$(( $last_test - $first_test + 1))

 module load miniconda3
 source "$CONDA_PREFIX/etc/profile.d/conda.sh"
 conda activate machine-learning-cuda-11.6.0-2022.03.09


for test in $(eval echo "{$first_test..$last_test}")
do
 
 python3 make_files.py   $actual_T True $sigma $simulation $test

done



conda deactivate

for T_idx in $(eval echo "{0..$num_temperatures}")
do

  sbatch  --job-name=xy_${sigma}_sim_${simulation}    run.sbatch $sigma $first_test $last_test $simulation $actual_T

done
