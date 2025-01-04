#plotta la m dei test i
from functions import *
import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['figure.dpi'] = 150


#Tests and starting point
tests = np.arange(1)
t = 0

print(path) 
for L in Ls:
    for i, test in enumerate(tests):
    
                
        mx = np.load(path + f'/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)[t,:]
        my = np.load(path + f'/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)[t,:]
                
        mx_re = np.load(path + f'/L_{L}/magnetization/mx_re_test_{test}.npy', allow_pickle=True)[t,:]
        my_re = np.load(path + f'/L_{L}/magnetization/my_re_test_{test}.npy', allow_pickle=True)[t,:]

                
        mx_im = np.load(path + f'/L_{L}/magnetization/mx_im_test_{test}.npy', allow_pickle=True)[t,:]
        my_im = np.load(path + f'/L_{L}/magnetization/my_im_test_{test}.npy', allow_pickle=True)[t,:]



        plot_path = path +  f'/L_{L}/plots_L_{L}/'

        if not os.path.isdir(plot_path):
            os.makedirs(plot_path)
            
        T = np.load(path + f'/L_{L}/magnetization/T.npy', allow_pickle=True)

    
        m2 = mx**2 + my**2
        
        plt.figure()
        plt.xlabel('Timestep')
        plt.ylabel('Magnetization')
        plt.plot(mx_im, label = 'Test ' + str(test))
        plt.legend()        
        # plt.savefig(plot_path + f'm2_test_{test}.png')
        print('Shape of m2 is ' + str(np.shape(m2)) )
        #plt.close() 
    
        

plt.show()
