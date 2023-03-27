#!/bin/bash
#SBATCH --partition=cpu
#SBATCH --output=output.txt
#SBATCH --mail-user=pietro.zgaga@studenti.unipr.it
#SBATCH --mail-type=BEGIN
#SBATCH --time=0-00:10:00


 
module load miniconda3
source "$CONDA_PREFIX/etc/profile.d/conda.sh"
 
conda activate machine-learning-cuda-11.6.0-2022.03.09

python3 convert_data.py 

