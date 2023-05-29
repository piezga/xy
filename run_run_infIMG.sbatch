#!/bin/bash
#SBATCH --qos=cpu_infn
#SBATCH --output=output.txt
#SBATCH --mail-user=pietro.zgaga@studenti.unipr.it
#SBATCH --mail-type=BEGIN
#SBATCH --time=0-00:10:00


sigma=1.80
simulation=sweep_2_infIMG

for i in {0..19}
do
 
 module load miniconda3
 source "$CONDA_PREFIX/etc/profile.d/conda.sh"
 conda activate machine-learning-cuda-11.6.0-2022.03.09

 python3 make_files.py True $sigma $simulation $i

 conda deactivate

 sbatch  --job-name=outs/xy_dll_${sigma}_$i      run_infIMG.sbatch  $sigma $simulation $i
done
