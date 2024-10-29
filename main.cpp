#include <iostream>
#include <bits/stdc++.h>
#include <cstring>
#include <string>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include "SFMT.h"
#include <math.h>
#include <omp.h>
#include <cctype>
#include <array>
#include <vector>
#include <random>
#include <cstdlib>
#include <time.h>
#include <ctime>
#include <omp.h>

using namespace std;

#define BUFFER_SIZE 1000

int main(int argc, char *argv[]) {

bool already_termalized = false; //true per fare partire dall'ultima configurazione

int checkpoint = 10;

/*
argc is the argument counter
argv is the string array containing all the arguments passed after the .out.
argv[0] is ./main.out, argv[argc-1] is the last
Scheme:
./main.out  data_path/parameters.txt simulation test [> stoud (optional)]
*/


  int num_threads = 10;
// test is the test Number
  char* simulation = argv[argc-2];
  char* test = argv[argc-1];
  printf("Starting simulation: %s and test: %s\n", simulation,test);

  /*  loading parameter from parameter.txt  */
  ifstream input_param;
  input_param.open(argv[1]);
  if(!input_param.is_open()){
    cout << "Parameters file not found" << endl;
    exit(1);}
  string parameter_strings[5];
  double parameter_numbers[5];
  for(int i=0; i<5 ; i++){
    getline(input_param,parameter_strings[i]);
  }
  for(int i=0; i<5; i++){
    parameter_numbers[i] = stod(parameter_strings[i]);
  }


//Some more variable definitions

  time_t my_time = time(NULL); 
  const double sigma = parameter_numbers[0];
  const int q = parameter_numbers[1];
  const int steps = parameter_numbers[2];
  const int termalization = parameter_numbers[3];
  const double g = parameter_numbers[4];
  string rounded_sigma = to_string(sigma).substr(0, to_string(sigma).find(".")+4);
  string temperatures_path_name = "./data/sigma_" + rounded_sigma +
                                  "/simulation_" + simulation  + "/";
  string sizes_file_name =  "./data/sigma_" + rounded_sigma +
                            "/simulation_" + simulation +"/Ls_test_"+test+".txt";
  string output_path_name = "./data/sigma_" + rounded_sigma +
                            "/simulation_" + simulation  + "/";

  printf("sigma = %f \n",sigma);
  printf("steps = %d \n",steps);
  printf("q = %d \n",q);
  printf("termalization = %d \n",termalization);
  printf("Temperatures path: %s\n", temperatures_path_name.c_str());
  printf("Sizes file: %s\n", sizes_file_name.c_str());
  printf("output path: %s\n", output_path_name.c_str());
  fflush(stdout);



  FILE  *sizes_file;


  int initialization = time(NULL);
  initialization += (50*atoi(test)*atoi(test));
  srand (initialization);
  clock_t now_time, tStart = clock();

  int c;    //this must be an int (we need it to get number of sizes)
  int number_of_L = 0;//number of sizes
  int index_L = 0;//temporary index to store sizes

  double lower = sqrt(2) ; //this is the lower bound of the distances extracted

  double  alpha = -1/sigma; //this is the exponent for the distance extraction

  //for time computing via omp_get_wtime()
  double start; 
  double end;

  printf("Opening the size's file...\n");
  fflush(stdout);

  //open the file containing the sizes
  sizes_file = fopen(sizes_file_name.c_str(),"r");

  printf("Done!\n");
  fflush(stdout);

  printf("getting the number of sizes\n");
  fflush(stdout);

  //get the number of sizes
  for (c = getc(sizes_file); c != EOF; c = getc(sizes_file))
    if (c == '\n') // Increment count if this character is newline
      number_of_L = number_of_L + 1;


  printf("Done!\n");
  fflush(stdout);
  printf("Number of sizes: %d\n", number_of_L);
  fflush(stdout);

  //reput the FILE puntactor at the start of the file
  rewind(sizes_file);

  //create the size array and put the sizes into it
  int Ls[number_of_L];


  while (fscanf(sizes_file, "%d", &Ls[index_L])!=EOF){
    index_L ++;
  }

  fclose( sizes_file );




  //start the loop over the sizes
  printf("number of Ls: %d \n", number_of_L);
  for(int sizes = 0; sizes < number_of_L; sizes ++){

    int tmp, L, number_of_T = 0, index_T = 0;
    string  temperatures_file_name;
    FILE *temperatures_file;
    L = Ls[sizes];
    int max_distance = L / 2;
    double spatial_correlations[max_distance];



    // open the temperature files
  printf("Opening the T's file...\n");
  fflush(stdout);

    temperatures_file_name = temperatures_path_name + "L_"+to_string(L)+"/Ts_test_"+test+".txt";
    printf("Temperatures FILE: %s\n", temperatures_file_name.c_str());
	fflush(stdout);

    temperatures_file = fopen(temperatures_file_name.c_str(),"r");
    // gets the number of temperatures
    for (tmp = getc(temperatures_file); tmp != EOF; tmp = getc(temperatures_file))
      if (tmp == '\n') // Increment count if this character is newline
        number_of_T = number_of_T + 1;

    printf("Number of temperatures: %d\n", number_of_T);
    //put the puntactor of the file at the start of this one
    rewind(temperatures_file);
    //create a temperatures array in which we store the temperatures
    double Ts[number_of_T];

    while (fscanf(temperatures_file, "%lf", &Ts[index_T])!=EOF){
      index_T ++;
    }
    fclose( temperatures_file );


    // START THE LOOP OVER TEMPERATURES

    //set the number of threads as number_of_T
    num_threads = number_of_T;


    /* defining main random seed */

    /* inizialing seeds for different threads */

    printf("\n> Seed estratti per i diversi threads: \n\n");

    int seeds[num_threads];
    bool seed_check_flag = true;

    while (seed_check_flag){
      for(int i = 0; i<num_threads ; i++){
        seeds[i] = (rand()%100000);
      }
      /* checking diversity of seeds */

      for (int i = 0; i < (num_threads-1); i++ ) {
        for (int j = (i+1); j < num_threads; j++ ) {
          if ( seeds[i] == seeds[j] ) { seed_check_flag = false; }
        }
      }
      if (!seed_check_flag){
         printf("\n> Flag di controllo sui seeds : false \n");
         seed_check_flag = true;
      }
      else{
        /*Print the seeds*/
        for(int i = 0; i<num_threads ; i++){
          if ( (i+1) == 0) { printf("\t %d", seeds[i]); }
          else if ( (i+1) % 4 == 0) { printf("\t %d \n", seeds[i]); }
          else { printf("\t %d", seeds[i]); }
        }
        printf("\n");
        seed_check_flag = false;       
      }
    }
    
    //for(int temperature = 0; temperature < number_of_T; temperature ++)
    tStart = clock();
 
    start = omp_get_wtime(); 
    omp_set_num_threads(num_threads);
      int temperature = omp_get_thread_num();
      printf("%i",temperature);
      //initialize random generator
      sfmt_t sfmt;
      sfmt_init_gen_rand(&sfmt, seeds[temperature]);

      int center_x, center_y;
      double T,r, unif, theta,energy,neigh_theta,new_theta;
      double U,V,Sq,theta_q, Sq_x = 0, Sq_y = 0;
      double   magne_x = 0, magne_y = 0;
      string output_file_name_x,output_file_name_y, spatial_cor_file_name, seed_file_name, configuration_file_name;
      FILE * data_output_file_x, * data_output_file_y, * seed_file, * configuration_file, *spatial_cor_file;
      //double lattice[L][L];


    double **   lattice      = new double *  [L] ;

    for(int i=0 ; i<L ; i++){
        lattice[i]      =   new double [L];
    }


      T = Ts[temperature];
      double beta = 1/T;
      //save in the a file seed.txt the seed

      seed_file_name = output_path_name+"L_"+to_string(L)+"/test_"+test+
                        "/seeds/T_"+to_string(T)+".txt";
      seed_file = fopen(seed_file_name.c_str(), "w");
      fprintf(seed_file,"%d",seeds[temperature]);
      fclose(seed_file);

      // cold start!!
      for (int i = 0; i < L; i++){
         for (int j = 0; j < L; j++){
              lattice[i][j] = 0;
         }
      }
      //hot start
      // for (int i = 0; i < L; i++){
      //    for (int j = 0; j < L; j++){
      //         lattice[i][j] = 2*M_PI*sfmt_genrand_res53(&sfmt) - M_PI;
      //    }
      // }

      output_file_name_x = output_path_name+"L_"+
                          to_string(L)+"/test_"+test+"/T_"+to_string(T)+"_mx.bin";
      printf("Output FILE: %s\n", output_file_name_x.c_str());
      data_output_file_x = fopen( output_file_name_x.c_str() ,"wb");
      output_file_name_y = output_path_name+"L_"+
                          to_string(L)+"/test_"+test+"/T_"+to_string(T)+"_my.bin";
      printf("Output FILE: %s\n", output_file_name_y.c_str());
      data_output_file_y = fopen( output_file_name_y.c_str() ,"wb");

      spatial_cor_file_name = output_path_name+"L_"+
                          to_string(L)+"/test_"+test+"/T_"+to_string(T)+"_spatial.bin";
      printf("Spatial correlation FILE: %s\n", spatial_cor_file_name.c_str());
      spatial_cor_file = fopen( spatial_cor_file_name.c_str() ,"wb");

      fflush(stdout);

    
      //int count = 0;
      //TERMALIZATION
      if (already_termalized){
        configuration_file_name = output_path_name+"L_"+to_string(L)+"/test_"+test+
                        "/last_configuration/T_"+to_string(T)+".bin";

printf("Taking last configuration from %s\n", configuration_file_name.c_str());
fflush(stdout);
printf("Opening...\n");
fflush(stdout);

        configuration_file = fopen(configuration_file_name.c_str(), "rb");

  printf("File opened!\n");
  fflush(stdout);
fflush(stdout);

        double *  flatten_lattice = new double  [L*L] ;   //double flatten_lattice[L*L];

   printf("Flat lattice created!\n");
  fflush(stdout); 


  fflush(stdout); 

        for (int i = 0; i < L; i++){
          for (int j = 0; j < L; j++){
            
            lattice[i][j] = flatten_lattice[i*L+j];

          }

        }

  printf("Lattice filled!\n");
  fflush(stdout); 

        fclose(configuration_file);

  printf("File closed!\n");
  fflush(stdout); 



//delete [] flatten_lattice;

      }

  
printf("num steps: %d \n", steps);
fflush(stdout);
printf("################\n\n");
printf("Beginning step time record\n\n");
      for (int step = 0; step < steps; step++){

        
    
        if (step % checkpoint == 0) {
          time(&my_time); // Update my_time each time this block is entered
          printf("Step number %d performed on ",step);
          printf("%s\n", ctime(&my_time));
        }

       fflush(stdout);


        for (int spinflip = 0; spinflip < pow(L,2); spinflip++) {
          center_x = (int)(L*sfmt_genrand_res53(&sfmt))%L;
          center_y = (int)(L*sfmt_genrand_res53(&sfmt))%L;
          //Find q neighbours and compute the local energy
          Sq_x = 0;
          Sq_y = 0;



     
      fflush(stdout);

	  for (int j = 0; j < 4; j++){              
              r  = 1;
              theta = j*(M_PI/2);       
              neigh_theta = lattice[((center_x+(int)round(r*cos(theta)))%L + L )%L]
                                    [((center_y+(int)round(r*sin(theta)))%L+L)%L];
              Sq_x += cos(neigh_theta);
              Sq_y += sin(neigh_theta);
              
          }



          for (int j = 0; j < q; j++){
              unif = 1-sfmt_genrand_res53(&sfmt);
              r  = lower*exp(alpha*log(unif));//lower*pow(unif,alpha);
              
                unif = sfmt_genrand_res53(&sfmt);
                theta = unif*(2*M_PI);
                neigh_theta = lattice[((center_x+(int)round(r*cos(theta)))%L + L )%L]
                                    [((center_y+(int)round(r*sin(theta)))%L+L)%L];
                Sq_x += g*cos(neigh_theta);
                Sq_y += g*sin(neigh_theta);
              
          }


     
      fflush(stdout);


          Sq = sqrt(pow(Sq_x,2) + pow(Sq_y,2));
          if (Sq == 0){
            //new angle accepted (the interaction of neighbours is zero so it costs zero to move the angle)
            new_theta = 2*M_PI*sfmt_genrand_res53(&sfmt) - M_PI;
            lattice[center_x][center_y] = new_theta;
          }
          else{
            theta_q = atan2(Sq_y,Sq_x);
            energy = beta*Sq;
            if (energy > M_PI/8){       
              //New angle generation via Gaussian heat-bath
              new_theta = 4;
              while ((new_theta < -M_PI) || (new_theta > M_PI)){
                U = 1-sfmt_genrand_res53(&sfmt);
                V = 1-sfmt_genrand_res53(&sfmt);
                new_theta = sqrt(-2*log(U))*cos(2*M_PI*V)*(M_PI/2)*(1/sqrt(energy));
                if ((new_theta < -M_PI) || (new_theta > M_PI)){
                  new_theta = sqrt(-2*log(U))*sin(2*M_PI*V)*(M_PI/2)*(1/sqrt(energy));
                }
              }
              //Acceptance step
              unif = sfmt_genrand_res53(&sfmt)*exp(-2*energy*pow(new_theta/M_PI,2));
              if (unif < exp(-energy*(1-cos(new_theta)))){
                //new_theta is the difference between theta_q and the new angle.
                //It doesn't matter if the new angle is out of the boundary (-pi,pi],
                //because we only compute sin and cos of angles...(?)
                lattice[center_x][center_y] = new_theta + theta_q;
                // tmp = new_theta + theta_q;
                // if (tmp > M_PI){
                //   tmp -= 2*M_PI;
                // }
                // else if(tmp < -M_PI){
                //   tmp += 2*M_PI;
                // }
                // lattice[center_x][center_y] = tmp;
              }
            }
            else{
              //New angle generation via Uniform heat-bath
              new_theta = 2*M_PI*sfmt_genrand_res53(&sfmt) - M_PI;
              unif = sfmt_genrand_res53(&sfmt);
              if (unif < exp(-energy*(1-cos(new_theta)))){
                lattice[center_x][center_y] = new_theta + theta_q;
                // tmp = new_theta + theta_q;
                // if (tmp > M_PI){
                //   tmp -= 2*M_PI;
                // }
                // else if(tmp < -M_PI){
                //   tmp += 2*M_PI;
                // }
                // lattice[center_x][center_y] = tmp;
              }
            }
          }
        }
        //if (step % 20 == 0){

        magne_x = 0;
        magne_y = 0;
        for (int k = 0; k < L; k++){
            for (int l = 0; l < L; l++){
                magne_x += cos(lattice[k][l]);
                magne_y += sin(lattice[k][l]);
            }
        }

        magne_x = magne_x/pow(L,2);
        magne_y = magne_y/pow(L,2);

        fwrite(&magne_x,sizeof(double), 1, data_output_file_x);
        fwrite(&magne_y,sizeof(double), 1, data_output_file_y);
   //   }


    
      }

   //free( my_buffer );
      fclose( data_output_file_x );
      fclose( data_output_file_y );
      fclose( spatial_cor_file );

      configuration_file_name = output_path_name+"L_"+to_string(L)+"/test_"+test+
                        "/last_configuration/T_"+to_string(T)+".bin";
      configuration_file = fopen(configuration_file_name.c_str(), "wb");
      for (int k = 0; k < L; k++){
        for (int l = 0; l < L; l++){
                fwrite(&lattice[k][l],sizeof(double), 1, configuration_file);

              }

          }

      fclose( configuration_file);

    
    now_time = clock();
    printf("End of simulation for L: %d\n",L);
    printf("Time taken: %.2fs\n", (double)(now_time - tStart)/CLOCKS_PER_SEC);
    end = omp_get_wtime(); 
    printf("Time (per-thread) taken: %.2fs\n", (double)(end - start));
    fflush(stdout);

  }

  return 0;

}






