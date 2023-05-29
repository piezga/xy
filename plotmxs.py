#plotta la mx dei test i

import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['figure.dpi'] = 150


Ls = [1024]
tests = np.arange(100)  
sigmastr = "%0.2f" % 1.80
sigmafloat = float(sigmastr)
sigmaname = 'simT003_0_bis'
npoints = 150*10**3
temperature_index = 0
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
        mx = np.load(f'data/sigma_{sigmastr}/simulation_{sigmaname}/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)[temperature_index,-npoints:]
        my = np.load(f'data/sigma_{sigmastr}/simulation_{sigmaname}/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)[temperature_index,-npoints:]
        mag[test]= mx**2 + my**2

        # plt.figure(8)
        # plt.plot(mx[0],label=f'{test}')
        # plt.legend()
    
    meanmag = mag.mean(axis=0)
    magerror = mag.std(axis=0)/np.sqrt(len(tests)-1)
    plt.figure()
    plt.xlabel('t [Steps]')
    plt.ylabel('Magnetization')
    plt.errorbar(range(len(meanmag)),meanmag,magerror)
    #plt.plot(range(len(meanmag)),meanmag)
    #plt.figure()
    #plt.plot(range(len(meanmag)), mx[0,:])

    

plt.show()

        
        
        