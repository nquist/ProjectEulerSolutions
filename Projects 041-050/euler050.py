# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:42:08 2022

@author: nquist
This solves project Euler problem 50. 

Answer: 997651
Execution Time: 491.44894 seconds
"""
import numpy as np
import time
start = time.time()

max_val = 1000000
vals = [0, 0, 0, 0] # i, j, diff, num

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

Primes_set = find_primes(max_val)
Primes = list(Primes_set)
Primes.sort()

for i in range(22, len(Primes)-1):
    for j in range(0, len(Primes)-(i+1)):
        if i != j:
            sm = sum(Primes[j:(i+1)])
            if sm in Primes_set and (i-j) > vals[2]:
                vals = [i, j, i-j, sm]
            if sm > max_val:
                break

print(vals)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

