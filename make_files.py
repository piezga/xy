import numpy as np
import os
import sys

print('MAKING FILES')

steps = 10
termalization = 0

d = 2

#make_T_file(bool) sigma(1.50) simulation_number test_number

#take the number the identifies the test as the last
#character after the file.py
test = sys.argv[-1]

#take the simulation that identifies the test as the first
#character after the file.py
simulation = sys.argv[-2]


sigma = sys.argv[-3]#'1.50'

make_T_file = sys.argv[-4]#True

temperature = float(sys.argv[-5])#True


print(float(sigma))
if make_T_file == 'False':
    make_T_file = False
print('Simulation data: ',test, simulation, sigma , make_T_file)


parameters = [float(sigma),3,steps,termalization]


Ls = np.array([16])
print(Ls)

numT = 1

tmp = [temperature]
#tmp = np.linspace(0.01,1.1,numT)




   
T = {
45 :np.linspace( 1.69837898 , 1.728 ,numT),
90 :np.linspace( 1.70644139 , 1.728 ,numT),
181 :np.linspace( 1.70749405 , 1.721,numT),
362 :np.linspace(  1.70755791 , 1.716  ,numT),
724 :np.linspace( 1.658 , 1.67  ,numT),

4 : tmp,
16 :  tmp, #np.linspace( 0.001 , 0.02,numT),
32 :tmp, #np.linspace(  0.001 , 0.02  ,numT),
64 :tmp, #np.linspace(   0.001 , 0.02 ,numT),
128 :tmp, #np.linspace(  0.001 , 0.02,numT),
256 :tmp, #np.linspace(   0.001 , 0.02 ,numT),
512 :tmp,#np.linspace(  0.05 , 1.2  ,numT),
750 :np.linspace( 0.1 , 5,numT),
1000 :np.linspace( 0.00281481 , 5 ,numT),

1024 : tmp,# np.linspace( 0.5 , 5 ,numT)
}

if d == 1:
    T = {
512 :np.linspace(2.38,2.465,numT),
1024 :np.linspace(2.47,2.535 ,numT),
2048 :np.linspace(2.525, 2.59 ,numT),
4096 :np.linspace(2.565,2.64 ,numT),
8192 :np.linspace(2.6,2.645 ,numT),
16384 :np.linspace( 2.62,2.67 ,numT),
32768 :np.linspace( 2.635,2.69,numT),
65536 : np.linspace(0.1,3 ,numT)


}


path = 'data/sigma_'+sigma+'/simulation_'+str(simulation)
if d == 1:
    path = 'data/1D/sigma_'+sigma+'/simulation_'+str(simulation)
print('PATH: ', path)


try:
  os.mkdir('data/sigma_'+sigma)
  print('created sigma dir')
except OSError as error:
  print('NOT created sigma dir ')
  pass


try:
  os.mkdir(path)
  print('created_path')
except OSError as error:
  print('NOT created_path ')
  pass

try:
  os.mkdir(path+'/outputs')
  print('created output directory')
except OSError as error:
  print('NOT created output directory')
  pass

if test == '0':
  with open(path+'/L_string.txt','w') as f:
    print('numT = ', numT, file = f)
    for l in T:
      print(l,':np.linspace(',T[l][0],',',T[l][-1],',numT),',file = f)

  f.close()

for L in Ls:
    tot_path = path+'/L_'+str(L)
    try:
      os.mkdir(tot_path)
    except OSError as error:
      print('NOT created_path L')
      pass

    try:
      os.mkdir(tot_path+'/test_'+str(test))
    except OSError as error:
      print('NOT created_path L test')
      pass
    try:
      os.mkdir(tot_path+'/test_'+str(test)+'/seeds')
    except OSError as error:
      print('NOT created_path L test seed')
      pass
    try:
      os.mkdir(tot_path+'/test_'+str(test)+'/last_configuration')
    except OSError as error:
      print('NOT created_path L test seed')
      pass

    if make_T_file:
        with open(tot_path+'/Ts_test_'+str(test)+'.txt', 'w') as f:

            for t in T[L]:
                print(t, file = f)
        f.close()
print('now create Ls file and parameter file')

with open(path+'/Ls_test_'+str(test)+'.txt', 'w') as f:

    for L in Ls:
        print(L, file = f)
f.close()

with open(path+'/parameters_test_'+str(test)+'.txt', 'w') as f:

    for param in parameters:
        print(param, file = f)
f.close()
