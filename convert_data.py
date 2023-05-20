from functions import *

chi_max = np.empty(len(Ls_chosen))

for i in range(test):
  print('#########################')
  print('Taking data from test: ', i)
  #Ls = np.loadtxt(path+'/Ls_test_'+str(i)+'.txt', dtype = 'int16')
  Ls = Ls_chosen
  for L in Ls:
    print('-------------')
    print('L: ', L)
    L_path = path+'/L_'+str(L)+'/'
    total_path = L_path +'test_'+str(i)+'/'
    T = np.loadtxt(L_path+'Ts_test_'+str(i)+'.txt',ndmin=1)      #this is where I read the temperatures
    m_T_x = []
    m_T_y = []
    temperature_saving = True
    for temp in range(len(T)):
     # print('T: ', T[temp])
      if os.path.exists(total_path):
        list_of_files = os.listdir(total_path) #list of files in the current directory
        check_temperature = False
        for each_file in list_of_files:
            if (each_file != 'Ts.txt'
            and each_file != 'analysis'
            and each_file != 'seeds'
            and each_file != 'last_configuration'
	          and each_file != 'binder.npy'
            and float(each_file[2:-7]) == round(T[temp],6)
            and each_file[-5] == 'x') :#in this way i'm taking only just one time the data  
              m_T_x.append(np.fromfile(total_path+each_file[:-7]+'_mx.bin',dtype = 'float')[-150000:])
              m_T_y.append(np.fromfile(total_path+each_file[:-7]+'_my.bin',dtype = 'float')[-150000:])
              check_temperature = True
              try:
                os.remove(total_path+each_file[:-7]+'_mx.bin')
                os.remove(total_path+each_file[:-7]+'_my.bin')
              except:
                print('No data to remove')
      
            # print('Data taken! (',total_path+each_file,') shape: ', m_T[-1].shape)
        if not check_temperature:
          temperature_saving = False

                
    try:
      os.mkdir(L_path+'magnetization')
    except OSError as error:
      pass
    if len(m_T_x) > 0:
      m_T_x = np.array(m_T_x,dtype='object')
      m_T_y = np.array(m_T_y,dtype='object')
      np.save(L_path+'magnetization/'+'mx_test_'+str(i)+'.npy',m_T_x)
      np.save(L_path+'magnetization/'+'my_test_'+str(i)+'.npy',m_T_y)
      
      if temperature_saving:
        np.save(L_path+'magnetization/T.npy',T)
      #print('Data saved in ', L_path+'magnetization/'+'m_test_'+str(i)+'.npy')
      print('Data shape: ', m_T_x.shape)
    else:
      print('No data was found, no data will be saved!')

    print('END')

