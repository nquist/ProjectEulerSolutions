# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 15:23:37 2022

@author: nquist
This solves project Euler problem 44. This finds the difference between two
pentagonal numbers (numbers that are generated by P(n) = n*(3n -1)/2) where
the sum is pentagonal and the difference is pentagonal.

Answer: 5482660
Execution Time: 26.99296 seconds
"""

import time
start = time.time()

def Pentag_number(indx):
    val = indx*(3*indx - 1)/2
    return int(val)

pent_nums = []
for i in range(1, 10000):
    new_num = Pentag_number(i)
    pent_nums.append(new_num)

pent_nums_set = set(pent_nums)
for i in range(1, len(pent_nums)):
    for j in range(i+1, len(pent_nums)):
        if (pent_nums[i] + pent_nums[j]) in pent_nums_set:
            if (pent_nums[j] - pent_nums[i]) in pent_nums_set:
                print(pent_nums[j], pent_nums[i], 'diff is ' + str(pent_nums[j]-pent_nums[i]))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))