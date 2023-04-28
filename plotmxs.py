#plotta la mx dei test i

import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['figure.dpi'] = 150


Ls = [1024]
tests = np.arange(100)  #scegli il test
sigmastr = "%0.2f" % 1.80
sigmafloat = float(sigmastr)
sigmaname = 'new2_2'
mypath = 'data/sigma_{sigmastr}/simulation_sigma{sigmaname}/plots/'   #creo cartella plots
if not os.path.isdir(mypath):
    os.makedirs(mypath)
    
    
for L in Ls:
    T = np.load(f'data/sigma_{sigmastr}/simulation_{sigmaname}/L_{L}/magnetization/T.npy', allow_pickle=True)

    Lpath = f'data/sigma_{sigmastr}/simulation_sigma{sigmaname}/plots/L_{L}/' 
    if not os.path.isdir(Lpath):
        os.makedirs(Lpath)
        
    mag = np.empty([len(tests),170000])

    for test in tests:
        mx = np.load(f'data/sigma_{sigmastr}/simulation_{sigmaname}/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)[0][:170000]
        my = np.load(f'data/sigma_{sigmastr}/simulation_{sigmaname}/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)[0][:170000]
        mag[test]= mx**2 + my**2

        # plt.figure(8)
        # plt.plot(mx[0],label=f'{test}')
        # plt.legend()
    
    meanmag = mag.mean(axis=0)
    magerror = mag.std(axis=0)/np.sqrt(len(tests)-1)
    plt.figure()
    plt.errorbar(range(len(meanmag)),meanmag,magerror)
    
    # magpath = f'data/sigma_{sigmastr}/simulation_{sigmaname}/L_{L}/magnetization/plots_test_{test}/'
    # if not os.path.isdir(magpath):
    #     os.makedirs(magpath)
    # for t in range(len(T)):
    #     fig, ax = plt.subplots()
    #     ax.plot(mx[t])
    #     ax.set(xlabel = 'timestep', ylabel = 'mx', title = 'T = ' + str(T[t]))
    #     ax.grid()
        # plt.savefig(magpath + f'T_{t}_' + str(T[t]) + '.png')
        # plt.close()
        # plt.figure()
        # plt.scatter(mx[t],my[t])
        # plt.savefig(magpath + f'scatterT_{t}_' + str(T[t]) + '.png')
    

        
        
        