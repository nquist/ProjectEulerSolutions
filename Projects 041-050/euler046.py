# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:00:07 2022

@author: nquist
This solves project Euler problem 46. 

It was proposed by Christian Goldbach that every odd composite number can be 
written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime 
and twice a square?

Answer: 5777
Execution Time: 0.08599 seconds
"""
import numpy as np
import time
start = time.time()

def is_prime(num):
    for i in range(2, int(np.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

def next_double_square(curr_val):
    base = int(np.sqrt(curr_val/2))
    return 2*(base+1)**2

primes_list = [2, 3, 5, 7]
double_squares_set = set([2, 8, 18, 32])
found = False
curr_val = 11
while not found:
    if curr_val > max(double_squares_set):
        double_squares_set.add(next_double_square(max(double_squares_set)))
    if is_prime(curr_val):
        primes_list.append(curr_val)
    else:
        found = True
        for j in primes_list:
            if (curr_val-j) in double_squares_set:
                found = False
                break
    curr_val += 2

print('The smallest composite that satisifies this is %i' % (curr_val-2))
        

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))
