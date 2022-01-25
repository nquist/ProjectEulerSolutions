# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:21:54 2020

@author: nquist

This code solves Project Euler problem 3. The function a_factor returns the 
lowest prime factor of the number (num). Factors uses a_factor to find the list
of prime factors of any given number. In the case of this problem, we were
looking for the highest prime factor of 600851475143.
"""

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