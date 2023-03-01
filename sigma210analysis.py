#test0

import numpy as np
import matplotlib.pyplot as plt

temps = np.load('data/sigma_2.10/simulation_sigma210/L_256/magnetization/T.npy', allow_pickle=True)
mx = np.load('data/sigma_2.10/simulation_sigma210/L_256/magnetization/mx_test_0.npy', allow_pickle=True)
my = np.load('data/sigma_2.10/simulation_sigma210/L_256/magnetization/my_test_0.npy', allow_pickle=True)



fig, (ax1,ax2) = plt.subfigure(2)
ax1 = plt.p