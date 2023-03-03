#calcola i binder

import numpy as np

Ls = [16,32,64,128,256]
tests = np.arange(6)

sigmastr = "%0.2f" % 2.10
sigmafloat = float(sigmastr)
name = 'sigma'+ str(int(sigmafloat*100))


T = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_16/magnetization/T.npy', allow_pickle=True) #stesse T


binders = np.empty([len(tests),len(T)])
meanbinders = np.empty([len(Ls),len(T)])
errbinders = np.empty([len(Ls),len(T)])

        
for i, L in enumerate(Ls):
    for j,test in enumerate(tests):
        mx = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)
        my = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)
        binder = []    
        for t in range(len(T)):
            m2 = mx[t]**2 + my[t]**2
            m4 = m2**2 
            binder.append(2 - m4.mean()/m2.mean()**2)
        bindarr = np.array(binder)
        np.save(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/test_{test}/binder',bindarr, allow_pickle=True)
        binders[j] = bindarr
        
    meanbinder = binders.mean(axis=0)
    meanbinders[i] = meanbinder
    errbinders[i] = binders.std(axis=0)/np.sqrt(len(tests)-1)
    
#salva binder separatamente
np.save(f'data/sigma_{sigmastr}/simulation_{name}/meanbinders',meanbinders, allow_pickle=True)
np.save(f'data/sigma_{sigmastr}/simulation_{name}/errbinders',errbinders, allow_pickle=True)

