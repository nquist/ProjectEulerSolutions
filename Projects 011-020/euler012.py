# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 12:36:27 2020

@author: nquist

This solves project Euler problem 12. This looks for the first triangle number
that has over five hundred divisors.

Answer: 76576500
Execution Time: 6.97690 seconds
"""
import numpy as np
import time
start = time.time()

def triangle_number(n):
    return(0.5*n*(n+1))
    
def num_proper_divisors(num):
    div_list = [1, num]
    num_root = np.sqrt(num)
    for i in range(2, int(round(num_root))+1):
        if num%i == 0:
            div_list.append(i)
            if num//i != i:
                div_list.append(num//i)    
    return len(div_list)
    
num_div = 0   
tri_index = 1
while num_div <= 500:
    tri_index += 1
    tri_num = triangle_number(tri_index)
    num_div = num_proper_divisors(tri_num)
    
print('The %.0fth triangle number is %i with %i proper divisors.' % (tri_index, tri_num, num_div))
    
end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

