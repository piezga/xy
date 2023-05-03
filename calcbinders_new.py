#calcola i binder

import numpy as np

Ls = [16,32,64,128,256]
sigmastr = "%0.2f" % 1.80
sigmafloat = float(sigmastr)
tests = np.arange(20)
name = 'low'

#T = [0.17148148, 0.25222222, 0.33296296, 0.93851852, 1.05962963]
#T = np.array(T)
#np.save(f'data/sigma_{sigmastr}/simulation_{name}/L_1024/magnetization/T',T, allow_pickle=True)

T = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_16/magnetization/T.npy', allow_pickle=True)[:5] #stesse T

meanbinders_new = np.empty([len(Ls),len(T)])
errbinders_new = np.empty([len(Ls),len(T)])

        
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

    
    for t in range(len(T)):
        m2s = []
        m4s= []
        for j, test in enumerate(tests):
            mx = np.load(f'data/sigma_1.80/simulation_{name}/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)[t,:]
            my = np.load(f'data/sigma_1.80/simulation_{name}/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)[t,:]
            m2 = mx**2 + my**2
            m4 = m2**2
            m2_meantime = np.mean(m2)
            m4_meantime = np.mean(m4)
            m2s = np.append(m2s,m2_meantime)
            m4s = np.append(m4s,m4_meantime)
        m2 = np.mean(m2s)
        m4 = np.mean(m4s)
        binder = 2 - m4/(m2**2)
        meanbinders_new[i,t] = binder
    
        # for t in range(len(T)):
        #     m2 = mx[t]**2 + my[t]**2
        #     m4 = m2**2 
        #     m2s.append(np.mean(m2))
        #     m4s.append(np.mean(m4))
        
        
#     meanbinder = binders.mean(axis=0)
#     meanbinders_new[i] = meanbinder
#     errbinders_new[i] = binders.std(axis=0)/np.sqrt(len(tests)-1)

# #salva binder separatamente
# np.save(f'data/sigma_{sigmastr}/simulation_{name}/meanbinders_new',meanbinders_new, allow_pickle=True)
# np.save(f'data/sigma_{sigmastr}/simulation_{name}/errbinders_new',errbinders_new, allow_pickle=True)
