#calcola la suscettivita

import numpy as np

Ls = [16,32,64,128,256]
sigmastr = "%0.2f" % 1.80
sigmafloat = float(sigmastr)
tests = np.arange(20)
name = 'real'

T = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_32/magnetization/T.npy', allow_pickle=True)[1:] #stesse T


meanchis = np.empty([len(Ls),len(T)])
errchis = np.empty([len(Ls),len(T)])

        
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

    chis = np.empty([len(tests),len(T)])
    for j,test in enumerate(tests):
        

        mx = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)
        my = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)
        chi = []    
        for k,t  in enumerate(T):
            m2 = mx[k]**2 + my[k]**2
            absm = m2**(1/2)
            chi.append(t*L**(-2)*(m2.mean()-absm.mean()**2))
        chiarr = np.array(chi)
        np.save(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/test_{test}/chi',chiarr, allow_pickle=True)
        chis[j] = chiarr
        
    meanchi = chis.mean(axis=0)
    meanchis[i] = meanchi
    errchis[i] = chis.std(axis=0)/np.sqrt(len(tests)-1)


np.save(f'data/sigma_{sigmastr}/simulation_{name}/meanchis',meanchis, allow_pickle=True)
np.save(f'data/sigma_{sigmastr}/simulation_{name}/errchis',errchis, allow_pickle=True)