# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 15:26:16 2022

@author: nquist
This solves project Euler problem 37. This finds all the truncatable primes that
are truncatable in both directions. And it returns the sum.

Answer: 748317
Execution Time: 5.01590 seconds
"""
import numpy as np
import time
start = time.time()

max_val = 740000
trunc_primes = []


def find_primes(max_val):
    Primes = [2, 3, 5, 7]
    Num_list = set(range(11, max_val, 2))
    for i in [3, 5, 7]:
        st = set(range(i, max_val, i))
        Num_list = Num_list - st
    
    while min(Num_list)<int(np.sqrt(max_val)):
        curr_num = min(Num_list)
        Primes.append(curr_num)
        sm_set = set([curr_num]+list(range(curr_num*curr_num, max_val, curr_num)))
        Num_list = Num_list - sm_set

    Primes = Primes + list(Num_list)
    
    return(set(Primes))

def check_left_trunc(num):
    str_num = str(num)
    while len(str_num) > 0:
        if int(str_num) not in Primes:
            return False
        str_num = str_num[1:]
    
    return True

def check_right_trunc(num):
    str_num = str(num)
    while len(str_num) > 0:
        if int(str_num) not in Primes:
            return False
        str_num = str_num[:-1]
    
    return True

Primes = find_primes(max_val)

for i in Primes:
    if i > 10:
        if check_right_trunc(i) and check_left_trunc(i):
            trunc_primes.append(i)
    
print('The sum of the bi-directional truncatable primes is %i.' % sum(trunc_primes))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))
