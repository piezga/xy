import numpy as np

sigmastr = "%0.2f" % 1.80
sigmafloat = float(sigmastr)
tests = np.arange(100)
name = 'real_1'

temps =  [0.17148148, 0.25222222, 0.33296296, 0.93851852, 1.05962963]

path = f'data/sigma_{sigmastr}/simulation_{name}/L_1024/'

for test in tests:
    f = open(path+f'Ts_test_{test}.txt', 'w')
    for temp in temps:
        f.write(str(temp) + '\n')
    f.close()
    

        
    
