from variables import *
import numpy as np
import os

for T in temperatures:
    print(f'Calculating T: {T}')

    path = os.path.join(data_path, f'simulation_{T}')

    for L in sizes:
        L_path = os.path.join(path, f'L_{L}')
        composed_path = os.path.join(L_path, 'composed_quantities')

        if not os.path.isdir(composed_path):
            os.makedirs(composed_path, exist_ok=True)

        magnetization_path = os.path.join(L_path, 'magnetization')

        # Initialize lists to store arrays
        composed_mx = []
        composed_my = []
        composed_mx_k_re = []
        composed_my_k_re = []
        composed_mx_k_im = []
        composed_my_k_im = []

        for test in range(tests):
            print(f'Processing test {test}')

            # Load arrays
            mx = np.load(os.path.join(magnetization_path, f'mx_test_{test}.npy'), allow_pickle=True)
            my = np.load(os.path.join(magnetization_path, f'my_test_{test}.npy'), allow_pickle=True)
            mx_re = np.load(os.path.join(magnetization_path, f'mx_re_test_{test}.npy'), allow_pickle=True)
            my_re = np.load(os.path.join(magnetization_path, f'my_re_test_{test}.npy'), allow_pickle=True)
            mx_im = np.load(os.path.join(magnetization_path, f'mx_im_test_{test}.npy'), allow_pickle=True)
            my_im = np.load(os.path.join(magnetization_path, f'my_im_test_{test}.npy'), allow_pickle=True)

            # Append arrays to lists
            composed_mx.append(mx)
            composed_my.append(my)
            composed_mx_k_re.append(mx_re)
            composed_my_k_re.append(my_re)
            composed_mx_k_im.append(mx_im)
            composed_my_k_im.append(my_im)

        # Concatenate arrays along a new axis (axis=0 by default)
        composed_mx = np.concatenate(composed_mx, axis=1)
        composed_my = np.concatenate(composed_my, axis=1)
        composed_mx_k_re = np.concatenate(composed_mx_k_re, axis=1)
        composed_my_k_re = np.concatenate(composed_my_k_re, axis=1)
        composed_mx_k_im = np.concatenate(composed_mx_k_im, axis=1)
        composed_my_k_im = np.concatenate(composed_my_k_im, axis=1)

        # Save concatenated arrays
        np.save(os.path.join(composed_path, 'composed_mx.npy'), composed_mx)
        np.save(os.path.join(composed_path, 'composed_my.npy'), composed_my)
        np.save(os.path.join(composed_path, 'composed_mx_k_re.npy'), composed_mx_k_re)
        np.save(os.path.join(composed_path, 'composed_my_k_re.npy'), composed_my_k_re)
        np.save(os.path.join(composed_path, 'composed_mx_k_im.npy'), composed_mx_k_im)
        np.save(os.path.join(composed_path, 'composed_my_k_im.npy'), composed_my_k_im)

        print(f'Megastories saved to {composed_path}')