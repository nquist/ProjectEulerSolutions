# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 21:35:06 2022

@author: nquist
This solves project Euler problem 26. 

A unit fraction contains 1 in the numerator. The decimal representation of the 
unit fractions with denominators 2 to 10 are given:

1/2= 0.5            1/3= 0.(3)          1/4= 0.25
1/5= 0.2            1/6= 0.1(6)         1/7= 0.(142857)
1/8= 0.125          1/9= 0.(1)          1/10= 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be 
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle 
in its decimal fraction part.

Answer: 983
Execution Time: 2.61026 seconds
"""

import time
start = time.time()

def recy(num, denom):
    for i in range(1, denom+1):
        if (num*(10**i-1))%denom == 0:
            return i
    return 0
        
repeating_vals = []
    
for i in range(1, 1001):
    if len(str(1/i)) >= 18:
        repeating_vals.append(i)

vals_dic = {}
for j in repeating_vals:
    repeat_len = 0
    remain = 1
    while repeat_len == 0:
        repeat_len = recy(remain, j)
        if repeat_len != 0:
            vals_dic[j] = repeat_len
        else:
            remain = (remain%j)*10

print('The max length is %i' % max(vals_dic, key=vals_dic.get))
        

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

