import numpy as np

sigmastr = "%0.2f" % 1.80
sigmafloat = float(sigmastr)
tests = np.arange(100)
name = 'new'


path = f'\data\sigma_{sigmastr}\simulation_{name}\L_1024\magnetization'

for test in tests:
    mx1 = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_1024/magnetization/bismx_test_{test}.npy', allow_pickle=True)
    mx2 = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_1024/magnetization/mx_test_{test}.npy', allow_pickle=True)
    mag = np.append(mx1,mx2, axis=0)
    np.save(f'data/sigma_{sigmastr}/simulation_{name}/L_1024/magnetization/amx_test_{test}.npy',mag, allow_pickle=True)