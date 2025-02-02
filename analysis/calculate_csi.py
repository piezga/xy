from variables import *
import numpy as np
import os

#create a matrix where the rows are the temperatures
#and the columns the sizes

temperatures = simulations
sizes = Ls

correlation_lengths = np.empty([len(temperatures), len(sizes)])

d_correlation_lengths = np.empty([len(temperatures), len(sizes)])


m2s = np.empty([len(temperatures), len(sizes)])

m_k_2s = np.empty([len(temperatures), len(sizes)])



for t, temp in enumerate(temperatures):
    print('Calculating T: ' + str(temp))
    for l, L in enumerate(sizes):

        path = data_path+'simulation_'+ temp
        L_path = path + '/L_' + str(L) + '/'
        prefactor = 1 / (2 * np.sin(np.pi / L))
        print(prefactor)
        m2_over_tests = np.empty(tests)  # Reset each time
        m_k_2_over_tests = np.empty(tests)

        for test in range(tests):

            print('Path is ' + path)


            mx = np.load(L_path + f"magnetization/mx_test_{test}.npy", allow_pickle=True)
            my = np.load(L_path + f"magnetization/my_test_{test}.npy", allow_pickle=True)

            mx_re = np.load(L_path + f"magnetization/mx_re_test_{test}.npy", allow_pickle=True)
            my_re = np.load(L_path + f"magnetization/my_re_test_{test}.npy", allow_pickle=True)

            mx_im = np.load(L_path + f"magnetization/mx_im_test_{test}.npy", allow_pickle=True)
            my_im = np.load(L_path + f"magnetization/my_im_test_{test}.npy", allow_pickle=True)

            m2 = mx**2 + my**2
            m_k_2 = mx_re**2 + my_re**2 + mx_im**2 + my_im**2

            m2_over_tests[test] = np.mean(m2)
            m_k_2_over_tests[test] = np.mean(m_k_2)

            print(f"T={temp}, L={L}, Test={test}, m2={np.mean(m2)}, m_k_2={np.mean(m_k_2)}")

        m2_mean = np.mean(m2_over_tests)
        d_m2_mean = np.std(m2_over_tests)/np.sqrt(tests-1)       

        m_k_2_mean = np.mean(m_k_2_over_tests)
        d_m_k_2_mean = np.std(m_k_2_over_tests)/np.sqrt(tests-1) 
        
        m2s[t,l] = m2_mean
        m_k_2s[t,l] = m_k_2_mean
        
        correlation_lengths[t, l] = prefactor * np.sqrt(m2_mean/m_k_2_mean - 1)
        d_correlation_lengths[t,l] = (abs(prefactor / 2 / m_k_2_mean / np.sqrt(m2_mean / m_k_2_mean - 1))* d_m2_mean 
                                    + abs(prefactor * m2_mean * -1 / 2 / m_k_2_mean ** 2 / np.sqrt(m2_mean / m_k_2_mean - 1)) 
                                    * d_m_k_2_mean)
        print(f"T={temp}, L={L}, Mean Correlation Length={correlation_lengths[t, l]}, Std Dev={d_correlation_lengths[t, l]}")


if not os.path.isdir(quantities_path):
    os.makedirs(quantities_path)

np.save(quantities_path + 'csi.npy',correlation_lengths)
np.save(quantities_path + 'd_csi.npy',d_correlation_lengths)


