from variables import *
import numpy as np
import os
from functions import covariance, csi_error
#create a matrix where the rows are the temperatures
#and the columns the sizes



correlation_lengths = np.empty([len(temperatures), len(sizes)])

d_correlation_lengths = np.empty([len(temperatures), len(sizes)])


m2s = np.empty([len(temperatures), len(sizes)])

m_k_2s = np.empty([len(temperatures), len(sizes)])



for t, temp in enumerate(temperatures):
    print('Calculating T: ' + str(temp))
    path = data_path+'simulation_'+ temp
    
    for l, L in enumerate(sizes):

        L_path = path + '/L_' + str(L) + '/'
        prefactor = 1 / (2 * np.sin(np.pi / L))

        m2_over_tests = np.empty(tests)  # Reset each time
        m_k_2_over_tests = np.empty(tests)

        m_over_tests = np.empty(tests)  # Reset each time
        m_k_over_tests = np.empty(tests)




        for test in range(tests):

            print('Path is ' + L_path)


            mx = np.load(L_path + f"magnetization/mx_test_{test}.npy", allow_pickle=True)
            my = np.load(L_path + f"magnetization/my_test_{test}.npy", allow_pickle=True)

            mx_re = np.load(L_path + f"magnetization/mx_re_test_{test}.npy", allow_pickle=True)
            my_re = np.load(L_path + f"magnetization/my_re_test_{test}.npy", allow_pickle=True)

            mx_im = np.load(L_path + f"magnetization/mx_im_test_{test}.npy", allow_pickle=True)
            my_im = np.load(L_path + f"magnetization/my_im_test_{test}.npy", allow_pickle=True)

            m2 = mx**2 + my**2
            m2 = m2.astype(float)
            m_k_2 = mx_re**2 + my_re**2 + mx_im**2 + my_im**2
            m_k_2 = m_k_2.astype(float)

            m = np.sqrt(m2)
            m_k = np.sqrt(m_k_2)



            m2_over_tests[test] = np.mean(m2)
            m_k_2_over_tests[test] = np.mean(m_k_2)

            m_over_tests[test] = np.mean(m)
            m_k_over_tests[test] = np.mean(m_k)


            print(f"T={temp}, L={L}, Test={test}, m2={np.mean(m2)}, m_k_2={np.mean(m_k_2)}")
     
        #sbagliato dividere per np.sqrt
        m2_mean = np.mean(m2_over_tests)
        d_m2_mean = np.std(m2_over_tests)/np.sqrt(tests-1)       

        m_k_2_mean = np.mean(m_k_2_over_tests)
        d_m_k_2_mean = np.std(m_k_2_over_tests)/np.sqrt(tests-1) 
 
        m_mean = np.mean(m_over_tests)
        d_m_mean = np.std(m_over_tests)/np.sqrt(tests-1)       

        m_k_mean = np.mean(m_k_over_tests)
        d_m_k_mean = np.std(m_k_over_tests)/np.sqrt(tests-1) 
        
        m2s[t,l] = m2_mean
        m_k_2s[t,l] = m_k_2_mean

        covariance_matrix = np.cov(m2_over_tests,m_k_2_over_tests)/(tests-1)
        cov = covariance_matrix[0,1]
        d_m2_mean = covariance_matrix[0,0]
        d_m_k_2_mean = covariance_matrix[1,1] 


        correlation_lengths[t, l] = prefactor * np.sqrt(m2_mean/m_k_2_mean - 1)
        d_correlation_lengths[t,l] = prefactor * csi_error(m_mean, d_m2_mean, m_k_mean, d_m_k_2_mean, cov)
        print(f"T={temp}, L={L}, Mean Correlation Length={correlation_lengths[t, l]}, Std Dev={d_correlation_lengths[t, l]}")
        print(f"Covariance = {cov}")

if not os.path.isdir(quantities_path):
    os.makedirs(quantities_path)

np.save(quantities_path + 'csi.npy',correlation_lengths)
np.save(quantities_path + 'd_csi.npy',d_correlation_lengths)




#Create path and save


if not os.path.isdir(quantities_path):
    os.makedirs(quantities_path)
    
np.save(quantities_path + 'csi',correlation_lengths)
np.save(quantities_path + 'd_csi',d_correlation_lengths)