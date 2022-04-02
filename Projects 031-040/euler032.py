# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 17:22:25 2022

@author: nquist
This solves project Euler problem 32. 

We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 
5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can 
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.

Answer: 45228
Execution Time: 5.40415 seconds
"""
from itertools import permutations
import time
start = time.time()

def test_multi(number_str):
    prods = []
    for i in range(1, 4):
        for j in range(1, 7-i):
            cal = int(number_str[:i])*int(number_str[i:i+j])
            if cal == int(number_str[i+j:]):
                prods.append(int(number_str[i+j:]))
    return prods

number_per = list(permutations('123456789'))
number_per = [''.join(perm) for perm in number_per]
prods_list  = []
for nums in number_per:
    new_list = test_multi(nums)
    prods_list = prods_list + new_list

prods_list = list(set(prods_list))
print('The sum of the products is %i' % sum(prods_list))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))