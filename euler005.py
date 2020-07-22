# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:45:19 2020

@author: nquist

This code solves project euler problem 5. It has a function called prime factors
that finds and returns a list of the prime factors of a given number. This is used
in a loop to find all the prime factors of the numbers 1-20. This was used to 
create a list of all the unique factors of the numbers while retaining the correct
quantity of each factor. The product of this list was found and printed. 
"""
import numpy as np

def prime_factors(num):
    vals = []
    divide = True
    cur_num = 1*num
    while divide:
        count = 2
        found = False
        while not found:
            if count <= cur_num:
                if cur_num%count == 0:
                    vals.append(count)
                    cur_num = cur_num//count
                    found = True
                else:
                    count += 1
            else:
                found = True
                divide = False
    return vals

all_factors = []
for i in range(2, 21):
    facts = prime_factors(i)
    nums = list(set(facts))
    for i in range(len(nums)):
        ct_in = all_factors.count(nums[i])
        ct_out = facts.count(nums[i])
        if ct_in < ct_out:
            all_factors = all_factors + [nums[i]]*(ct_out-ct_in)

prod = 1
for k in range(len(all_factors)):
    prod = prod*all_factors[k]
    
print(prod)
        
            