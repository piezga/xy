import numpy as np


def n_linfit_params(X,Y,fitpoints):
    ms = []
    qs = []
    for i in range(len(X)-fitpoints+1):
        x = X[i:i+fitpoints]
        y = Y[i:i+fitpoints]
        m,q = np.polyfit(x,y,1)
        ms.append(m)
        qs.append(q)
    return ms, qs
    


a = np.arange(4)
b = np.array([1,0,2.5,3.1])
points = 2 

coeff = n_linfit_params(a,b,points)


print(coeff)