# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 23:44:54 2022

@author: nquist

This solves project Euler problem 20. This finds the sum of the digits of 100!

Answer: 648
Execution Time: 0.00000 seconds
"""
import math
import time
start = time.time()

fac_val = str(math.factorial(100))
print(fac_val)

fac_sum = 0
for i in range(len(fac_val)):
    fac_sum += int(fac_val[i])
    

print('The sum of the digits of 100! is %i.' % fac_sum)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))