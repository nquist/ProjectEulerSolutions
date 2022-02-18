# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:31:10 2022

@author: nquist
This solves project Euler problem 18. This finds the maximum sum of the triangle,
if the sum is found by following a path from the top element down to the bottom.

Answer: 1074
Execution Time: 0.00000 seconds
"""
import numpy as np
import time
start = time.time()

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
    
pyramid = [[75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

for i in range(len(pyramid)-1, 0, -1):
    ret_row = reduce_rows(pyramid[i-1], pyramid[i])
    pyramid[i-1] = 1*ret_row
    pyramid = pyramid[:i]

print('The Maximum sum is %i.' % pyramid[0][0])

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

