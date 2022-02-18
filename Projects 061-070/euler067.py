# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 14:12:58 2022

@author: nquist
This solves project Euler problem 67. This finds the maximum sum of the triangle,
found in p067_triangle.txt, if the sum is found by following a path from the 
top element down to the bottom.

Answer: 7273
Execution Time: 0.08700 seconds
"""
import numpy as np
import time
start = time.time()

f = open("p067_triangle.txt", "r")
lst = list(f.readlines())
curr_row = lst[-1].split()
curr_row = list(map(int, curr_row))

def reduce_rows(list_short, list_long):
    new_list = []
    if (len(list_long) - len(list_short)) != 1:
        return [0]
    else:
        for i in range(len(list_short)):
            first_sum = list_short[i] + list_long[i]
            second_sum = list_short[i] + list_long[i+1]
            if first_sum > second_sum:
                new_list.append(first_sum)
            else:
                new_list.append(second_sum)
        return new_list

for i in range(len(lst)-2, -1, -1):
    short_row = lst[i].split()
    short_row = list(map(int, short_row))
    ret_row = reduce_rows(short_row, curr_row)
    curr_row = 1*ret_row

print('The Maximum sum is %i.' % curr_row[0])

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))


