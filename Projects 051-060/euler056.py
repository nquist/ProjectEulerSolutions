# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:22:29 2022

@author: nquist
This solves project Euler problem 56. 

A googol (10^100) is a massive number: one followed by one-hundred 
zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the 
maximum digital sum?

Answer: 972
Execution Time: 0.22699 seconds
"""

import time
start = time.time()

def digit_sum(num):
    lst = list(str(num))
    lst = [int(i) for i in lst]
    return sum(lst)

def calc_power(a, b):
    val = a**b
    return digit_sum(val)

high_sum = 0
for i in range(2,101):
    for j in range(1, 101):
        temp_sum = calc_power(i, j)
        if temp_sum > high_sum:
            high_sum = 1*temp_sum

print('The highest value is %i' % high_sum)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))