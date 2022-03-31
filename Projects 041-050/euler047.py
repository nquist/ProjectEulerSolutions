# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 16:09:08 2022

@author: nquist
This solves project Euler problem 47. 

The first two consecutive numbers to have two distinct prime factors are:
    14 = 2 × 7
    15 = 3 × 5
The first three consecutive numbers to have three distinct prime factors are:
    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.
Find the first four consecutive integers to have four distinct prime factors 
each. What is the first of these numbers?

Answer: 134043
Execution Time: 167.06509 seconds
"""
import numpy as np
import time
start = time.time()

def find_factors(number):
    factors = set()
    if number % 2 == 0:
        factors.add(2)
    while number % 2 == 0:
        number = number //2
        if number == 1:
            return factors
    curr_num = 3
    while number > 1:
        if number % curr_num == 0:
            factors.add(curr_num)
            while number % curr_num == 0:
                number = number // curr_num
        curr_num += 2
    return factors

max_value = 200000

previous = False
count = 0
prime_len = 4
seq_len = 4
starting_val = 0
for i in range(600, max_value):
    facts = find_factors(i)
    if len(facts) == prime_len:
        previous = True
        count += 1
    else:
        previous = False
        count = 0
    
    if previous and count == seq_len:
        starting_val = i - seq_len + 1
        break

if starting_val == 0:
    print('Range not large enough')
else:
    print('The first number in the sequence is %i' % starting_val)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))