# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:21:54 2020

@author: nquist

This code solves Project Euler problem 3. 

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

Answer: 6857
Execution Time: 0.00201 seconds
"""
import time
start = time.time()

def a_factor(num):
    for i in range(1,(num//2)):
        if num%(i+1) == 0:
            return i+1, num//(i+1)
    return 0, num

def factors(num):
    val = 1
    cur_val = 1*num
    factors = [1]
    while val > 0:
        val, cur_val = a_factor(cur_val)
        factors.append(val)
    factors[-1]= 1*cur_val
    
    return factors

print(factors(600851475143))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))