#plotta la mx dei test i

import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['figure.dpi'] = 150


Ls = [1024]
tests = np.arange(100)  #scegli il test
sigmastr = "%0.2f" % 1.80
sigmafloat = float(sigmastr)
sigmaname = 'simT003_2'
npoints = 150000

mypath = 'data/sigma_{sigmastr}/simulation_sigma{sigmaname}/plots/'   #creo cartella plots
if not os.path.isdir(mypath):
    os.makedirs(mypath)
    
    
for L in Ls:
    #T = np.load(f'data/sigma_{sigmastr}/simulation_{sigmaname}/L_{L}/magnetization/T.npy', allow_pickle=True)

    Lpath = f'data/sigma_{sigmastr}/simulation_sigma{sigmaname}/plots/L_{L}/' 
    # if not os.path.isdir(Lpath):
    #     os.makedirs(Lpath)
        
    mag = np.empty([len(tests),npoints])

    for test in tests:
        mx = np.load(f'data/sigma_{sigmastr}/simulation_{sigmaname}/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)[:,-npoints:]
        my = np.load(f'data/sigma_{sigmastr}/simulation_{sigmaname}/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)[:,-npoints:]
        mag[test]= mx**2 + my**2

        # plt.figure(8)
        # plt.plot(mx[0],label=f'{test}')
        # plt.legend()
    
    meanmag = mag.mean(axis=0)
    magerror = mag.std(axis=0)/np.sqrt(len(tests)-1)
    plt.figure()
    plt.errorbar(range(len(meanmag)),meanmag,magerror)
    

plt.show()

        
        
        