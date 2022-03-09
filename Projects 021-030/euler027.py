# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 18:25:19 2022

@author: nquist
This solves project Euler problem 27. 

Euler discovered the remarkable quadratic formula:
    n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive 
integer values 0 <= n <= 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41$ is clearly divisible 
by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes 
for the consecutive values 0 <= n <= 79. The product of the coefficients, −79 
and 1601, is −126479.

Considering quadratics of the form:
    n^2 + an + b, where |a| <= 1000 and |b| <= 1000
    where |n| is the modulus/absolute value of n (e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, 
starting with n = 0.

Answer: -59231
Execution Time: 5.24217 seconds
"""
import numpy as np
import time
start = time.time()

def find_primes(max_val):
    primes_list = [2]
    starting_set = set(range(3, max_val, 2))
    while len(starting_set) > 0:
        val = min(starting_set)
        temp_set = set(range(val, max_val, val))
        starting_set = starting_set - temp_set
        primes_list.append(val)
    return primes_list

def is_prime(val):
    for i in range(2, int(np.sqrt(abs(val)))+1):
        if val%i == 0:
            return 0
    return 1

def new_function(n, a, b):
    return(n**2 + a*n + b)

b_list = find_primes(1000)
val_list = []
for i in range(-1000, 1001):
    for j in b_list:
        add1 = True
        add2 = True
        max_val = 71
        for k in range(1,max_val):
            if is_prime(new_function(k, i, j)) == 0:
                add1 = False
                break
        for l in range(1,max_val):
            if is_prime(new_function(l, i, j)) == 0:
                add2 = False
                break
        if add1: val_list.append([i, j])
        if add2: val_list.append([i, -j])

print('The product is %i.' % (val_list[0][0]*val_list[0][1]))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

