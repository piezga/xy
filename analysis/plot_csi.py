from variables import *
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 150




csi = np.load(quantities_path + 'csi.npy', allow_pickle= True)
d_csi = np.load(quantities_path + 'd_csi.npy', allow_pickle= True)

temps = simulations 
temps = np.array(temps)

for index in range(len(Ls)):
    plt.errorbar(temps, csi[:,index]/Ls[index], yerr = d_csi[:,index]/Ls[index])

plt.xlabel('Temperature')
plt.ylabel('Csi/L')
plt.show()