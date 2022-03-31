# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 12:36:22 2022

@author: nquist
This solves project Euler problem 49. 

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases 
by 3330, is unusual in two ways: (i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this 
sequence?

Answer: 296962999629
Execution Time: 0.08900 seconds
"""
from itertools import permutations
import time
start = time.time()

def find_primes(min_val, max_val):
    starting_set = set(range(3, max_val+1, 2))
    primes_list = []
    while len(starting_set) > 0:
        val = min(starting_set)
        if val >= min_val:
            primes_list.append(val)
        val_set = set(range(val, max_val, val))
        starting_set = starting_set - val_set
    
    return primes_list 

def find_permutations(number_str):
    perm_set = set()
    number_per = list(permutations(number_str))
    for perm in number_per:
        new_perm = ''.join(perm)
        if int(new_perm) >= 1000 and int(new_perm) in primes_set:
            perm_set.add(int(new_perm))
    return perm_set

def find_span(nums_set):
    nums_list = list(nums_set)
    nums_list.sort()
    for i in range(len(nums_list)-2):
        for j in range(i+1, len(nums_list)-1):
            diff = nums_list[j] - nums_list[i]
            if (nums_list[j] + diff) in nums_set:
                return str(nums_list[i]) + str(nums_list[j]) + str(nums_list[j]+ diff)
                
    return str(0)


four_digit_primes = find_primes(1000, 10000)   
primes_set = set(four_digit_primes)     
values = set()
for val in four_digit_primes:
    curr_set = find_permutations(str(val))
    if len(curr_set) >= 3:
        curr_val = find_span(curr_set)
        if curr_val != '0':
            values.add(int(curr_val))

print('The value is %i.' % max(values))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))
