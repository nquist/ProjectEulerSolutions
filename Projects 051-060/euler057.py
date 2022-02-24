# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 10:23:42 2022

@author: nquist
This solves project Euler problem 57. This finds the number of fractions where
the number of digits in the numerator is larger than the number of digits in the
denomenator for the series of fractions that can be used to approximate the 
square root of 2.

Answer: 153
Execution Time: 0.00500 seconds
"""
import time
start = time.time()

def find_fraction(curr_frac):
    new_denon = 2*curr_frac[1] + curr_frac[0]
    return [1*curr_frac[1], new_denon]

current_frac = [1,2]
longer_num = 0
for i in range(1000):
    current_frac = find_fraction(current_frac)
    temp_frac = [current_frac[0]+current_frac[1], current_frac[1]]
    if len(str(temp_frac[0])) > len(str(temp_frac[1])):
        longer_num += 1

print('There are %i numbers in the series where the numerator has more digits than the denominator.' % longer_num)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))
