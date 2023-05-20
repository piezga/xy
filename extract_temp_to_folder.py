import numpy as np
import os
import shutil


sigmastr = "%0.2f" % 1.80
L = 1024
tests = np.arange(100)
name_initial = 'simT0001T005_1'
name_final = 'simT05_1'
temp = "%0.6f" % 0.046370 
path_temp = f'data/sigma_{sigmastr}/simulation_{name_final}/L_{L}/'
path_Ls = f'data/sigma_{sigmastr}/simulation_{name_final}/'




for test in tests:

    print('Elaborating test #' + str(test))
    path_final = f'data/sigma_{sigmastr}/simulation_{name_final}/L_{L}/test_{test}'
    if not os.path.isdir(path_final):
            os.makedirs(path_final)
            print('Created directory ' + path_final)
    else:
            print('Directory ' + path_final + ' already exists')
    bin_file = f'data/sigma_{sigmastr}/simulation_{name_initial}/L_{L}/test_{test}/T_{temp}_mx.bin'
    shutil.copy(bin_file, path_final)
    bin_file = f'data/sigma_{sigmastr}/simulation_{name_initial}/L_{L}/test_{test}/T_{temp}_my.bin'
    shutil.copy(bin_file, path_final)
        
    f = open(path_temp+f'Ts_test_{test}.txt', 'w')
    f.write(str(temp))
    f.close()
    print('Created temperature file')
    f = open(path_Ls +f'Ls_test_{test}.txt', 'w' )
    f.write(str(L))
    f.close()
    print('Created Ls file')
    print('================================')

"""         
        CAVEAT

I nomi delle cartelle devono essere simulation_{nome}_{numero}
dove numero va da 1 in poi, perche' 0 e' la run di termalizzazione



"""