#plotta e salva i binder

import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['figure.dpi'] = 150


Ls = [128]
tests = [0]

sigmastr = "%0.2f" % 1.88
sigmafloat = float(sigmastr)
name = 'sweep'


T = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_128/magnetization/T.npy', allow_pickle=True) #stesse T



        
# for i, L in enumerate(Ls):
    
#     for j,test in enumerate(tests):
#         binder = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/test_{test}/binder.npy')
#         plt.figure(j+1)
#         plt.plot(T,binder, label= 'L' +str(L) +' test'+ str(test),marker='.')
#         plt.legend()
#         binderplotpath = f'data/sigma_{sigmastr}/simulation_{name}/plots/binders/'
#         if not os.path.isdir(binderplotpath):
#             os.makedirs(binderplotpath)
#         if not os.path.isdir(binderplotpath + f'L_{L}'):
#             os.makedirs(binderplotpath + f'L_{L}')
#         plt.savefig(binderplotpath + f'L_{L}/L_{L}_test{test}.png')
        
        
        

    
meanbinders = np.load(f'data/sigma_{sigmastr}/simulation_{name}/meanbinders.npy')
# errbinders = np.load(f'data/sigma_{sigmastr}/simulation_{name}/errbinders.npy')

binderplotpath = f'data/sigma_{sigmastr}/simulation_{name}/plots/binders/'
if not os.path.isdir(binderplotpath):
    os.makedirs(binderplotpath)


plt.figure()
for i,L in enumerate(Ls):
    # plt.errorbar(T,meanbinders[i],errbinders[i], label=str(L),marker = '.')
    plt.plot(meanbinders)
    plt.legend()

# plt.savefig(binderplotpath + 'meanbinders.png')

# plt.show()
