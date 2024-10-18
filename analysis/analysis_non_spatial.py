from functions import *
import shutil



print(f'Beginning analysis of simulation {simulation}')

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



try:
  os.mkdir(path+'_analyzed')
except OSError as error:
  pass


print('##################')
print('Taking the magnetization data already checked with the temperature.')

chi_max = np.empty(len(Ls_chosen))

L_idx = 0


for L in Ls_chosen:

    print('L: ',L)
    L_path = path+'/L_'+str(L)+'/'

    analysis_path = path+'_analyzed'+'/L_'+str(L)+'/analysis'
    try:
      os.mkdir(path+'_analyzed'+'/L_'+str(L))
      os.mkdir(path+'_analyzed'+'/L_'+str(L)+'/magnetization')
      os.mkdir(analysis_path)
    except OSError as error:
      pass



    T = np.load(L_path+'magnetization/T.npy')
    np.save(path+'_analyzed'+'/L_'+str(L)+'/magnetization'+'/T.npy', T)

    print('T: ', T)


    chis = []
    binders = []
    ms = []
    ms2 = []
    ms4 = []
    ms_x = []
    ms_y = []
    energy = []
    specific_heat = []


    actual_test = test


    for i in range(test):
        test_path = path+'/L_'+str(L)+f'/test_{i}/last_configuration/'
        test_path_analyzed = path+'_analyzed/L_'+str(L)+f'/test_{i}/last_configuration/'
        try:
           os.mkdir(path+'_analyzed/L_'+str(L)+f'/test_{i}')
        except:
          pass

        if (os.path.exists(L_path+'magnetization/mx_test_'+str(i)+'.npy') and 
            os.path.exists(L_path+'magnetization/my_test_'+str(i)+'.npy')):
            print('Test num: ', i)
            try:
              shutil.copytree(test_path, test_path_analyzed)
            except:
               print('Last configuration yet exists')

            mx_test = np.load(L_path+'magnetization/mx_test_'+str(i)+'.npy', allow_pickle = True)
            my_test = np.load(L_path+'magnetization/my_test_'+str(i)+'.npy', allow_pickle = True)
            print(mx_test.shape)

            if i<2:
              np.save(path+'_analyzed'+'/L_'+str(L)+'/magnetization' + f'/mx_test_{i}.npy',mx_test)
              np.save(path+'_analyzed'+'/L_'+str(L)+'/magnetization' + f'/my_test_{i}.npy',my_test)

            chi_tmp = []
            m_tmp = []
            binder_tmp = []
            mx_tmp = []
            my_tmp = []
            m2_tmp = []
            m4_tmp = []
            for t in range(len(T)):              
                mx_tmp.append(mx_test[t].mean())
                my_tmp.append(my_test[t].mean())
                min_len = min(len(mx_test[t]),len(my_test[t]))
                m_norm = (mx_test[t][:min_len]**2+my_test[t][:min_len]**2)**(0.5)

                m2_tmp.append((m_norm**2).mean())
                m4_tmp.append((m_norm**4).mean())

                m_tmp.append(m_norm.mean())
                chi_tmp.append(susce(m_norm)*(L**d/T[t]))
                binder_tmp.append(binder(m_norm))

            chis.append(chi_tmp)
            ms.append(m_tmp)
            binders.append(binder_tmp)
            ms_x.append(mx_tmp)
            ms_y.append(my_tmp)
            ms2.append(m2_tmp)
            ms4.append(m4_tmp)


        else:
            print('Test num: ',i,' -> Data not found!')
            actual_test -=1



    chis = np.array(chis)
    ms = np.array(ms)
    ms_x = np.array(ms_x)
    ms_y = np.array(ms_y)
    ms2 = np.array(ms2)
    ms4 = np.array(ms4)
    binders = np.array(binders)
    print('Shape', chis.shape)


    chis_mean = chis.mean(axis = 0)
    print('chi shape: ', chis_mean.shape)
    chis_err = chis.std(axis = 0)/np.sqrt(actual_test-1)
  
    
    ms_mean = ms.mean(axis = 0)
    print('m shape: ', ms_mean.shape)
    ms_err = ms.std(axis = 0)/np.sqrt(actual_test-1)


    
    ms_x_mean = ms_x.mean(axis = 0)
    print('mx shape: ', ms_x_mean.shape)
    ms_x_err = ms_x.std(axis = 0)/np.sqrt(actual_test-1)

    
    ms_y_mean = ms_y.mean(axis = 0)
    print('my shape: ', ms_y_mean.shape)
    ms_y_err = ms_y.std(axis = 0)/np.sqrt(actual_test-1)

    
    ms2_mean = ms2.mean(axis = 0)
    print('my shape: ', ms2_mean.shape)
    ms2_err = ms2.std(axis = 0)/np.sqrt(actual_test-1)

    ms4_mean = ms4.mean(axis = 0)
    print('my shape: ', ms4_mean.shape)
    ms4_err = ms4.std(axis = 0)/np.sqrt(actual_test-1)


    cov_m4m2 = covariance(ms4,ms2,ms4_mean,ms2_mean)/(actual_test-1)
    print('cov AB shape: ', cov_m4m2.shape)
    binders_mean = 2 - ms4_mean/(ms2_mean**2)
   


    binders_err = ((ms4_mean)/ms2_mean**2)*np.sqrt(((ms4_err/ms4_mean)**2+4*(ms2_err/ms2_mean)**2-4*cov_m4m2/(ms4_mean*ms2_mean)))

    print('Binders _ err = ' + str(binders_err))
    print('(ms4_err/ms4_mean)**2 = ' + str((ms4_err/ms4_mean)**2))
    print('4*(ms2_err/ms2_mean)**2 = ' + str(4*(ms2_err/ms2_mean)**2))
    print('4*cov_m4m2/(ms4_mean*ms2_mean) = ' + str(4*cov_m4m2/(ms4_mean*ms2_mean)))



    

    # for t in range(len(T)):
    #   print('T: ',T[t])
    #   sample = []
    #   for i in range(test):
    #     tmp = np.load(L_path+'magnetization/m_test_'+str(i)+'.npy', allow_pickle = True)
    #     for x in tmp[t]:
    #       sample.append(x)
      

    np.save(analysis_path + '/T.npy',T)
    np.save(analysis_path + '/m.npy',ms_mean)
    np.save(analysis_path + '/dm.npy',ms_err)
    np.save(analysis_path + '/m_x.npy',ms_x_mean)
    np.save(analysis_path + '/dm_x.npy',ms_x_err)
    np.save(analysis_path + '/m_y.npy',ms_y_mean)
    np.save(analysis_path + '/dm_y.npy',ms_y_err)

    np.save(analysis_path + '/m2.npy',ms2_mean)
    np.save(analysis_path + '/dm2.npy',ms2_err)

    np.save(analysis_path + '/m4.npy',ms4_mean)
    np.save(analysis_path + '/dm4.npy',ms4_err)


    np.save(analysis_path + '/chi.npy',chis_mean)
    np.save(analysis_path + '/dchi.npy',chis_err)
    np.save(analysis_path + '/binder.npy',binders_mean)
    np.save(analysis_path + '/dbinder.npy',binders_err)



    plt.figure(1)
    plt.errorbar(T,ms_mean,ms_err, marker = '.',label = str(L))
    plt.legend()
    plt.figure(2)
    plt.errorbar(T,chis_mean,chis_err, marker = '.',label = str(L))
    plt.legend()
    plt.figure(3)
    plt.errorbar(T,binders_mean,binders_err, marker = '.',label = str(L))
    plt.legend()

    chi_max[L_idx] = max(chis_mean)

    L_idx += 1



plt.figure(4)

plt.title('$\chi$ vs $L$ at $\sigma$ = '+str(sigma))
plt.xlabel('L')
plt.ylabel('$\chi$')

plt.errorbar(Ls_chosen,chi_max,marker = 'o',label='experiment' )

plt.xscale('log')
plt.yscale('log')



popt,pcov = linear_fit(np.log(Ls_chosen),np.log(chi_max))
x_plot = np.linspace(Ls_chosen[0],Ls_chosen[-1],10**3)
plt.plot(x_plot,np.exp(popt[1])*x_plot**popt[0],label='fit' )
print(popt,pcov)

plt.xscale('log')
plt.yscale('log')
plt.legend()



#plt.show()
