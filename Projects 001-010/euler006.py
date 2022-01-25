# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:17:38 2020

@author: nquist

This is the soultion for Project Euler problem 6. The function finds the 
difference between the sum of a^2 + b^2 + .... and the square of (a + b + ...).
Mathematically, this is the sum of 2*a*b + 2*a*c + 2*b*c +....
The problem asks for the difference of the numbers between 1 and 100.
"""

import numpy as np

def sum_square_diff(low, high):
    diff = 0
    vals = list(np.arange(low, high+1))
    for i in range(len(vals)-1):
        for j in range(i+1, len(vals)):
            diff = diff + 2*vals[i]*vals[j]
    return diff

print(sum_square_diff(1,100))