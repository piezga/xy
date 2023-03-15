import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt


sigmastr = "%0.2f" % 2.50
sigmafloat = float(sigmastr)
name = 'q3'
L = 128
test = 7
T = np.load('data/sigma_2.50/simulation_q3/L_128/magnetization/T.npy', allow_pickle=True)[0:2]



mx = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)[:,:4000]
my = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)[:,:4000]
m2 = mx**2 + my**2

plt.figure()


for t, temp in enumerate(T):
    data = m2[t]
    lags = np.arange(len(data))
    acorr = sm.tsa.acf(data, nlags = len(lags)-1)
    intacorr_stat = np.cumsum(acorr)
    # plt.plot(acorr, label = str(t))
    # plt.legend()    
    plt.plot(intacorr_stat, label = str(temp) + ' stats' )
    plt.legend()  
    
for t,temp in enumerate(T):
    data = m2[t]
    ndata = data- np.mean(data)
    var = np.var(data)
    acorr = np.correlate(ndata, ndata, 'full')[len(ndata)-1:] 
    acorr = acorr / var / len(ndata)
    intacorr_np = np.cumsum(acorr)
    # plt.plot(acorr, label = str(t))
    # plt.legend()    
    plt.plot(intacorr_stat, '.', label = str(temp) + ' np')
    plt.legend()  


#rifai con taglie piccole e potrebbe esserci un plateau, poi fai media sui test
#2.1 (boh) e 1.88 (0.5-0.75)  1M
#script coeff rette all'andare di 1/L 2 a 2
#cross check autocorr