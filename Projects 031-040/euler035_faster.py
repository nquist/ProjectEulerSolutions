# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 15:17:40 2022

@author: nquist
This solves project Euler problem 35. This finds number of circular primes
below one million.

Answer: 55
Execution Time: 7.49147 seconds
"""
import numpy as np
import time
start = time.time()

max_val = 1000000
full_set_list = set(range(3,max_val,2))
Primes = [2]

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
    
def is_circ(num):
    string_num = str(num)
    new_val = string_num +''
    for i in range(len(new_val)-1):
        new_val = new_val[1:] + new_val[0]
        if int(new_val) not in Primes:
            return False
    
    return True

Primes = find_primes(max_val)
circ_Primes = [2, 3, 5, 7, 11]

for i in Primes:
    if i > 11:
        if is_circ(i):
            circ_Primes.append(i)
        
print("The number of circular primes lower than one million is %i." % len(circ_Primes))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))


