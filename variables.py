import numpy as np

if __name__ == "__main__":
    print('Just a module! There is not a reason to execute it!')


g_drive_dir = ''#G:/Other computers/principal/Università/DOTTORATO/Codes/dll/'

d = 2
test = 6
simulation = 'sigma210'

sigma = '2.10'

data_path = g_drive_dir + 'data/sigma_'+sigma+'/'
#for 1D:
if d == 1:
    data_path = g_drive_dir +  'data/1D/sigma_'+sigma+'/'

path = data_path+'simulation_'+str(simulation)#+'/old/'





print('simulation: ', simulation)
print('SIGMA: ', sigma)

Ls_chosen = np.array([16,32,64,128,256])#16,32,45,64,90,128,181,256,362,512,750 #45,90,181,362
#16,32,64,128,256,512,45,90,181,362,724
if d == 1:
    Ls_chosen = np.array([512,1024,2048,4096,8192,16384,32768])#,8192,16384,32768,65536

    
chi_error_factor = 1



num_of_estim = 2#120

block_size = 10**4#2**12#2**15


#test per github
