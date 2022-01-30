# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 17:11:31 2022

@author: nquist
This solves project Euler problem 24. This finds the 1,000,000 number of the
permutations of integers 0 through 9, inclusive, in lexicographic order.

Answer: 2783915460
Execution Time: 0.00100 seconds
"""
import math
import time
start = time.time()

goal = 1000000
val = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
test = 1
num_str = ''

while test < goal:
    div = (goal-test)//math.factorial(len(val)-1)
    test += div*math.factorial(len(val)-1)
    num_str = num_str + val[div]
    val.pop(div)

num_str = num_str + val[0]

print('The 1,000,000 lexicographic permuation of integers 0 through 9 inclusive is %s' % num_str)


end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

