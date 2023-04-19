import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 150

sigmastr = "%0.2f" % 1.80
Ls = [512,1024]

T = [0.001, 0.04637037]
T = np.array(T)

binders1024 = np.load(f'data/sigma_{sigmastr}/simulation_new2/meanbinders.npy')
binders512low = np.load(f'data/sigma_{sigmastr}/simulation_taglia512/meanbinders.npy')
binders512high = np.load(f'data/sigma_{sigmastr}/simulation_low/meanbinders.npy')[5,25]

meanbinders = np.empty([2,len(T)])

meanbinders[0,0] = binders512low
meanbinders[0,1] = binders512high
meanbinders[1,:] = binders1024


def plot_various_T(T,Ls,binders,sigma): 
    cmap = plt.cm.rainbow
    fig,ax = plt.subplots()
    fig.suptitle(str(sigma))
    for i,t in enumerate(T):
        ax.plot(np.log(Ls), binders[:,i],
                #err_binders[:,i]/(1-binders[:,i]),     #errore giusto                
                color=cmap(i/len(T)),
                label=str(t),
                linestyle = '--', marker='.')
        # plt.xscale('log')
        # plt.yscale('log')
        plt.xlabel(r'$\log(L)$')
        plt.ylabel(r'$\log(1/U_2-1)$')
        # Add a colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=T.min(), vmax=T.max()))
    sm.set_array([])
    cbar = plt.colorbar(sm)
    cbar.ax.set_ylabel('$T$')


plot_various_T(T,Ls,np.log10(1/meanbinders-1),1.80)

binderL = np.log10(1/meanbinders[:-1] - 1)
binder2L = np.log10(1/meanbinders[1:] - 1)
derivative = binder2L - binderL

plot_various_T(T,Ls[:-1],derivative,1.80)