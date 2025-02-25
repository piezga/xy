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
        quantities_L_path = quantities_path + 'L_' + str(L) + '/'
        composed_path = L_path + 'composed_quantities' + '/'
        
        prefactor = 1 / (2 * np.sin(np.pi / L))



        print('Path is ' + os.getcwd())


        mx = np.load(composed_path + 'composed_mx.npy', allow_pickle=True)
        my = np.load(composed_path + 'composed_my.npy', allow_pickle=True)

        mx_re = np.load(composed_path + 'composed_mx_k_re.npy', allow_pickle=True)
        my_re = np.load(composed_path + 'composed_my_k_re.npy', allow_pickle=True)

        mx_im = np.load(composed_path + 'composed_mx_k_im.npy', allow_pickle=True)
        my_im = np.load(composed_path + 'composed_my_k_im.npy', allow_pickle=True)

        m2 = mx**2 + my**2
        m_k_2 = mx_re**2 + my_re**2 + mx_im**2 + my_im**2

        m2 = m2.astype(float)
        m_k_2 = m_k_2.astype(float)

        m = np.sqrt(m2)
        m_k = np.sqrt(m_k_2)


        m2_mean = np.mean(m2)
        m_k_2_mean = np.mean(m_k_2)

        m_mean = np.mean(m)
        m_k_mean = np.mean(m_k)


        print(f"T={temp}, L={L}, m2={m2_mean}, m_k_2={m_k_2_mean}")
    
        d_m2_mean = np.std(m2)       
        d_m_k_2_mean = np.std(m_k_2) 
 
        d_m_mean = np.std(m)       
        d_m_k_mean = np.std(m_k) 
        

        print(f"T={temp}, L={L}, d_m2={d_m2_mean}, d_m_k_2={d_m_k_2_mean}")

        m2s[t,l] = m2_mean
        m_k_2s[t,l] = m_k_2_mean

        cov = np.cov(m,m_k)[0,1]
        


        correlation_lengths[t, l] = prefactor * np.sqrt(m2_mean/m_k_2_mean - 1)
        d_correlation_lengths[t,l] = prefactor * csi_error(m_mean, d_m_mean, m_k_mean, d_m_k_mean, cov)
        print(f"T={temp}, L={L}, Mean Correlation Length={correlation_lengths[t, l]}, Std Dev={d_correlation_lengths[t, l]}")
        print(f"Covariance = {cov}")



#Create path and save


if not os.path.isdir(quantities_path):
    os.makedirs(quantities_path)
    
np.save(quantities_path + 'csi_from_megastories.npy',correlation_lengths)
np.save(quantities_path + 'd_csi_from_megastories.npy',d_correlation_lengths)