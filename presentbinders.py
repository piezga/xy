import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 150


sigmavalue = 1.20
sigmastr = "%0.2f_infIMG" % sigmavalue
Ls = [16, 32, 64, 128, 256]
min_temp = 0
max_temp = 4
name = 'binders'


""" T = np.load(f'data/sigma_{sigmastr}/simulation_binders/L_1024/magnetization/T.npy')[:max_temp]
meanbinders = np.load(f'data/sigma_{sigmastr}/simulation_binders/meanbinders_new.npy')[:,:max_temp]
errbinders = np.load(f'data/sigma_{sigmastr}/simulation_binders/errbinders_new.npy')[:,:max_temp]
 """

totaltemp = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_16/magnetization/T.npy')#[min_temp:max_temp]
T = totaltemp[min_temp:max_temp]
meanbinders = np.load(f'data/sigma_{sigmastr}/simulation_{name}/meanbinders_new.npy')[:,min_temp:max_temp]
errbinders = np.load(f'data/sigma_{sigmastr}/simulation_{name}/errbinders_new.npy')[:,min_temp:max_temp]
#errbinders = np.ones((len(L),maxtemp))*10**(-12)


#print(len(T))
print(T)


def plot_various_T(T,Ls,binders,sigma,err,x_label, y_label): 
    cmap = plt.cm.rainbow
    fig,ax = plt.subplots()
    fig.suptitle(r'$\sigma = $' + str(sigma))
    for i,t in enumerate(T):
        ax.errorbar(np.log2(Ls), binders[:,i],
                abs(err[:,i]),               
                color=cmap(i/len(totaltemp)),
                label='T ' + str(t),
                linestyle = '--', marker='.')
        # plt.xscale('log')
        # plt.yscale('log')
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend(loc='upper left')
        # Add a colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=T.min(), vmax=T.max()))
    sm.set_array([])
    # cbar = plt.colorbar(sm)
    # cbar.ax.set_ylabel('$T$')
    

errplot = errbinders/(meanbinders**2-meanbinders)


plot_various_T(T,Ls,np.log10(1/meanbinders-1),sigmavalue,errplot, r'$log_2(L)$', r'$\log_{10}(1/B-1)$')

binderL = np.log10(1/meanbinders[:-1] - 1)
binder2L = np.log10(1/meanbinders[1:] - 1)
derivative = binder2L - binderL

errL = errplot[:-1]
err2L = errplot[1:]
errderivative = err2L + errL

#errderivative = np.ones((4,28))*10**(-12)


plot_various_T(T,Ls[:-1],derivative/np.log10(2),sigmavalue,errderivative/np.log10(2),r'$log_2(L)$', 'Derivative')

plt.show() 

