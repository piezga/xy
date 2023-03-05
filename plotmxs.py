#plotta la mx dei test i

import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['figure.dpi'] = 150


Ls = [16,32,64,128,256]
test = 2  #scegli il test
sigmastr = "%0.2f" % 2.10
sigmafloat = float(sigmastr)
sigmaname = int(sigmafloat*100)
mypath = 'data/sigma_{sigmastr}/simulation_sigma{sigmaname}/plots/'   #creo cartella plots
if not os.path.isdir(mypath):
    os.makedirs(mypath)
    
    
for L in Ls:
    
    Lpath = f'data/sigma_{sigmastr}/simulation_sigma{sigmaname}/plots/L_{L}/' 
    if not os.path.isdir(Lpath):
        os.makedirs(Lpath)
    
    mx = np.load(f'data/sigma_{sigmastr}/simulation_sigma{sigmaname}/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)
    my = np.load(f'data/sigma_{sigmastr}/simulation_sigma{sigmaname}/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True) 
    magpath = f'data/sigma_{sigmastr}/simulation_sigma{sigmaname}/L_{L}/magnetization/plots_test_{test}/'
    if not os.path.isdir(magpath):
        os.makedirs(magpath)
    T = np.load(f'data/sigma_{sigmastr}/simulation_sigma{sigmaname}/L_{L}/magnetization/T.npy', allow_pickle=True)
    for t in range(len(T)):
        # fig, ax = plt.subplots()
        # ax.plot(mx[t])
        # ax.set(xlabel = 'timestep', ylabel = 'mx', title = 'T = ' + str(T[t]))
        # ax.grid()
        # plt.savefig(magpath + f'T_{t}_' + str(T[t]) + '.png')
        # plt.close()
        plt.figure()
        plt.scatter(mx[t],my[t])
        plt.savefig(magpath + f'scatterT_{t}_' + str(T[t]) + '.png')
        
        