# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 12:36:27 2020

@author: nquist

This solves project Euler problem 12. This looks for the first triangle number
that has over five hundred divisors.

Answer:
    
    
    INCOMPLE---- HAVE NOT FINISHED SOLUTION
"""

import time
start = time.time()


def triangle_number(n):
    return(0.5*n*(n+1))
    
    
for i in range(10):
    print('The %.0fth triangle number is %.0f.' % (i, triangle_number(i)))
    
    
end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

