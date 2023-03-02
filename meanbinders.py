#plotta media dei binder

import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['figure.dpi'] = 150
Ls = [16,32,128,256]
tests = np.arange(0,6)  #per ora hardcoded
T = np.load('data/sigma_2.10/simulation_sigma210/L_16/magnetization/T.npy', allow_pickle=True) #stesse T

binders = np.empty([len(tests),len(T)])
meanbinders = np.empty([len(Ls),len(T)])
for i, L in enumerate(Ls):
    for test in tests:
        mx = np.load(f'data/sigma_2.10/simulation_sigma210/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)
        my = np.load(f'data/sigma_2.10/simulation_sigma210/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)
        binder = []    
        m = []
        for t in range(len(T)):
            m2 = mx[t]**2 + my[t]**2
            m4 = m2**2 
            binder.append(2 - m4.mean()/m2.mean()**2)
    bindarr = np.array(binder).reshape(1,28)
    binders[i] = bindarr
meanbinder = binders.mean(axis=0).reshape(1,28)
meanbinders[i] = meanbinder



