# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:26:44 2022

@author: nquist
This solves project Euler problem 29. This finds all the unique values of the 
funtion a**b where 2 <= a <= 100 and 2 <= b <= 100.

Answer: 9183
Execution Time: 0.38801 seconds
"""

import time
start = time.time()

powers_list = []

for i in range(2, 101):
    for j in range(2, 101):
        power = i**j
        if power not in powers_list:
            powers_list.append(power)

print('There are %i distinct terms in the generated sequence.' % len(powers_list))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

