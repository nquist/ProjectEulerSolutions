# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 16:19:08 2022

@author: nquist
This solves project Euler problem 41. This finds the largest pandigital number
that is prime.

Answer: 7652413
Execution Time: 3.49583 seconds
"""
import numpy as np
import itertools
import time
start = time.time()

def is_prime(num):
    for i in range(2, int(np.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

def all_pandigitals(num):
    perms = itertools.permutations(range(1, num+1))
    perms_list = []
    for vals in perms:
        string = ''
        for j in range(len(vals)):
            string += str(vals[j])
        perms_list.append(int(string))
    
    return perms_list


def find_largest_pan(max_length):
    for i in range(max_length, 0, -1):
        lst = all_pandigitals(i)
        lst = sorted(lst, reverse=True)
        for j in range(len(lst)):
            if is_prime(lst[j]):
                return str(lst[j])


print('The largest prime pandigital number is %s.' % find_largest_pan(9))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))


