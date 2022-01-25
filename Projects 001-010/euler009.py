# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 19:54:29 2020

@author: nquist

This solves project euler problem 9, which looks for the pathagorean triplet
which sums to 1000 and prints the product of the pathagorean triplet.
"""

import numpy as np

missing = True
i = 1
while missing:
    a = ((1000**2)-2000*i)/(2000-2*i)
    a_int = ((1000**2)-2000*i)//(2000-2*i)
    if a-a_int == 0:
        c = np.sqrt(a**2 + i**2)
        c_other = 1000 - i - a
        print(a*i*c)
        print(a*i*c_other)
        missing = False
    if i >1000:
        print('No value found')
        missing = False
    i+=1
