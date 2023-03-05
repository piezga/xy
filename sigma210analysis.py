#test0

import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['figure.dpi'] = 150


Ls = [16,32,128,256]
test = 2

fig, ax = plt.subplots(4)
mxs = []
for i,L in enumerate(Ls):    
    temps = np.load(f'data/sigma_2.10/simulation_sigma210/L_{L}/magnetization/T.npy', allow_pickle=True)
    mx = np.load(f'data/sigma_2.10/simulation_sigma210/L_{L}/magnetization/mx_test_{test}.npy', allow_pickle=True)[:,50000:]
    my = np.load(f'data/sigma_2.10/simulation_sigma210/L_{L}/magnetization/my_test_{test}.npy', allow_pickle=True)[:,50000:]
    T = np.load(f'data/sigma_2.10/simulation_sigma210/L_{L}/magnetization/T.npy', allow_pickle=True)
    
    
    files = os.listdir(f'data/sigma_2.10/simulation_sigma210/L_{L}/test_{test}/last_configuration/')
    
    # for file in files[:-10]:
        
    
    #     config = np.fromfile(f'data/sigma_2.10/simulation_sigma210/L_{L}/test_{test}/last_configuration/{file}', dtype = 'float64').reshape((L,L))
        
        
    #     #plt.figure(1)
    #     #plt.plot(mx[3])
    #     fig, ax = plt.subplots(1)
    #     ax.set_title(file)
    #     scale = 200
        
    #     # Create a grid of x and y values    
    #     x, y = np.meshgrid(np.arange(config.shape[1]), np.arange(config.shape[0]))    
    #     # Print the shapes of the input arrays      # Define a color map    
    #     cmap = plt.get_cmap('twilight')   
    #     #colors = cyclic_colors(config+np.pi)   
    #     colors = config
    #     # Plot black arrows with the config    
    #     ax.quiver(x, y, np.cos(config), np.sin(config), color='black',scale=scale, width = 10**-3, headwidth = 2.5, headaxislength = 2, headlength = 2)    
    #     fig.colorbar(ax.pcolormesh(x, y, colors, cmap=cmap, alpha=0.3, shading='auto'), ax = ax)
        
        
    binder = []    
    m = []
    for t in range(len(T)):
        m2 = mx[t]**2 + my[t]**2
        m4 = m2**2 
        binder.append(2 - m4.mean()/m2.mean()**2)
        m.append(m2.mean())
    # plt.figure(1)
    # plt.plot(T,binder,label=str(L))
    # plt.legend()
    plt.figure(2)
    plt.plot(T,m,label=str(L))
    plt.legend()
    plt.figure(3)
    plt.plot(np.abs(mx[4]), label=str(L))
    plt.legend()
    
    
    
    
    
