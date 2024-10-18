#!/bin/bash

sigma=$1
first_test=$2
last_test=$3
simulation=$4
actual_T=$5




for test in $(eval echo "{$first_test..$last_test}")
do

g++ -fopenmp -o executables/main_sigma_${sigma}_simulation_${simulation}_test_${test}_T_${actual_T} -O3 -std=c++11 -DSFMT_MEXP=607 SFMT.c main.cpp

./executables/main_sigma_${sigma}_simulation_${simulation}_test_${test}_T_${actual_T} ./data/sigma_${sigma}/simulation_${simulation}/parameters_test_${test}.txt  ${simulation} ${test}  > ./data/sigma_${sigma}/simulation_${simulation}/outputs/output_${test}_T_${actual_T}.txt &




done
wait

