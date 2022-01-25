# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:30:16 2020

@author: nquist

This code solves Project Euler problem 2. The funtion finds the sum of the even
numbers in the fibonacci numbers that fall under the given number (num). In this
case we want numbers that are under 4 million.

Answer: 4613732
Execution Time: 0.00200 seconds
"""

import time
start = time.time()

def even_fib(num):
    val1 = 1
    val2 = 2
    sm = 0
    while val2 < num:
        sm += val2
        tmp = 3*val2 + 2*val1 # calculate the new even value
        val1 = 2*val2+val1
        val2 = 1*tmp
        print(val2)
    
    return sm

print(even_fib(4000000))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))
        