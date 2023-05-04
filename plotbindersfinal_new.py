import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 150

sigmastr = "%0.2f" % 1.80
Ls = [16, 32, 64, 128, 256, 512, 1024]

T = [0.001, 0.002815, 0.00463, 0.042741, 0.04637037]
T = np.array(T)

binders256_low = np.load(f'data/sigma_{sigmastr}/simulation_riccardo/meanbinders.npy')

# binders512_001 = np.load(f'data/sigma_{sigmastr}/simulation_taglia512/meanbinders_new.npy')
# binders512_001 = np.array(binders512_001)
# indices = [2,3,23,25]
# binders512_others = np.empty([1,len(T)-1])
# binderslow = np.load(f'data/sigma_{sigmastr}/simulation_low/meanbinders_new.npy')
# for i, index in enumerate(indices):
#     binders512_others[0,i] = binderslow[5,index]
binders512_low = np.load(f'data/sigma_{sigmastr}/simulation_low_512_analyzed/meanbinders_new.npy')



binders1024_001 = np.load(f'data/sigma_{sigmastr}/simulation_new2_2/meanbinders_new.npy')[0,0]
binders1024_003 = float(np.load(f'data/sigma_{sigmastr}/simulation_sim003_1/meanbinders_new.npy'))
binders1024_005 = float(np.load(f'data/sigma_{sigmastr}/simulation_sim005_1/meanbinders_new.npy'))
binders1024_042 = float(np.load(f'data/sigma_{sigmastr}/simulation_sim042_1/meanbinders_new.npy'))
binders1024_05 = np.load(f'data/sigma_{sigmastr}/simulation_new2_2/meanbinders_new.npy')[0,1]


binders1024 = [binders1024_001, binders1024_003, binders1024_005, binders1024_042, binders1024_05]
binders1024 = np.array(binders1024)
binders1024_low = np.resize(binders1024, [1,5])

meanbinders = np.empty([len(Ls),len(T)])
meanbinders[:5,:] = binders256_low
meanbinders[5,:] = binders512_low
meanbinders[6,:] = binders1024_low

meanbinders_low = meanbinders

# meanbinders = np.empty([len(Ls),len(T)])
# meanbinders[:5,:] = binders256
# #meanbinders[5,:] = binders512
# meanbinders[5,:] = binders1024
#meanbinders = meanbinders[:,:-1]

errbinders256_low = np.load(f'data/sigma_{sigmastr}/simulation_riccardo/errbinders.npy')
errbinders512_low = np.load(f'data/sigma_{sigmastr}/simulation_low_512_analyzed/errbinders_new.npy')

errbinders1024_001 = np.load(f'data/sigma_{sigmastr}/simulation_new2_2/errbinders_new.npy')[0,0]
errbinders1024_003 = float(np.load(f'data/sigma_{sigmastr}/simulation_sim003_1/errbinders_new.npy'))
errbinders1024_005 = float(np.load(f'data/sigma_{sigmastr}/simulation_sim005_1/errbinders_new.npy'))
errbinders1024_042 = float(np.load(f'data/sigma_{sigmastr}/simulation_sim042_1/errbinders_new.npy'))
errbinders1024_05 = np.load(f'data/sigma_{sigmastr}/simulation_new2_2/errbinders_new.npy')[0,1]


errbinders1024 = [errbinders1024_001, errbinders1024_003, errbinders1024_005, errbinders1024_042, errbinders1024_05]
errbinders1024 = np.array(errbinders1024)
errbinders1024_low = np.resize(errbinders1024, [1,5])

errbinders = np.empty([len(Ls),len(T)])
errbinders[:5,:] = errbinders256_low
errbinders[5,:] = errbinders512_low
errbinders[6,:] = errbinders1024_low

errbinders_low = errbinders





T = [0.17148148, 0.25222222, 0.33296296, 0.93851852, 1.05962963]
T = np.array(T)

binders256_high = np.load(f'data/sigma_{sigmastr}/simulation_real/meanbinders_new.npy')

indices = [4,6,8,23,26]

meanbinders = np.empty([len(Ls),len(T)])
for i, index in enumerate(indices):
    meanbinders[:5,i] = binders256_high[:,index]

