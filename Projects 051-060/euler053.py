# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 22:28:59 2022

@author: nquist
This solves project Euler problem 53. This find the number of r and n values such
that the number of ways to select r values from n numbers is over one million.

Answer: 4075
Execution Time: 0.02117 seconds
"""
import math
import time
start = time.time()

def chose(n, r):
    num = math.factorial(n)
    den = math.factorial(r)*math.factorial(n-r)
    return num/den

count = 0
for i in range(100, 22, -1):
    for j in range(i, 2, -1):
        val = chose(i, j)
        if val > 1000000: count += 1

print('There are %i r and n values that result in over 1,000,000 combinations.' % count)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))
