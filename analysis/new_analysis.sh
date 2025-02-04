#!/bin/bash


#scp -r pietro.zgaga@login.hpc.unipr.it:/hpc/home/pietro.zgaga/zgaga/data/sigma_1.800_proper /media/piezga/EXTERNAL_USB/xy/data/

export CALLED_FROM_BASH=1

for sim_number in {0..11}
do
     
    python take_data.py $sim_number
    #python analysis_non_spatial.py $sim_number
    #python present_binders.py $sim_number
done

