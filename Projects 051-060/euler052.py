# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 20:27:00 2022

@author: nquist
This solves project Euler problem 52. 

It can be seen that the number, 125874, and its double, 251748, contain exactly 
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2*x, 3*x, 4*x, 5*x, and 6*x, 
contain the same digits.

Answer: 142857
Execution Time: 0.88190 seconds
"""

import time
start = time.time()

def check_digits(nums_list):
    vals_set = []
    for nums in nums_list:
        temp = list(nums)
        temp.sort()
        if len(vals_set) == 0:
            vals_set = 1*temp
        elif vals_set != temp:
            return False
    return True

def num_list(number, high_multi):
    values = [str(number)]
    for i in range(2, high_multi+1):
        values.append(str(i*number))
    return values

multi_num_list = []
for i in range(1, 200000):
    num_lst = num_list(i, 6)
    if check_digits(num_lst):
        multi_num_list.append(i)
        
print('The lowest number is %i' % min(multi_num_list))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))