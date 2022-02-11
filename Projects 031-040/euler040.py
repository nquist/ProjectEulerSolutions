# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 14:09:11 2022

@author: nquist
This solves project Euler problem 40. This finds the product of the first, 10th,
100th, 1,000th, 10,000th, 100,000th and 1,000,000th digit of the irrational
decimal that is made by concatenation the positive integers.

Answer: 210
Execution Time: 0.18286 seconds
"""

import time
start = time.time()

current_num = 1
tens_count = 0
tens_find = [9, 99, 999, 9999, 99999]
selected_digits = [1,1]
curr_string = ""

while len(selected_digits) < 7:
    if len(curr_string) < 10:
        for i in range(20):
            curr_string += str(current_num)
            current_num += 1
    elif tens_count in tens_find:
        selected_digits.append(int(curr_string[9]))
        curr_string = curr_string[10:]
        tens_count += 1
    else:
        curr_string = curr_string[10:]
        tens_count += 1

product = 1
for i in range(len(selected_digits)):
    product = product*selected_digits[i]

print('The product of the first, 10th, 100th, 1,000th, 10,000th, 100,000th '+
      'and 1,000,000th digit of the irrational decimal is %i' % product)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))


