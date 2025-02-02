from variables import *
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 150


Ls = [64,128,256]


csi = np.load(quantities_path + 'csi.npy', allow_pickle= True)
d_csi = np.load(quantities_path + 'd_csi.npy', allow_pickle= True)

temps =  ['0.6','0.8','1','1.2','1.4','1.6']
temps = np.array(temps)

for index in range(4):
    plt.errorbar(temps, csi[:,index]/Ls[index], yerr = d_csi[:,index]/Ls[index])

plt.xlabel('Temperature')
plt.ylabel('Csi/L')
plt.legend()