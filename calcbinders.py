#calcola i binder

import numpy as np

Ls = [512]
sigmastr = "%0.2f" % 1.80
sigmafloat = float(sigmastr)
tests = np.arange(25)
name = 'taglia512'

T = [0.001]
#np.save(f'data/sigma_{sigmastr}/simulation_{name}/L_1024/magnetization/T',T, allow_pickle=True)

#T = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_1024/magnetization/T.npy', allow_pickle=True) #stesse T

meanbinders = np.empty([len(Ls),len(T)])
errbinders = np.empty([len(Ls),len(T)])

        
for i, L in enumerate(Ls):
    

    #if L == 256:
        #tests = [0,1,2,3,4,5,6,7,9,10]
        #name = 'taglia256'
    #elif L == 64:
        #tests = [1,2,3,4,5,6,7,8,9,10]
        #name = 'q3'
    #elif L ==128:
        #tests = [0,2,3,4,5,6,7,8,9,10]
        #name
    #else:
        #tests = np.arange(11)
        #name = 'sweep'

    binders = np.empty([len(tests),len(T)])
    for j,test in enumerate(tests):
        

        mx = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)[:,-20000:]
        my = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)[:,-20000:]
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