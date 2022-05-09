# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:07:11 2022

@author: nquist
This solves project Euler problem 100. 

Answer: 
Execution Time:  seconds


    IN PROGRESS ----- NOT COMPLETE
"""
import numpy as np
import time
start = time.time()

def sqrt_fun(num):
    under = 2*num*num + 2*num +1
    return np.sqrt(under)

def p_trend(value):
    return 0.5512*np.exp(1.7776*value)

def p_refine(num):
    under = 2*num*num + 2*num +1
    return np.sqrt(under)

n = 1
trend_val = 0
while trend_val < 100000000000:
    trend_val = p_trend(n)
    n += 1
  

'''
def find_denom(start_val):
    i = 1*start_val
    if i % 2 == 0:
        i -= 1
    max_cap = start_val + 10000000
    while i < max_cap:
        squared_val = (i*(i-1)*2)+1
        base_val = int(np.sqrt(2)*(i-1))
        if base_val % 2 == 0:
            base_val -= 1
        high_val = int(1.5*(i-1))
        while (base_val*base_val <= squared_val) and (base_val <= high_val):
            if base_val*base_val == squared_val:
                return base_val
            else:
                base_val += 2
        i += 1
    return 0

curr_value = 1024740000000
for i in range(20):
    print(curr_value)
    blue_disks = int((1+find_denom(curr_value))/2)
    print('There should be %i blue disks.' % blue_disks)
    curr_value = curr_value + 10000000
    if blue_disks != 0 :
        break
'''
end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))
