from variables import *
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 150


L = 32

csi = np.load(quantities_path + 'csi.npy', allow_pickle= True)
d_csi = np.load(quantities_path + 'd_csi.npy', allow_pickle= True)

temps = np.arange(0.1,1.5,0.1)

plt.errorbar(1/temps, csi[:,0]/L, yerr = d_csi[:,0]/L,fmt='.')
plt.errorbar(1/temps, csi[:,1]/64, yerr = d_csi[:,1]/64,fmt='.')