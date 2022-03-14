# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 16:09:08 2022

@author: nquist
This solves project Euler problem 776. 

Answer: 
Execution Time:  seconds


    IN PROGRESS ----- NOT COMPLETE
"""

import time
start = time.time()

def is_prime(num):
    for i in range(2, int(np.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

primes_list = [2, 3, 5, 7]
primes_set = set(primes_list)
consec_list = []
counter = 11
while len(consec_list)<3:
    if is_prime(counter):
        primes_list.append(counter)
        primes_set.add(counter)
        counter += 1
    else:
        temp_val = 1*counter
        for k in primes_list:
            if 

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))