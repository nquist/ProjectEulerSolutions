# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 16:06:01 2022

@author: nquist
This solves project Euler problem 55. This finds all the lychrel numbers (assuming
only 50 itterations are needed to determine if it is lychrel) that are less than
10,000.

Answer: 249
Execution Time: 0.08661 seconds
"""

import time
start = time.time()

max_val = 10000

def check_pal(num):
    if num == num[::-1]: return True
    return False

lychrel = []
for i in range(10, max_val):
    is_lychrel = True
    curr_val = str(i)
    for j in range(50):
        curr_val = str(int(curr_val) + int(curr_val[::-1]))
        if check_pal(curr_val):
            is_lychrel = False
            break
    if is_lychrel:
        lychrel.append(i)

print('There are %i lychrel numbers below 10,000.' % len(lychrel))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))
