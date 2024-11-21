import numpy as np
import sys
import os


#External storage flag
external_usb = 0

#Simulation variables
sigma = '1.800'
simulations = ['0.0001','0.001','0.023','0.38','0.67','0.72']
manual_simulation_ID = 2
Ls = np.array([1024])
test = 80 


################################################################


#This allows for script to be called directly or from bash files
if os.getenv('CALLED_FROM_BASH') == '1':
    print("Script called from Bash")
    sim_ID = int(sys.argv[1])

else:
    print("Script called directly or from another source")
    sim_ID = manual_simulation_ID

simulation = simulations[sim_ID]

#simulation = '0.123'

################################################################

#Path construction
usb_drive_path = '/media/piezga/toshiba/xy/'
data_path =   '../data/sigma_'+sigma+'/'
path = data_path+'simulation_'+str(simulation)

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