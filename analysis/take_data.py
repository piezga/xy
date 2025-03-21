from functions import *
import sys


end = 500*10**3

#Flags
spatial_cor = 0
thermo = 0
fourier = 1



for i in range(tests):
  print('#########################')
  print('Taking data from test: ', i)
  for L in Ls:
    print('-------------')
    print('L: ', L)

    L_path = path+'/L_'+str(L)+'/'
    total_path = L_path +'test_'+str(i)+'/'

    T = np.loadtxt(L_path+'Ts_test_'+str(i)+'.txt',ndmin=1)
    m_T_x = []
    m_T_x_re = [] 
    m_T_x_im = []
    m_T_y = []
    m_T_y_re = []
    m_T_y_im = []
    spatial = []
    temperature_saving = True

    # Thermalization
    
    if L == 512:

      thermalization = 50 * 10 ** 3

    elif L== 1024:

      thermalization = 100*10**3
    
    else:
      thermalization = 25 * 10 ** 3

  

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
            and 'spatial' not in each_file
            and float(each_file[2:9]) == round(T[temp],6)
            and each_file[-5] == 'x') :#in this way i'm taking only just one time the data  
              print(each_file)
              m_T_x.append(np.fromfile(total_path+each_file[:-7]+'_mx.bin',dtype = 'float')[thermalization:end])
              m_T_y.append(np.fromfile(total_path+each_file[:-7]+'_my.bin',dtype = 'float')[thermalization:end])

              if fourier:
                m_T_x_re.append(np.fromfile(total_path+each_file[:-7]+'_mx_re.bin',dtype = 'float')[thermalization:end])
                m_T_x_im.append(np.fromfile(total_path+each_file[:-7]+'_mx_im.bin',dtype = 'float')[thermalization:end])
                m_T_y_re.append(np.fromfile(total_path+each_file[:-7]+'_my_re.bin',dtype = 'float')[thermalization:end])
                m_T_y_im.append(np.fromfile(total_path+each_file[:-7]+'_my_im.bin',dtype = 'float')[thermalization:end])
  
              if spatial_cor:
                spatial.append(np.fromfile(total_path+each_file[:-7]+'_spatial.bin',dtype = 'float'))
              check_temperature = True

        if not check_temperature:
          temperature_saving = False

                
    try:
      os.mkdir(L_path+'magnetization')
    except OSError as error:
      pass
    if spatial_cor:
      try:
        os.mkdir(L_path+'spatial_cor')
      except OSError as error:
        pass
    if len(m_T_x) > 0:
      m_T_x = np.array(m_T_x,dtype='object')
      m_T_y = np.array(m_T_y,dtype='object')
      m_T_x_re = np.array(m_T_x_re,dtype='object')
      m_T_y_re = np.array(m_T_y_re,dtype='object')
      m_T_x_im = np.array(m_T_x_im,dtype='object')
      m_T_y_im = np.array(m_T_y_im,dtype='object')
 
      np.save(L_path+'magnetization/'+'mx_test_'+str(i)+'.npy',m_T_x)
      np.save(L_path+'magnetization/'+'my_test_'+str(i)+'.npy',m_T_y)
      np.save(L_path+'magnetization/'+'mx_re_test_'+str(i)+'.npy',m_T_x_re)
      np.save(L_path+'magnetization/'+'my_re_test_'+str(i)+'.npy',m_T_y_re)
      np.save(L_path+'magnetization/'+'mx_im_test_'+str(i)+'.npy',m_T_x_im)
      np.save(L_path+'magnetization/'+'my_im_test_'+str(i)+'.npy',m_T_y_im)
 
      if spatial_cor:
        spatial = np.array(spatial,dtype='object')
        print('Spatial shape: ',spatial.shape)
        np.save(L_path+'spatial_cor/'+'spatial_test_'+str(i)+'.npy',spatial)
      
      if temperature_saving:
        np.save(L_path+'magnetization/T.npy',T)
      #print('Data saved in ', L_path+'magnetization/'+'m_test_'+str(i)+'.npy')
      print('Data shape: ', m_T_x.shape)
    else:
      print('No data was found, no data will be saved!')

    print('END')

