from variables import *
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 150


L = 32

csi = np.load(data_path + 'csi.npy', allow_pickle= True)
d_csi = np.load(data_path + 'd_csi.npy', allow_pickle= True)

temps = np.arange(0.1,1.5,0.1)

plt.errorbar(temps, csi.ravel(), yerr = d_csi.ravel())