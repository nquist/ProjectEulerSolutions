# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 20:48:11 2022

@author: nquist
This solves project Euler problem 15. This finds all the possible paths through
a 20x20 grid from the top left corner to the bottome right corner. To solve
this, I represented each right step as a 1 and each down step as a 0. Thus, we
can use permutation of multisets.

Answer: 137846528820
Execution Time: 0.00000 seconds
"""
import math
import time
start = time.time()

Total_length = 40
num_ones = 20
num_zeros = 20

num_perms = math.factorial(Total_length)/(math.factorial(num_ones)*math.factorial(num_zeros))
print('The number of paths in an 20x20 grid is %i' % num_perms)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

