# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:06:32 2022

@author: nquist
This solves project Euler problem 47. 

The first two consecutive numbers to have two distinct prime factors are:
    14 = 2 × 7
    15 = 3 × 5
The first three consecutive numbers to have three distinct prime factors are:
    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.
Find the first four consecutive integers to have four distinct prime factors 
each. What is the first of these numbers?

Answer: 134043
Execution Time: 2.09089 seconds
"""
import time
start = time.time()

max_value = 1000000
distinct_primes = 4
consec_length = 4

factor_list = [0]*max_value
starting_val = 0

for idx in range(2, max_value):
    if factor_list[idx] == 0:
        # This is a prime number
        run_count = 0
        new_idx = 1*idx
        while new_idx < len(factor_list):
            factor_list[new_idx] += 1
            new_idx += idx
    elif factor_list[idx] == distinct_primes:
        run_count += 1
        if run_count == consec_length:
            starting_val = idx + 1 - consec_length
            break
    else:
        run_count = 0


if starting_val == 0:
    print('Range not large enough')
else:
    print('The first number in the sequence is %i' % starting_val)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))