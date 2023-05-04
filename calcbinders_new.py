#calcola i binder

import numpy as np

Ls = [1024]
sigmastr = "%0.2f" % 1.80
sigmafloat = float(sigmastr)
tests = np.arange(100)
name = 'real_1'

#T = [0.17148148, 0.25222222, 0.33296296, 0.93851852, 1.05962963]
#T = np.array(T)
#np.save(f'data/sigma_{sigmastr}/simulation_{name}/L_1024/magnetization/T',T, allow_pickle=True)

#T = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_16/magnetization/T.npy', allow_pickle=True) #stesse T
T = np.arange(5)

meanbinders_new = np.empty([len(Ls),len(T)])
errbinders_new = np.empty([len(Ls),len(T)])

        
for i, L in enumerate(Ls):
    print('Calculating size ' + str(L))
    binders = np.empty([len(tests),len(T)])
    m2matrix = np.zeros((len(T),len(tests)))
    m4matrix = np.zeros((len(T),len(tests)))
    for j, test in enumerate(tests):
        m2s = []
        m4s= []
        dm2s = []
        dm4s = []
        mx = np.load(f'data/sigma_1.80/simulation_{name}/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)
        my = np.load(f'data/sigma_1.80/simulation_{name}/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)
        for t in range(len(T)):
            m2 = mx[t]**2 + my[t]**2
            m4 = m2**2
            m2_meantime = np.mean(m2)
            m4_meantime = np.mean(m4)
            m2s = np.append(m2s,m2_meantime)
            m4s = np.append(m4s,m4_meantime)
        m2matrix[:,j] = m2s
        m4matrix[:,j] = m4s
    m2 = np.mean(m2matrix,axis=1)
    dm2vec = np.std(m2matrix,axis=1)/np.sqrt(len(tests)-1)
    m4 = np.mean(m4matrix,axis=1)
    dm4vec = np.std(m4matrix,axis=1)/np.sqrt(len(tests)-1)
    binder = 2 - m4/(m2**2)
    errbinder = abs(binder)*np.sqrt((dm4vec/m4)**2 + 4*(dm2vec/m2)**2)
    meanbinders_new[i,:] = binder
    errbinders_new[i,:] = errbinder
    
        # for t in range(len(T)):
        #     m2 = mx[t]**2 + my[t]**2
        #     m4 = m2**2 
        #     m2s.append(np.mean(m2))
        #     m4s.append(np.mean(m4))
        
        
#     meanbinder = binders.mean(axis=0)
#     meanbinders_new[i] = meanbinder
#     errbinders_new[i] = binders.std(axis=0)/np.sqrt(len(tests)-1)
np.save(f'data/sigma_{sigmastr}/simulation_{name}/meanbinders_new',meanbinders_new, allow_pickle=True)
np.save(f'data/sigma_{sigmastr}/simulation_{name}/errbinders_new',errbinders_new, allow_pickle=True)
