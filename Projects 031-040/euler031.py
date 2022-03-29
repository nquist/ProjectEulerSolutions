# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 12:30:17 2022

@author: nquist
This solves project Euler problem 31. 

In the United Kingdom the currency is made up of pound (£) and pence (p). There 
are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:
    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

Answer: 73682
Execution Time: 0.01000 seconds
"""

import time
start = time.time()

c_values = [200, 100, 50, 20, 10, 5, 2, 1]

def choices(curr_idx, curr_max):
    new_count = 0
    mx_count = curr_max//c_values[curr_idx]
    curr_list = [x for x in range(mx_count+1)]
    if curr_idx == (len(c_values)-2):
        return len(curr_list)
    else:
        for i in curr_list[::-1]:
            new_max = curr_max-i*c_values[curr_idx]
            if curr_max == 0:
                return 1
            else:
                new_count += choices(curr_idx+1, new_max)
        return new_count

trial = choices(0, 200) 

print('There are %i combinations' % trial)   

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))