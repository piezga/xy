import numpy as np

sigmastr = "%0.2f" % 1.80
sigmafloat = float(sigmastr)
tests = np.arange(100)
name = '049_085'

temps =  [0.696296]
    
path = f'data/sigma_{sigmastr}/simulation_{name}/L_1024/'

for test in tests:
    f = open(path+f'Ts_test_{test}.txt', 'w')
    for temp in temps:
        f.write(str(temp) + '\n')
    f.close()
    

        
    
