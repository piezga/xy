import numpy as np
import os


sigmastr = "%0.2f" % 1.80
L = 1024
tests = np.arange(100)
sims = np.arange(2) + 1
name = 'simT003'
sim_length = 150000 

path_total = f'data/sigma_{sigmastr}/simulation_{name}_total/L_{L}/magnetization'
if not os.path.isdir(path_total):
        os.makedirs(path_total)
        print('Created directory ' + path_total)
else:
        print('Directory ' + path_total + ' already exists')



for test in tests:
        
    print('Elaborating test #' + str(test))
    mx = []
    my = []
        
    for sim in sims:
        mx_temp = np.load(f'data/sigma_{sigmastr}/simulation_{name}_{sim}/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)
        my_temp = np.load(f'data/sigma_{sigmastr}/simulation_{name}_{sim}/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)
        mx = np.append(mx,mx_temp)
        my = np.append(my,my_temp)
        
    
    np.save(path_total + f'/mx_test_{test}',mx)
    np.save(path_total + f'/my_test_{test}',my)
    print('Data shape for mx: ' + str(mx.shape))
    print('Data shape for my: ' + str(my.shape))
    print('============================')
        
                

"""         
        CAVEAT

I nomi delle cartelle devono essere simulation_{nome}_{numero}
dove numero va da 1 in poi, perche' 0 e' la run di termalizzazione



"""