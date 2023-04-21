#plotta la m dei test i

import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['figure.dpi'] = 150


Ls = [1024] #[16,32,64,128,256]
tests = np.arange(4) #scegli il test
t = 0
sigmastr = "%0.2f" % 1.80
sigmafloat = float(sigmastr)
name = 'sim003'
mypath = 'data/sigma_{sigmastr}/simulation_{name}/plots/'   #creo cartella plots
if not os.path.isdir(mypath):
    os.makedirs(mypath)
    
    
for L in Ls:
    for i, test in enumerate(tests):
    
        Lpath = f'data/sigma_{sigmastr}/simulation_{name}/plots/L_{L}/' 
        if not os.path.isdir(Lpath):
            os.makedirs(Lpath)
        
        mx = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)[t,10000:]
        my = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)[t,10000:]
        magpath = f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/plots_test_{test}/'
        
        if not os.path.isdir(magpath):
            os.makedirs(magpath)
            
        T = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/T.npy', allow_pickle=True)

    
        #mx = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/mx_test_{i}.npy', allow_pickle=True)[3]
        #my = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/my_test_{i}.npy', allow_pickle=True)[3]
        
        m2 = mx**2 + my**2
        
        plt.figure(i+1)
        plt.scatter(mx,my, label = str(test) + ' temp ' + str(T[t]))
        plt.legend()
        # plt.plot(m2, label = str(test))
        # plt.legend()        
        
    
    
    # for t in range(20):
    #     plt.figure()
    #     plt.plot(m2[t])
    #     plt.title(str(T[t]))
        #plt.savefig(magpath + f'scatterT_{t}_' + str(T[t]) + '.png')
        
    
