import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 150

sigmastr = "%0.2f" % 1.80
Ls = [16, 32, 64, 128, 256, 512, 1024]

T = [0.001, 0.002815, 0.00463, 0.042741, 0.04637037]
T_low = np.array(T)
Triccardo = np.load(f'data/sigma_{sigmastr}/simulation_riccardo/T.npy')
#LOW

binders256_low = np.load(f'data/sigma_{sigmastr}/simulation_riccardo/meanbinders_new.npy')
binders512_low = np.load(f'data/sigma_{sigmastr}/simulation_low_512_analyzed/meanbinders_new.npy')
Triccardo512low = np.load(f'data/sigma_{sigmastr}/simulation_low_512_analyzed/T.npy')

binders1024_001 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT0001_1/meanbinders_new.npy')) #ex new2
binders1024_003 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT003_total/meanbinders_new.npy'))
binders1024_005 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT005_1/meanbinders_new.npy'))
binders1024_042 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT042_total/meanbinders_new.npy'))
binders1024_05 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT05_1/meanbinders_new.npy'))

binders1024 = [binders1024_001, binders1024_003, binders1024_005, binders1024_042, binders1024_05]
binders1024 = np.array(binders1024)
binders1024_low = np.resize(binders1024, [1,5])

meanbinders = np.empty([len(Ls),len(T)])
meanbinders[:5,:] = binders256_low
meanbinders[5,:] = binders512_low
meanbinders[6,:] = binders1024_low

meanbinders_low = meanbinders


errbinders256_low = np.load(f'data/sigma_{sigmastr}/simulation_riccardo/errbinders_new.npy')
errbinders512_low = np.load(f'data/sigma_{sigmastr}/simulation_low_512_analyzed/errbinders_new.npy')

errbinders1024_001 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT0001_1/errbinders_new.npy'))
errbinders1024_003 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT003_1/errbinders_new.npy'))
errbinders1024_005 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT005_1/errbinders_new.npy'))
errbinders1024_042 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT042_total/errbinders_new.npy'))
errbinders1024_05 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT05_1/errbinders_new.npy'))

errbinders1024 = [errbinders1024_001, errbinders1024_003, errbinders1024_005, errbinders1024_042, errbinders1024_05]
errbinders1024 = np.array(errbinders1024)
errbinders1024_low = np.resize(errbinders1024, [1,5])

errbinders = np.empty([len(Ls),len(T)])
errbinders[:5,:] = errbinders256_low
errbinders[5,:] = errbinders512_low
errbinders[6,:] = errbinders1024_low

errbinders_low = errbinders






Triccardo512medium = np.load(f'data/sigma_{sigmastr}/simulation_medium_512_analyzed/T.npy')




T = [0.17148148, 0.25222222, 0.33296296, 0.93851852, 1.05962963]
T_high = np.array(T)


######################################################################
binders256_high = np.load(f'data/sigma_{sigmastr}/simulation_real/meanbinders_new.npy')  #controlla

indices = [4,6,8,23,26]

meanbinders = np.empty([len(Ls),len(T)])
for i, index in enumerate(indices):
    meanbinders[:5,i] = binders256_high[:,index]


######################################################################


binders512_high = np.load(f'data/sigma_{sigmastr}/simulation_high_512_analyzed/meanbinders_new.npy')        #controlla
Triccardo512high = np.load(f'data/sigma_{sigmastr}/simulation_high_512_analyzed/T.npy')



binders1024_017 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT017_1/meanbinders_new.npy'))
binders1024_025 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT025_1/meanbinders_new.npy'))
binders1024_033 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT033_1/meanbinders_new.npy'))
binders1024_093 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT093_1/meanbinders_new.npy'))
binders1024_105 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT105_1/meanbinders_new.npy'))
binders1024_high = [binders1024_017, binders1024_025, binders1024_033, binders1024_093, binders1024_105]
binders1024_high = np.array(binders1024_high)


meanbinders[5,:] = binders512_high
meanbinders[6,:] = binders1024_high

meanbinders_high = meanbinders

errbinders256_high = np.load(f'data/sigma_{sigmastr}/simulation_real/errbinders_new.npy')           #controlla

indices = [4,6,8,23,26]

errbinders = np.empty([len(Ls),len(T)])
for i, index in enumerate(indices):
    errbinders[:5,i] = errbinders256_high[:,index]


errbinders512_high = np.load(f'data/sigma_{sigmastr}/simulation_high_512_analyzed/errbinders_new.npy')

errbinders1024_017 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT017_1/errbinders_new.npy'))
errbinders1024_025 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT025_1/errbinders_new.npy'))
errbinders1024_033 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT033_1/errbinders_new.npy'))
errbinders1024_093 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT093_1/errbinders_new.npy'))
errbinders1024_105 = float(np.load(f'data/sigma_{sigmastr}/simulation_simT105_1/errbinders_new.npy'))
errbinders1024_high = [errbinders1024_017, errbinders1024_025, errbinders1024_033, errbinders1024_093, errbinders1024_105]
errbinders1024_high = np.array(errbinders1024_high)



errbinders[5,:] = errbinders512_high
errbinders[6,:] = errbinders1024_high

errbinders_high = errbinders





meanbinders = np.concatenate((meanbinders_low,meanbinders_high),axis=1)#[:,:-2]
errbinders = np.concatenate((errbinders_low,errbinders_high),axis=1)#[:,:-2]
T = np.concatenate((T_low,T_high))#[:-2]
np.save(f'data/sigma_{sigmastr}/simulation_binders/meanbinders_new_1.npy', meanbinders, allow_pickle=True)
np.save(f'data/sigma_{sigmastr}/simulation_binders/errbinders_new.npy', errbinders, allow_pickle=True)
np.save(f'data/sigma_{sigmastr}/simulation_binders/L_1024/magnetization/T.npy',T, allow_pickle=True)

#errbinders = np.ones((7,10))*10**(-12)





""" 
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
    

errplot = errbinders/(meanbinders**2-meanbinders)


plot_various_T(T,Ls,np.log10(1/meanbinders-1),1.80,errplot, 'Log(L)', r'$\log(1/U_2-1)$')

binderL = np.log10(1/meanbinders[:-1] - 1)
binder2L = np.log10(1/meanbinders[1:] - 1)
derivative = binder2L - binderL

errL = errplot[:-1]
err2L = errplot[1:]
errderivative = err2L + errL

#errderivative = np.ones((6,10))*10**(-12)


plot_various_T(T,Ls[:-1],derivative,1.80,errderivative,'Log(L)', r'$d_L (\log(1/U_2-1)$)')

plt.show() """