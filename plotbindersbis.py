import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 150

sigmastr = "%0.2f" % 1.80
Ls = [16, 32, 64, 128, 256, 512, 1024]

T = [0.001, 0.002815, 0.00463, 0.042741, 0.04637037]
T = np.array(T)

binders256 = np.load(f'data/sigma_{sigmastr}/simulation_riccardo/meanbinders.npy')

# binders512_001 = np.load(f'data/sigma_{sigmastr}/simulation_taglia512/meanbinders.npy')
# binders512_001 = np.array(binders512_001)
# indices = [2,3,23,25]
# binders512_others = np.empty([1,len(T)-1])
# binderslow = np.load(f'data/sigma_{sigmastr}/simulation_low/meanbinders.npy')
# for i, index in enumerate(indices):
#     binders512_others[0,i] = binderslow[5,index]
binders512 = np.load(f'data/sigma_{sigmastr}/simulation_riccardo512/meanbinders.npy')



binders1024_001 = np.load(f'data/sigma_{sigmastr}/simulation_new2_2/meanbinders.npy')[0,0]
binders1024_003 = float(np.load(f'data/sigma_{sigmastr}/simulation_sim003_1/meanbinders.npy'))
binders1024_005 = float(np.load(f'data/sigma_{sigmastr}/simulation_sim005_1/meanbinders.npy'))
binders1024_042 = float(np.load(f'data/sigma_{sigmastr}/simulation_sim042_1/meanbinders.npy'))
binders1024_05 = np.load(f'data/sigma_{sigmastr}/simulation_new2_2/meanbinders.npy')[0,1]


binders1024 = [binders1024_001, binders1024_003, binders1024_005, binders1024_042, binders1024_05]
binders1024 = np.array(binders1024)
binders1024 = np.resize(binders1024, [1,5])

meanbinders = np.empty([len(Ls),len(T)])
meanbinders[:5,:] = binders256
meanbinders[5,:] = binders512
meanbinders[6,:] = binders1024

# meanbinders = np.empty([len(Ls),len(T)])
# meanbinders[:5,:] = binders256
# #meanbinders[5,:] = binders512
# meanbinders[5,:] = binders1024
#meanbinders = meanbinders[:,:-1]

errbinders256 = np.load(f'data/sigma_{sigmastr}/simulation_riccardo/errbinders.npy')
errbinders512 = np.load(f'data/sigma_{sigmastr}/simulation_riccardo512/errbinders.npy')

errbinders1024_001 = np.load(f'data/sigma_{sigmastr}/simulation_new2_2/errbinders.npy')[0,0]
errbinders1024_003 = float(np.load(f'data/sigma_{sigmastr}/simulation_sim003_1/errbinders.npy'))
errbinders1024_005 = float(np.load(f'data/sigma_{sigmastr}/simulation_sim005_1/errbinders.npy'))
errbinders1024_042 = float(np.load(f'data/sigma_{sigmastr}/simulation_sim042_1/errbinders.npy'))
errbinders1024_05 = np.load(f'data/sigma_{sigmastr}/simulation_new2_2/errbinders.npy')[0,1]


errbinders1024 = [errbinders1024_001, errbinders1024_003, errbinders1024_005, errbinders1024_042, errbinders1024_05]
errbinders1024 = np.array(errbinders1024)
errbinders1024 = np.resize(errbinders1024, [1,5])

errbinders = np.empty([len(Ls),len(T)])
errbinders[:5,:] = errbinders256
errbinders[5,:] = errbinders512
errbinders[6,:] = errbinders1024






def plot_various_T(T,Ls,binders,sigma,err): 
    cmap = plt.cm.rainbow
    fig,ax = plt.subplots()
    fig.suptitle(str(sigma))
    for i,t in enumerate(T):
        ax.errorbar(np.log(Ls), binders[:,i],
                abs(err[:,i]),               
                color=cmap(i/len(T)),
                label=str(t),
                linestyle = '--', marker='.')
        # plt.xscale('log')
        # plt.yscale('log')
        plt.xlabel(r'$\log(L)$')
        plt.ylabel(r'$\log(1/U_2-1)$')
        plt.legend()
        # Add a colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=T.min(), vmax=T.max()))
    sm.set_array([])
    cbar = plt.colorbar(sm)
    cbar.ax.set_ylabel('$T$')

errplot = errbinders/(meanbinders**2-meanbinders)

plot_various_T(T,Ls,np.log10(1/meanbinders-1),1.80,errplot)

binderL = np.log10(1/meanbinders[:-1] - 1)
binder2L = np.log10(1/meanbinders[1:] - 1)
derivative = binder2L - binderL

errL = errplot[:-1]
err2L = errplot[1:]
errderivative = err2L + errL

plot_various_T(T,Ls[:-1],derivative,1.80,errderivative)