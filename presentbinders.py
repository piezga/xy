import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 150

sigmastr = "%0.2f" % 2.50
Ls = [16, 32, 64, 128, 256]
max_temp = 15
name = 'sigma250'


""" T = np.load(f'data/sigma_{sigmastr}/simulation_binders/L_1024/magnetization/T.npy')[:max_temp]
meanbinders = np.load(f'data/sigma_{sigmastr}/simulation_binders/meanbinders_new.npy')[:,:max_temp]
errbinders = np.load(f'data/sigma_{sigmastr}/simulation_binders/errbinders_new.npy')[:,:max_temp]
 """

T = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_16/magnetization/T.npy')[:max_temp]
meanbinders = np.load(f'data/sigma_{sigmastr}/simulation_{name}/meanbinders_new.npy')[:,:max_temp]
errbinders = np.load(f'data/sigma_{sigmastr}/simulation_{name}/errbinders_new.npy')[:,:max_temp]
#errbinders = np.ones((5,28))*10**(-12)



def plot_various_T(T,Ls,binders,sigma,err,x_label, y_label): 
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
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        #plt.legend()
        # Add a colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=T.min(), vmax=T.max()))
    sm.set_array([])
    # cbar = plt.colorbar(sm)
    # cbar.ax.set_ylabel('$T$')
    

errplot = errbinders/(meanbinders**2-meanbinders)


plot_various_T(T,Ls,np.log10(1/meanbinders-1),2.50,errplot, 'Log(L)', r'$\log(1/U_2-1)$')

binderL = np.log10(1/meanbinders[:-1] - 1)
binder2L = np.log10(1/meanbinders[1:] - 1)
derivative = binder2L - binderL

errL = errplot[:-1]
err2L = errplot[1:]
errderivative = err2L + errL

#errderivative = np.ones((4,28))*10**(-12)


plot_various_T(T,Ls[:-1],derivative,2.50,errderivative,'Log(L)', r'$d_L (\log(1/U_2-1)$)')

plt.show() 

