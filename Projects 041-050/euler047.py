# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 16:09:08 2022

@author: nquist
This solves project Euler problem 47. 

Answer: 134043
Execution Time: 167.06509 seconds
"""
import numpy as np
import time
start = time.time()
'''
def prime_set(max_val):
    full_set_list = list(range(3,max_val,2))
    Primes = {2}

    while len(full_set_list) > 0:#min(full_set_list)<int(np.sqrt(max_val)):
        curr_val = min(full_set_list)
        Primes.add(curr_val)
        temp_set = set(range(curr_val*curr_val, max_val, 2*curr_val))
        temp_set.add(curr_val)
        full_set_list = list(set(full_set_list) - temp_set)
    
    return Primes
'''
def find_factors(number):
    factors = set()
    if number % 2 == 0:
        factors.add(2)
    while number % 2 == 0:
        number = number //2
        if number == 1:
            return factors
    curr_num = 3
    while number > 1:
        if number % curr_num == 0:
            factors.add(curr_num)
            while number % curr_num == 0:
                number = number // curr_num
        curr_num += 2
    return factors
'''
def find_factors(number):    
    factors = set()
    if number % 2 == 0:
        factors.add(2)
    while number % 2 == 0:
        number = number //2
        if number == 1:
            return factors
    primes_list = list(filter((number).__ge__, starting_primes_list))
    idx = 1
    while number > 1:
        if number % primes_list[idx] == 0:
            factors.add(primes_list[idx])
            while number % primes_list[idx] == 0:
                number = number // primes_list[idx]
        idx += 1
        if idx == len(primes_list):
            break
    return factors
        
max_value = 200000
starting_primes = prime_set(max_value)
starting_primes_list = list(starting_primes)
starting_primes_list.sort()'''

previous = False
count = 0
prime_len = 4
seq_len = 4
starting_val = 0
for i in range(600, max_value):
    facts = find_factors(i)
    if len(facts) == prime_len:
        previous = True
        count += 1
    else:
        previous = False
        count = 0
    
    if previous and count == seq_len:
        starting_val = i - seq_len + 1
        break

if starting_val == 0:
    print('Range not large enough')
else:
    print('The first number in the sequence is %i' % starting_val)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))