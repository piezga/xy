from variables import *
import numpy as np
import matplotlib.pyplot as plt


test = 0
L = 32

mx = np.load(path + f'/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)
my = np.load(path + f'/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)
    
mx_re = np.load(path + f'/L_{L}/magnetization/mx_re_test_{test}.npy', allow_pickle=True)
my_re = np.load(path + f'/L_{L}/magnetization/my_re_test_{test}.npy', allow_pickle=True)

        
mx_im = np.load(path + f'/L_{L}/magnetization/mx_im_test_{test}.npy', allow_pickle=True)
my_im = np.load(path + f'/L_{L}/magnetization/my_im_test_{test}.npy', allow_pickle=True)

m2 = mx**2 + my**2
m_k_2 = mx_re**2 + my_re**2 + mx_im**2 + my_im**2

