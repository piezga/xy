#!/bin/bash
#SBATCH --partition=cpu
#SBATCH --output=output.txt
#SBATCH --mail-user=pietro.zgaga@studenti.unipr.it
#SBATCH --mail-type=BEGIN
#SBATCH --time=0-00:10:00


sigma=1.76
simulation=800k

#era 9
for i in {0..14}
do
 
 module load miniconda3
 source "$CONDA_PREFIX/etc/profile.d/conda.sh"
 
 conda activate machine-learning-cuda-11.6.0-2022.03.09


 python3 make_files.py True $sigma $simulation $i

 conda deactivate

 sbatch  --job-name=outs/xy_dll_${sigma}_$i      run.sbatch  $sigma $simulation $i
done
