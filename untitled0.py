import pandas as pd
import numpy as np


sigmavalue = 1.80
sigmastr = "%0.2f_infIMG" % sigmavalue
Ls = [16, 32, 64, 128,256,512]
min_temp = 0
max_temp = 5
name = 'binders'


T = np.load(f'data/sigma_{sigmastr}/simulation_{name}/L_16/magnetization/T.npy')[min_temp:max_temp]
meanbinders = np.load(f'data/sigma_{sigmastr}/simulation_{name}/meanbinders_new.npy')[:,min_temp:max_temp]
errbinders = np.load(f'data/sigma_{sigmastr}/simulation_{name}/errbinders_new.npy')[:,min_temp:max_temp]

## convert your array into a dataframe
df = pd.DataFrame(errbinders)

## save to xlsx file

filepath = 'C:/Users/Pietro/Desktop/binderdump.xlsx'

df.to_excel(filepath, index=False)