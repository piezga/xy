#plotta e salva i binder

import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['figure.dpi'] = 150


Ls = [16,32,64,128]

sigmastr = "%0.2f" % 1.80
sigmafloat = float(sigmastr)
name = 'sweep_infIMG'


T = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_16/magnetization/T.npy', allow_pickle=True) #stesse T
    
meanbinders = np.load(f'data/sigma_{sigmastr}/simulation_{name}/meanbinders_new.npy')

errbinders = np.load(f'data/sigma_{sigmastr}/simulation_{name}/errbinders_new.npy')





### selezione delle temperature

# indices = [2,3,23,25]

# T = [T[i] for i in indices]
# T = np.array([T])
# T = np.resize(T,[4,])

# meanbinders = np.empty([len(Ls),len(T)])
# for i, index in enumerate(indices):
#     meanbinders[:,i] = binders[:,index]


###


binderplotpath = f'data/sigma_{sigmastr}/simulation_{name}/plots/binders/'
if not os.path.isdir(binderplotpath):
    os.makedirs(binderplotpath)


plt.figure()
for i,L in enumerate(Ls):
    plt.plot(T,meanbinders[i], label=str(L),marker = '.')
    plt.legend()

plt.savefig(binderplotpath + 'meanbinders.png')

plt.show()

