from variables import *
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 150

megastories = False


csi = np.load(quantities_path + 'csi.npy', allow_pickle= True)
d_csi = np.load(quantities_path + 'd_csi.npy', allow_pickle= True)

if megastories:
 
    csi = np.load(quantities_path + 'csi_from_megastories.npy', allow_pickle= True)
    d_csi = np.load(quantities_path + 'd_csi_from_megastories.npy', allow_pickle= True)

  


print(f"Csi shape is: {csi.shape}")

temps = simulations 
temps = np.array(temps)
print(f"Temperatures are : {temps}")

for index in range(len(Ls)):
    plt.errorbar(temps, csi[:,index]/Ls[index], yerr = d_csi[:,index]/Ls[index], label = str(Ls[index]))

plt.xlabel('Temperature')
plt.ylabel('Csi/L')
plt.legend()
plt.show()