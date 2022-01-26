# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:05:53 2020

@author: nquist
This solves project Euler problem 10. This finds the sum of the primes that are
2 million 

Answer: 142913828922
Execution Time: 13.60660 seconds
"""
import numpy as np
import time
start = time.time()

max_val = 2000000
full_set_list = list(range(3,max_val,2))
Primes = [2]

while min(full_set_list)<int(np.sqrt(max_val)):
    curr_val = min(full_set_list)
    Primes.append(curr_val)
    temp_set = set(range(curr_val*curr_val, max_val, 2*curr_val))
    temp_set.add(curr_val)
    full_set_list = list(set(full_set_list) - temp_set)

Primes = Primes + full_set_list
print('The sum of the primes lower than %.0f is %i.' % (max_val, sum(Primes)))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))