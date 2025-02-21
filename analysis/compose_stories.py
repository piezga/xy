from variables import *
import numpy as np
import os

original_dir = os.getcwd()

for T in temperatures:

    print(f'Calculating T: {T}')

    path = data_path+'simulation_'+ T 


    for L in sizes:
        
        L_path = path + '/L_' + str(L) + '/'
        quantities_L_path = quantities_path + 'L_' + str(L) + '/'

        if not os.path.isdir(quantities_L_path):
            os.mkdir(quantities_L_path)

        magnetization_path = L_path + 'magnetization' + '/'
        print('Path is ' + os.getcwd())

        composed_mx = []
        composed_my = []
        composed_mx_k_re = []
        composed_my_k_re = []
        composed_mx_k_im = []
        composed_my_k_im = []
        

        for test in range(tests):

            print(f'Processing test {test}')

            composed_mx.append(np.load(magnetization_path + f'mx_test_{test}.npy',allow_pickle = True))
            composed_my.append(np.load(magnetization_path + f'my_test_{test}.npy',allow_pickle = True))
            composed_mx_k_re.append(np.load(magnetization_path + f'mx_re_test_{test}.npy',allow_pickle = True))
            composed_my_k_re.append(np.load(magnetization_path + f'my_re_test_{test}.npy',allow_pickle = True))
            composed_mx_k_im.append(np.load(magnetization_path + f'mx_im_test_{test}.npy',allow_pickle = True))
            composed_my_k_im.append(np.load(magnetization_path + f'my_im_test_{test}.npy',allow_pickle = True))

        
        np.save(quantities_L_path + 'composed_mx.npy', composed_mx)
        np.save(quantities_L_path + 'composed_my.npy', composed_my)
        np.save(quantities_L_path + 'composed_mx_k_re.npy', composed_mx_k_re)
        np.save(quantities_L_path + 'composed_my_k_re.npy', composed_my_k_re)
        np.save(quantities_L_path + 'composed_mx_k_im.npy', composed_mx_k_im)
        np.save(quantities_L_path + 'composed_my_k_im.npy', composed_my_k_im)

        print(f'Megastories saved to {quantities_L_path}') 









            