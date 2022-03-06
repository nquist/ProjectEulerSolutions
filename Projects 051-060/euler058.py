# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 18:32:45 2022

@author: nquist
This solves project Euler problem 58. This finds the side length when the ratio
of prime numbers on the diagonals of a square spiral to the total number of 
numbers on the diagonals of the square spiral falls below 10%.

Answer: 26241
Execution Time: 14.89573 seconds
"""
import numpy as np
import time
start = time.time()

diag_count = 1
prime_count = 0
step = 0
ratio = 1

def is_prime(val):
    for j in range(2, int(np.sqrt(val))+1):
        if val%j == 0:
            return False
    return True

def find_next_diag(curr_val, curr_step):
    new_step = curr_step + 2
    new_vals = []
    curval = 1*curr_val
    for j in range(0, 4):
        curval += new_step
        new_vals.append(curval)
    return new_vals, new_step

new_start = 1
while ratio > 0.1:
    test_list, step = find_next_diag(new_start, step)
    new_start = max(test_list)
    #diag_list = diag_list + test_list
    for j in test_list:
        if is_prime(j):
            prime_count +=1
    diag_count += 4
    ratio = prime_count/diag_count
    '''
    if step >10000:
        print(ratio)
        ratio = 0.01'''
    
print('The side length where the diagonal to non diagonal primes is %i' % (step+1))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

