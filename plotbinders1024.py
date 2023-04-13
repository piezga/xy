#plotta e salva i binder

import numpy as np
import matplotlib.pyplot as plt
import os

sigmastr = "%0.2f" % 1.80

plt.rcParams['figure.dpi'] = 150

Ls = [16,32,64,128,256,512]

indices = [2,3,23,25]

T = np.load(f'data/sigma_{sigmastr}/simulation_low/L_16/magnetization/T.npy', allow_pickle=True) #stesse T
T = [T[i] for i in indices]
T = np.array([T])
T = np.resize(T,[4,])

binderslow = np.load(f'data/sigma_{sigmastr}/simulation_low/meanbinders.npy')

binders = np.empty([len(Ls),len(T)])
for i, index in enumerate(indices):
    binders[:,i] = binderslow[:,index]

binders1024 = np.load(f'data/sigma_{sigmastr}/simulation_new/meanbinders.npy')

meanbinders = np.empty([7,len(T)])

for i in range(len(Ls)):
    meanbinders[i,:] = binders[i,:]

meanbinders[6,:] = binders1024

np.save(f'data/sigma_{sigmastr}/simulation_new/binders1024.npy',meanbinders, allow_pickle=True)
np.save(f'data/sigma_{sigmastr}/simulation_new/T1024.npy',T, allow_pickle=True)



Ls = [16,32,64,128,256,512,1024]



        
# for i, L in enumerate(Ls):
    
#     for j,test in enumerate(tests):
#         binder = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_{L}/test_{test}/binder.npy')
#         plt.figure(j+1)
#         plt.plot(T,binder, label= 'L' +str(L) +' test'+ str(test),marker='.')
#         plt.legend()
#         binderplotpath = f'data/sigma_{sigmastr}/simulation_{name}/plots/binders/'
#         if not os.path.isdir(binderplotpath):
#             os.makedirs(binderplotpath)
#         if not os.path.isdir(binderplotpath + f'L_{L}'):
#             os.makedirs(binderplotpath + f'L_{L}')
#         plt.savefig(binderplotpath + f'L_{L}/L_{L}_test{test}.png')
        
        
        

    
# meanbinders = np.load(f'data/sigma_{sigmastr}/simulation_{name}/meanbinders.npy')
# binders1024 = np.load(f'data/sigma_{sigmastr}/simulation_new/meanbinders.npy')
# errbinders = np.load(f'data/sigma_{sigmastr}/simulation_{name}/errbinders.npy')

# binderplotpath = f'data/sigma_{sigmastr}/simulation_{name}/plots/binders/'
# if not os.path.isdir(binderplotpath):
#     os.makedirs(binderplotpath)


# plt.figure()
# for i,L in enumerate(Ls):
#     plt.errorbar(T,meanbinders[i],errbinders[i], label=str(L),marker = '.')
#     #plt.plot(meanbinders)
#     plt.legend()

# plt.savefig(binderplotpath + 'meanbinders.png')

# plt.show()


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

