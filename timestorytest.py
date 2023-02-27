import numpy as np
import matplotlib.pyplot as plt

T = np.load('D:\\xy\\data\\sigma_4.00\\simulation_test\\L_64\\magnetization\\T.npy',
            allow_pickle=True)

mx = np.load('D:\\xy\\data\\sigma_4.00\\simulation_test\\L_64\\magnetization\\mx_test_0.npy',
            allow_pickle=True)

my = np.load('D:\\xy\\data\\sigma_4.00\\simulation_test\\L_64\\magnetization\\my_test_0.npy',
            allow_pickle=True)



T1 = T[0]
T2 = T[27]

mx1 = mx[0,:]
mx2 = mx[27,:]

t = np.arange(0,len(mx1),1)


fig,(ax1,ax2) = plt.subplots(2)
ax1.plot(t,mx1)
ax2.plot(t,mx2)
ax1.grid(True)
ax2.grid(True)
ax1.set(xlabel = 'T = 0,64', ylabel = 'mx')
ax1.set(xlabel = 'T = 0,81', ylabel = 'mx')