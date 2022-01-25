# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:05:53 2020

@author: nquist

This solves project Euler problem 7. This looks for the 10001st prime number.

Answer: 104743
Execution Time: 16.78110 seconds
"""

import time
start = time.time()

def is_prime(num):
    for i in range(5, (num//2)+1, 2):
        if num%i == 0:
            return False
    return True

count = 6
temp_num = 13
curr_num = 13
while count < 10001:
    curr_num += 2
    if curr_num%3 != 0:
        prme = is_prime(curr_num)
        if prme:
            count += 1
            temp_num = 1*curr_num

print(count, temp_num)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))