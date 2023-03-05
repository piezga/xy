#plotta tutte le lastconfig

import numpy as np
import matplotlib.pyplot as plt
import os


plt.rcParams['figure.dpi'] = 150

Ls = [16,32,64,128,256]
testnum = 6  #per ora hardcoded
sigmastr = "%0.2f" % 2.10
sigmafloat = float(sigmastr)
sigmaname = int(sigmafloat*100)
mypath = 'data/sigma_{sigmastr}/simulation_sigma{sigmaname}/plots/'   #creo cartella plots
if not os.path.isdir(mypath):
    os.makedirs(mypath)
    
    
for L in Ls:
    
    Lpath = f'data/sigma_{sigmastr}/simulation_sigma{sigmaname}/plots/L_{L}/' 
    if not os.path.isdir(Lpath):
        os.makedirs(Lpath)
    
    
    for test in np.arange(testnum):
        files = os.listdir(f'data/sigma_{sigmastr}/simulation_sigma{sigmaname}/L_{L}/test_{test}/last_configuration/')
        
        testpath = f'data/sigma_{sigmastr}/simulation_sigma{sigmaname}/plots/L_{L}/test_{test}/' 
        if not os.path.isdir(testpath):
            os.makedirs(testpath)
        
        
        for file in files:
            
        
            config = np.fromfile(f'data/sigma_{sigmastr}/simulation_sigma{sigmaname}/L_{L}/test_{test}/last_configuration/{file}', dtype = 'float64').reshape((L,L))
            
            
            #plt.figure(1)
            #plt.plot(mx[3])
            fig, ax = plt.subplots(1)
            ax.set_title(file)
            scale = 200
            
            # Create a grid of x and y values    
            x, y = np.meshgrid(np.arange(config.shape[1]), np.arange(config.shape[0]))    
            # Print the shapes of the input arrays      # Define a color map    
            cmap = plt.get_cmap('twilight')   
            #colors = cyclic_colors(config+np.pi)   
            colors = config
            # Plot black arrows with the config    
            ax.quiver(x, y, np.cos(config), np.sin(config), color='black',scale=scale, width = 10**-3, headwidth = 2.5, headaxislength = 2, headlength = 2)    
            fig.colorbar(ax.pcolormesh(x, y, colors, cmap=cmap, alpha=0.3, shading='auto'), ax = ax)
            plt.savefig(testpath + 'T_' + file[2:10] + '.png')
            plt.close()