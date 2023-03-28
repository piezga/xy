import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 150

Ls = [16,32,64,128,256,512]

Tlow = T = np.load('data/sigma_1.80/simulation_low/L_128/magnetization/T.npy', allow_pickle=True)
Tlower = T = np.load('data/sigma_1.80/simulation_lowzoom/L_128/magnetization/T.npy', allow_pickle=True)
T = np.append(Tlower,Tlow)

binderslow = np.load('data/sigma_1.80/simulation_low/meanbinders.npy')
binderslower = np.empty([len(Ls),len(Tlower)])
binderslower[:5,:] = np.load('data/sigma_1.80/simulation_lowzoom/meanbinders.npy')
binderslower[5,:] = np.zeros(len(Tlower))
meanbinders = np.append(binderslower, binderslow, axis=1)

sortorder = np.argsort(T)
meanbinders = meanbinders[:,sortorder]


def plot_various_T(T,Ls,binders,sigma): 
    cmap = plt.cm.rainbow
    fig,ax = plt.subplots()
    fig.suptitle(str(sigma))
    for i,t in enumerate(T):
        ax.plot(np.log(Ls), binders[:,i],
                #err_binders[:,i]/(1-binders[:,i]),     #errore giusto                
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

