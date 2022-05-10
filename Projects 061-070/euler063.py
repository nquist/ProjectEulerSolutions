# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:30:55 2022

@author: nquist
This solves project Euler problem 63. 


The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit 
number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

Answer: 49
Execution Time: 0.00130 seconds
"""

import time
start = time.time()

base = 2
counter = 0

for i in range(1, 11):
    loop = True
    power = len(str(i))
    while loop:
        if len(str(i**power)) == power:
            #print(i, power, i**power)
            counter += 1
        else:
            loop = False
        power += 1

print('There are %i numbers.' % counter)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))