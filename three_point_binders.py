import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 150

sigmastr = "%0.2f" % 1.80
Ls = [16, 32, 64, 128, 256, 512, 1024]
T = np.load(f'data/sigma_{sigmastr}/simulation_binders/L_1024/magnetization/T.npy')[:8]

meanbinders = np.load(f'data/sigma_{sigmastr}/simulation_binders/meanbinders_new_1.npy')[:,:8]
errbinders = np.load(f'data/sigma_{sigmastr}/simulation_binders/errbinders_new.npy')[:,:8]



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
        plt.legend()
        # Add a colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=T.min(), vmax=T.max()))
    sm.set_array([])
    # cbar = plt.colorbar(sm)
    # cbar.ax.set_ylabel('$T$')
    
    
    
    
#per l'errore in teoria dovrei considerare un peso
#questo e' un errore sui fit che non considera errbinders

def fit_binders_three(T,Ls,meanbinders, errbinders):
    ms = np.ones((len(Ls)-2,len(T)))
    errs = np.ones((len(Ls)-2,len(T)))
    for t in range(len(T)):
        for i in range(len(Ls)-2):
            x = np.log(Ls[i:i+2])
            y = np.log10(1/meanbinders[i:i+2,t] - 1)            
        
            mfit = np.polyfit(x, y, 1, w = 1/errbinders[i:i+2,t])
            ms[i,t] = mfit[0]
            
            delta = 3*np.sum(x**2) - np.sum(x)**2
            resf = np.sum((y - mfit[0]*x - mfit[1])**2)
            err = np.sqrt(resf) * np.sqrt(3/delta)
            errs[i,t] = err
    return ms, errs

ms, errs = fit_binders_three(T, Ls, meanbinders, errbinders)


# errplot = errbinders/(meanbinders**2-meanbinders)


# plot_various_T(T,Ls,np.log10(1/meanbinders-1),1.80,errplot, 'Log(L)', r'$\log(1/U_2-1)$')


# binderL = np.log10(1/meanbinders[:-1] - 1)
# binder2L = np.log10(1/meanbinders[1:] - 1)
# derivative = binder2L - binderL

# # errL = errplot[:-1]
# # err2L = errplot[1:]
# # errderivative = err2L + errL

# # #errderivative = np.ones((6,10))*10**(-12)


# # plot_various_T(T,Ls[:-1],derivative,1.80,errderivative,'Log(L)', r'$d_L (\log(1/U_2-1)$)')


plot_various_T(T,Ls[:-2],ms,1.80, errs, 'Log(L)', r'Slope (3 point fit)')

plt.show() 

