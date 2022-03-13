# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:11:38 2022

@author: nquist
This solves project Euler problem 48. 

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

Answer: 9110846700
Execution Time: 0.23862 seconds
"""

import time
start = time.time()

power_sum = 0
for i in range(1, 1001):
    val = i**i
    if len(str(val)) > 10:
        temp = str(val)[-10:]
        power_sum += int(temp)
    else:
        power_sum += val
        
print('The last 10 digits are %s.' % (str(power_sum)[-10:]))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))