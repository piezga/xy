import numpy as np
import sys
import os


#External storage flag
external_usb = 0

#Simulation variables
sigma = '1.200'

simulation_values = np.arange(0.5,1.4,0.1)
simulations = [f'{value:.1f}' for value in simulation_values]

manual_simulation_ID = 0

Ls = np.array([32,64,128])

tests = 2


################################################################


#This allows for script to be called directly or from bash files
if os.getenv('CALLED_FROM_BASH') == '1':
    print("Script called from Bash")
    sim_ID = int(sys.argv[1])

else:
    print("Script called directly or from another source")
    sim_ID = manual_simulation_ID

simulation = simulations[sim_ID]

#simulation = '1.4'

################################################################

#Path construction
usb_drive_path = '/media/piezga/toshiba/xy/'
data_path =   '../data/sigma_'+sigma+'/'
path = data_path+'simulation_'+str(simulation)
quantities_path = data_path + 'global_quantities/'


if external_usb:
    path = usb_drive_path +'simulation_'+str(simulation)



#Information printing
print('Simulation: ', simulation)
print('SIGMA: ', sigma)
print('Path is ', path)



#Legacy junk 
chi_error_factor = 1
num_of_estim = 2
block_size = 10**4
d = 2
