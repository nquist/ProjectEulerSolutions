# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 23:20:58 2022

@author: nquist
This solves project Euler problem 34. This finds the sum of all the numbers which
are the sum of the factorial of each of it's digits.

Answer: 40730 [145, 40585]
Execution Time: 1.34499 seconds
"""
import math
import time
start = time.time()

digit_list = []

# Max number is 409113 because this is the sum of 1-9, inclusive, factorial 
for i in range(11, 409113):
    num_sum = 0
    num_str = str(i)
    for j in range(len(num_str)):
        num_sum += math.factorial(int(num_str[j]))
    
    if num_sum == i:
        digit_list.append(i)

print('The sum is $i.' % sum(digit_list))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

