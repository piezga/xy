#calcola i binder

import numpy as np

Ls = [128]#[16,32,64,128,256]



T = np.load('data/sigma_2.50/simulation_q3/L_128/magnetization/T.npy', allow_pickle=True) #stesse T


meanbinders = np.empty([len(Ls),len(T)])
errbinders = np.empty([len(Ls),len(T)])

        
for i, L in enumerate(Ls):
    
    sigmastr = "%0.2f" % 1.88
    sigmafloat = float(sigmastr)
    if L == 256:
        tests = [0,1,2,4,5,6,7,8,9]
        name = 'taglia256'
    elif L == 64:
        tests = [0,1,2,3,4,5,6,7,9,10,11]
        name = 'q3'
    else:
        tests = [0]
        name = 'sweep'

    binders = np.empty([len(tests),len(T)])
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

