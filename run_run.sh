#!/bin/bash


actual_T=0.123
first_test=0
last_test=1
simulation=$actual_T
sigma=1.800
num_temperatures=0

num_tests=$(( $last_test - $first_test + 1))


for test in $(eval echo "{$first_test..$last_test}")
do
 
 python3 make_files.py   $actual_T True $sigma $simulation $test

done




for T_idx in $(eval echo "{0..$num_temperatures}")
do

   bash run.sh $sigma $first_test $last_test $simulation $actual_T

done
