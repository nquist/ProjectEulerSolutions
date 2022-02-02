# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 16:42:13 2022

@author: nquist
This solves project Euler problem 28. 

Answer: 669171001
Execution Time: 0.00100 seconds
"""

import time
start = time.time()

total_sum = 1
curr_num = 1

for i in range(2, 1001, 2):
    for j in range(0, 4):
        curr_num += i
        total_sum += curr_num

print('The sum of the diagonals of a 1,001 by 1,001 spiral is %i' % total_sum)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

