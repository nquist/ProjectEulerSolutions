# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 17:50:57 2022

@author: nquist
This solves project Euler problem 30. This finds the sum of the numbers in which
the sum of each digit in the number to the fifth power is equal to the number.

Answer: 443839
Execution Time: 7.52332 seconds
"""

import time
start = time.time()

def check_power(num, power):
    string = str(num)
    power_sum = 0
    for i in string:
        power_sum += int(i)**power
    
    if num == power_sum: return True
    else: return False

vals = []
for i in range(22, 1000000):
    if check_power(i, 5):
        vals.append(i)

print('The sum is %i' % sum(vals))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

