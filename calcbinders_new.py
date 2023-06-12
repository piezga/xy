#calcola i binder

import numpy as np

Ls = [16,32,64,128,256]
sigmastr = "%0.2f_infIMG" % 4.00
#sigmafloat = float(sigmastr)
tests = np.arange(100)
names = ['T01_bis', 'T02_bis']

#T = [0.17148148, 0.25222222, 0.33296296, 0.93851852, 1.05962963]
#T = np.array(T)
#np.save(f'data/sigma_{sigmastr}/simulation_{name}/L_1024/magnetization/T',T, allow_pickle=True)

#T = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_16/magnetization/T.npy', allow_pickle=True) #stesse T
T = np.arange(1)


def covariance(A, B, mean_A, mean_B):
    """
    Calculate the covariance between two arrays A and B.

    Parameters:
    -----------
    A : array-like
        First array.
    B : array-like
        Second array.
    mean_A : float
        Mean of A.
    mean_B : float
        Mean of B.

    Returns:
    --------
    float
        Covariance between A and B.
    """

    cov_AB = np.mean((A - mean_A) * (B - mean_B), axis = 0)
    #print('covariance ', cov_AB)



    return cov_AB



meanbinders_new = np.empty([len(Ls),len(T)])
errbinders_new = np.empty([len(Ls),len(T)])

for name in names:
    print('Elaborating ' + name )
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
            mx = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)
            my = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)
            for t in range(len(T)):
                m2 = mx[t]**2 + my[t]**2
                m4 = m2**2
                m2_meantime = np.mean(m2)
                m4_meantime = np.mean(m4)
                m2s = np.append(m2s,m2_meantime)
                m4s = np.append(m4s,m4_meantime)
            m2matrix[:,j] = m2s
            m4matrix[:,j] = m4s
        
        cov42 = np.ones(len(T))
    
        
            
        #m2matrix è matrice la cui entrata ij è m2 alla temperatura i del test j. Idem m4matrix
            
        m2 = np.mean(m2matrix,axis=1)
        sigma2 = np.std(m2matrix,axis=1)/np.sqrt(len(tests)-1)
        m4 = np.mean(m4matrix,axis=1)
        sigma4 = np.std(m4matrix,axis=1)/np.sqrt(len(tests)-1)
        
        for t in range(len(T)):
            cov42[t] = covariance(m2matrix[t],m4matrix[t], m2[t],m4[t])/(len(tests)-1)
    
        binder = 2 - m4/(m2**2)
        #print('(sigma4/m4)**2 = ' + str((sigma4/m4)**2))
        #print('4*(sigma2/m2)**2 = ' + str(4*(sigma2/m2)**2))
        #print('4*cov42/(m4*m2) = ' + str(4*cov42/(m4*m2)))
        errbinder = (m4/m2**2) * np.sqrt((sigma4/m4)**2 + 4*(sigma2/m2)**2 -4*cov42/(m4*m2))
        meanbinders_new[i,:] = binder
        errbinders_new[i,:] = errbinder
        
    np.save(f'data/sigma_{sigmastr}/simulation_{name}/meanbinders_new',meanbinders_new, allow_pickle=True)
    np.save(f'data/sigma_{sigmastr}/simulation_{name}/errbinders_new',errbinders_new, allow_pickle=True)
