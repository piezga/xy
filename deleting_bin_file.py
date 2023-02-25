from functions import *

total_memory = 0

for L in Ls_chosen:
    L_path = path +'/L_'+str(L)+'/'
    print('L: ',L)
    if os.path.exists(L_path+'magnetization/T.npy'):
        for i in range(test):
            print('test: ', i)
            if (os.path.exists(L_path+'magnetization/mx_test_'+str(i)+'.npy') and
                os.path.exists(L_path+'magnetization/my_test_'+str(i)+'.npy')):
                dir_path = L_path +'test_'+str(i)+'/'
                list_of_files = os.listdir(dir_path)
                for file in list_of_files:
                    if 'bin' in file:
                        print('removing file: ',dir_path+file)
                        total_memory += os.path.getsize(dir_path+file)
                        os.remove(dir_path+file)

print(f'Total memory deleted: {total_memory} bytes, {total_memory*10**-6} Mb, {total_memory*10**-9} Gb')