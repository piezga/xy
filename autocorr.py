import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt


sigmastr = "%0.2f" % 2.50
sigmafloat = float(sigmastr)
name = 'q3'
L = 64
test = 8


mx = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)[:,:20000]
my = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)[:,:20000]
m2 = mx**2 + my**2

plt.figure()
for t in np.arange(9):
    data = m2[t]
    lags = np.arange(len(data))
    acorr = sm.tsa.acf(data, nlags = len(lags)-1)
    plt.plot(acorr, label = str(t))
    plt.legend()    
