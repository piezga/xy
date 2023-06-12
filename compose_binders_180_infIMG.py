import numpy as np



sigmastr = "%0.2f_infIMG" % 4.00
Ls = [16, 32, 64, 128, 256]
T= [0.1, 0.15,0.2, 0.39, 0.42] #, 0.42]
names = ['T01', 'T015', 'T02', 'T039', 'T042'] #, 'T178']

meanbinders = np.ones((len(Ls), len(T))) 
errbinders = np.ones((len(Ls), len(T)))

for i,name in enumerate(names):
    binder = np.load(f'data/sigma_{sigmastr}/simulation_{name}/meanbinders_new.npy')
    meanbinders[:,i] = np.resize(binder,[1,len(Ls)])
    errbinder = np.load(f'data/sigma_{sigmastr}/simulation_{name}/errbinders_new.npy')
    errbinders[:,i] = np.resize(errbinder,[1,len(Ls)])

print(meanbinders)

np.save(f'data/sigma_{sigmastr}/simulation_binders/meanbinders_new.npy', meanbinders, allow_pickle=True)
np.save(f'data/sigma_{sigmastr}/simulation_binders/errbinders_new.npy', errbinders, allow_pickle=True)
np.save(f'data/sigma_{sigmastr}/simulation_binders/L_16/magnetization/T.npy',T, allow_pickle=True)