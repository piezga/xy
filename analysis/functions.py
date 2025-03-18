#import scienceplots
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import os

from statsmodels.api import GLS as gls
from statsmodels.api import add_constant as add_const
from sklearn.preprocessing import PolynomialFeatures
from variables import *

#plt.style.use(['science'])


def jackknife(sample,block):
  new_m = []
  if len(sample)%block!= 0:
      cut_sample = sample[:-(len(sample)%block)]
  else:
    cut_sample = sample


  for j in range(int(len(cut_sample)/block)):
      new_m.append(cut_sample[j*block:j*block+block].mean())
  new_m = np.array(new_m)


  return new_m.std()/(np.sqrt(len(new_m)-1))

def auto_bootstrap(func,sample,num_of_estim,block_size, N = 0):
  
  if len(sample)%block_size != 0:
    sample = sample[:-(len(sample)%block_size)]
    
  if N == 0:
    N = len(sample)
    
  M = num_of_estim
  estimators = np.empty(M)
  
  for i in range(M):   
     
    new_sample = np.empty(N)
    indexes = np.random.randint(0,N-block_size+1,size = int(N/block_size))
    for j in range(int(N/block_size)):
        
        new_sample[block_size*j:block_size*j+block_size] = sample[indexes[j]:indexes[j]+block_size]
    #print(j+block_size)
    estimators[i] = func(new_sample)

  
  return estimators.std()



def bootstrap(func,sample,num_of_estim):
  N = len(sample)
  M = num_of_estim
  estimators = np.empty(M)
  for i in range(M):   
    #sampling N indexes 
    indexes = np.random.randint(0,N,size = N)
    new_sample= sample[indexes]
    estimators[i] = func(new_sample)

  return estimators.std()

def binder(sample):
  x2 = (sample**2).mean()
  x4 = (sample**4).mean()
  return 1-x4/(3*x2**2)


def susce(sample):
  x = abs(sample).mean()
  x2 = (sample**2).mean()
  
  return (x2-x**2) 

def poly_fit(x,y,degree,dy = []):
    poly = PolynomialFeatures(degree=degree, include_bias=True)
    poly_features = poly.fit_transform(x.reshape(-1, 1))
    if dy == []:
        model = gls(y, poly_features)
        results = model.fit()

        return results.params[::-1],results.cov_params()[::-1,::-1]
    else:
        model = gls(y, poly_features, sigma = dy**2)
    results = model.fit()

    return results.params[::-1],results.normalized_cov_params[::-1,::-1]


def linear_fit(x,y,dy=[]):
    x = add_const(x)
    if dy == []:
        model = gls(y, x)
        results = model.fit()

        return results.params[::-1],results.cov_params()[::-1,::-1]



    else:

        model = gls(y, x,sigma = dy**2)
    results = model.fit()
    return results.params[::-1],results.normalized_cov_params[::-1,::-1]

def susce(sample):
    m = abs(sample).mean()
    m2 = (sample**2).mean()
    return m2-m**2


def get_m_q(x1,y1,x2,y2):
  '''
  return (m,q): the angular coefficient and intercept of the line passing through the two
  points.
  '''
  assert x1 != x2 and y1 != y2, \
  'Coincident points: infinite lines pass through them!'

  assert x1 != x2, \
  'points have the same x, the line will be vertical'

  return ((y2-y1)/(x2-x1),(y1*x2-y2*x1)/(x2-x1)) 
def find_extremis(arr,value):
    '''
    Find the nearest points of 'arr' between whom "value" can be found 
    '''
    dif_arr = abs(arr - value)
    first_extreme = np.where(dif_arr == min(dif_arr))
    first_extreme = first_extreme[0][0]
    if (arr-value)[first_extreme] > 0:
        second_extreme = first_extreme - 1
    else:
        second_extreme = first_extreme + 1
    return first_extreme, second_extreme

def find_cross_value(value,x,y):

    first, second = find_extremis(x,value)
    m,q = get_m_q(x[first],y[first],x[second],y[second])

    return m*value + q

def naive_derivative(x,y):
    
    return (y[:-1]-y[1:])/(x[:-1]-x[1:])
    
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


def delta_inf(y,Ls):
    x_extrapolation = (Ls[::-1][:-1])
    x_extrapolation = 1/np.array(x_extrapolation)
    y_extrapolation = np.empty(len(Ls)-1)
    for l in np.arange(1,len(Ls)):
        y_extrapolation[l-1] = y[l] - y[l-1]
    y_extrapolation = y_extrapolation[::-1]
    m,y_inf = np.polyfit(x_extrapolation,y_extrapolation,1)
    return y_inf

def covariance(A, B, mean_A, mean_B):
    
    cov_AB = np.mean((A - mean_A) * (B - mean_B), axis = 0)
    print('covariance ', cov_AB)

    return cov_AB

def copy_file(src_dir,dst_dir,filename):
   # Construct the full path of the source file
  src_path = os.path.join(src_dir, filename)
  # Construct the full path of the destination file
  dst_path = os.path.join(dst_dir, filename)
  # Copy the file from the source directory to the destination directory
  shutil.copy(src_path, dst_path)


def autocorrelation_time(series, max_lag=None):  #In futuro da implementare la FFT
    series = np.asarray(series.ravel())
    n = len(series)
    mean = np.mean(series)
    var = np.var(series)
    
    if max_lag is None:
        max_lag = n // 10  # PROBLEMA!!!
                           # set an adaptive kmax? -> prossimamente  
    autocorr = []
    for lag in range(max_lag):
        cov = np.sum((series[:n-lag] - mean) * (series[lag:] - mean)) / n
        autocorr.append(cov / var)
    
    autocorr = np.array(autocorr)
    tau_int = 1 + 2 * np.sum(autocorr[1:])  # Skip lag=0 for the sum
    return tau_int, autocorr


def csi_error(m, dm, mk, dmk, covariance): #Gives the error for csi WITHOUT PREFACTOR
  

  m_term = m**2/(mk**4 * (m**2/mk**2 -1)) * dm
  mk_term = m**4/(mk**6 * (m**2/mk**2 -1)) * dmk
  cross_term = 2 * m**3/(mk**5 * (m**2/mk**2 -1)) * covariance
  
  square_error = m_term + mk_term - cross_term
  error = np.sqrt(square_error)

  return error



if __name__ == "__main__":
  print('Just a module! There is not a reason to execute it!')
