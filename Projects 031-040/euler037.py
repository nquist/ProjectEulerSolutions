# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 21:59:23 2022

@author: nquist
This solves project Euler problem 37. This finds all the truncatable primes that
are truncatable in both directions. And it returns the sum.

Answer: 748317
Execution Time: 1411.05703 seconds
"""

import time
start = time.time()

max_val = 740000
Primes = [2, 3, 5, 7]
trunc_primes = []
Num_list = list(range(3, max_val, 2))

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

for i in range(len(Primes)-1):
    temp_set = set(range(Primes[i+1]*Primes[i+1], max_val, 2*Primes[i+1]))
    temp_set.add(Primes[i+1])
    Num_list = list(set(Num_list) - temp_set)

while len(Num_list) > 0:
    curr_val = min(Num_list)
    Primes.append(curr_val)
    temp_set = set(range(curr_val*curr_val, max_val, 2*curr_val))
    temp_set.add(curr_val)
    Num_list = list(set(Num_list) - temp_set)
    
    if check_right_trunc(curr_val) and check_left_trunc(curr_val):
        trunc_primes.append(curr_val)
    
print('The sum of the bi-directional truncatable primes is %i.' % sum(trunc_primes))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))
