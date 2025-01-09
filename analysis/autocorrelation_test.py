from variables import *
import numpy as np
import matplotlib.pyplot as plt
from functions import autocorrelation_time

L = 32


for test in range(tests):

    mx = np.load(path + f'/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)[:50000]
    my = np.load(path + f'/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)[:50000]
            
    mx_re = np.load(path + f'/L_{L}/magnetization/mx_re_test_{test}.npy', allow_pickle=True)
    my_re = np.load(path + f'/L_{L}/magnetization/my_re_test_{test}.npy', allow_pickle=True)

            
    mx_im = np.load(path + f'/L_{L}/magnetization/mx_im_test_{test}.npy', allow_pickle=True)
    my_im = np.load(path + f'/L_{L}/magnetization/my_im_test_{test}.npy', allow_pickle=True)
    
    m2 = mx**2 + my**2
    m_k_2 = mx_re**2 + my_re**2 + mx_im**2 + my_im**2
    
    tau_int_m2, autocorr_m2 = autocorrelation_time(m2)
    #tau_int_m_k_2, autocorr_m_k_2 = autocorrelation_time(m_k_2)

    print(f'Tau for m2 in test {test} is {tau_int_m2}' )
    #print(f'Tau for m_k_2 in test {test} is {tau_int_m_k_2}')
    plt.figure()
    plt.plot(autocorr_m2)
    plt.show()