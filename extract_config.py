import shutil
import numpy as np
import os

sigmastr = "%0.2f" % 1.80
L = 1024
tests = np.arange(100)
T = "%0.6f" % 0.252222
name1 = 'real_1'
name2 = 'T025_1_c'

for i in tests:
    path1 = f'data/sigma_{sigmastr}/simulation_{name1}/L_{L}/test_{i}/last_configuration/T_{T}.bin'
    path2 = f'data/sigma_{sigmastr}/simulation_{name2}/L_{L}/test_{i}/last_configuration'
    if not os.path.isdir(path2):
        os.makedirs(path2)
    shutil.copy(path1, path2)
    print('Extracted config # ' + str(i))
