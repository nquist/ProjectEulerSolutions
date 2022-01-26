# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 23:32:59 2022

@author: nquist


This solves project Euler problem 16. This finds the sum of the digits of 2^1000.

Answer: 1366
Execution Time: 0.00100 seconds
"""

import time
start = time.time()

power_val = str(2**1000)
print(power_val)

power_sum = 0
for i in range(len(power_val)):
    power_sum += int(power_val[i])
    

print('The sum of the digits of 2^1000 is %i.' % power_sum)


end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