######
# binders512_001 = np.load(f'data/sigma_{sigmastr}/simulation_taglia512/meanbinders_new.npy')
# binders512_001 = np.array(binders512_001)
# indices = [2,3,23,25]
# binders512_others = np.empty([1,len(T)-1])
# binderslow = np.load(f'data/sigma_{sigmastr}/simulation_low/meanbinders_new.npy')
# for i, index in enumerate(indices):
#     binders512_others[0,i] = binderslow[5,index]
binders512_high = np.load(f'data/sigma_{sigmastr}/simulation_high_512_analyzed/meanbinders_new.npy')



# binders1024_001 = np.load(f'data/sigma_{sigmastr}/simulation_new2_2/meanbinders_new.npy')[0,0]
# binders1024_003 = float(np.load(f'data/sigma_{sigmastr}/simulation_sim003_1/meanbinders_new.npy'))
# binders1024_00= float(np.load(f'data/sigma_{sigmastr}/simulation_sim005_1/meanbinders_new.npy'))
# binders1024_042 = float(np.load(f'data/sigma_{sigmastr}/simulation_sim042_1/meanbinders_new.npy'))
# binders1024_05 = np.load(f'data/sigma_{sigmastr}/simulation_new2_2/meanbinders_new.npy')[0,1]


# binders1024 = [binders1024_001, binders1024_003, binders1024_005, binders1024_042, binders1024_05]
# binders1024 = np.array(binders1024)
binders1024_high = np.load(f'data/sigma_{sigmastr}/simulation_real_1/meanbinders_new.npy')


#meanbinders[:5,:] = binders256_high
meanbinders[5,:] = binders512_high
meanbinders[6,:] = binders1024_high

meanbinders_high = meanbinders

# meanbinders = np.empty([len(Ls),len(T)])
# meanbinders[:5,:] = binders256
# #meanbinders[5,:] = binders512
# meanbinders[5,:] = binders1024
#meanbinders = meanbinders[:,:-1]

errbinders256_high = np.load(f'data/sigma_{sigmastr}/simulation_real/errbinders_new.npy')

indices = [4,6,8,23,26]

errbinders = np.empty([len(Ls),len(T)])
for i, index in enumerate(indices):
    errbinders[:5,i] = errbinders256_high[:,index]


errbinders512_high = np.load(f'data/sigma_{sigmastr}/simulation_high_512_analyzed/errbinders_new.npy')

# errbinders1024_001 = np.load(f'data/sigma_{sigmastr}/simulation_new2_2/errbinders_new.npy')[0,0]
# errbinders1024_003 = float(np.load(f'data/sigma_{sigmastr}/simulation_sim003_1/errbinders_new.npy'))
# errbinders1024_005 = float(np.load(f'data/sigma_{sigmastr}/simulation_sim005_1/errbinders_new.npy'))
# errbinders1024_042 = float(np.load(f'data/sigma_{sigmastr}/simulation_sim042_1/errbinders_new.npy'))
# errbinders1024_05 = np.load(f'data/sigma_{sigmastr}/simulation_new2_2/errbinders_new.npy')[0,1]


# errbinders1024 = [errbinders1024_001, errbinders1024_003, errbinders1024_005, errbinders1024_042, errbinders1024_05]
# errbinders1024 = np.array(errbinders1024)
errbinders1024_high = np.load(f'data/sigma_{sigmastr}/simulation_real_1/errbinders_new.npy')


#errbinders[:5,:] = errbinders256_low
errbinders[5,:] = errbinders512_high
errbinders[6,:] = errbinders1024_high

errbinders_high = errbinders




T = [0.001, 0.002815, 0.00463, 0.042741, 0.04637037, 0.17148148, 0.25222222, 0.33296296, 0.93851852, 1.05962963]
T = np.array(T)[:8]


meanbinders = np.concatenate((meanbinders_low,meanbinders_high),axis=1)[:8]
errbinders = np.concatenate((errbinders_low,errbinders_high),axis=1)[:8]

np.save(f'data/sigma_{sigmastr}/simulation_binders/meanbinders_new.npy', meanbinders, allow_pickle=True)
np.save(f'data/sigma_{sigmastr}/simulation_binders/errbinders_new.npy', errbinders, allow_pickle=True)
np.save(f'data/sigma_{sigmastr}/simulation_binders/L_1024/magnetization/T.npy',T, allow_pickle=True)

errbinders = np.ones((7,10))*10**(-12)



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

plot_various_T(T,Ls[:-1],derivative,1.80,errderivative,'Log(L)', r'$d_L (\log(1/U_2-1)$)')