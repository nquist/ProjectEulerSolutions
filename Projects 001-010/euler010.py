# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:05:53 2020

@author: nquist
This solves project Euler problem 10. This finds the sum of the primes that are
2 million. 

Answer: 142913828922
Execution Time: 4937.39619 seconds
"""

import time
start = time.time()

def is_prime(num):
    for i in range(5, (num//2)+1, 2):
        if num%i == 0:
            return False
    return True

temp_num = 13
curr_num = 15
sm = 2+3+5+7+11+13
perc = 0
print('{:.2%}'.format(perc))
while curr_num < 1000000:
    if curr_num%3 != 0:
        prme = is_prime(curr_num)
        if prme:
            sm += curr_num
            temp_num = 1*curr_num
    curr_num += 2
    if curr_num/2000000 > perc + .1:
        perc = 1*(curr_num/2000000)
        print('{:.2%}'.format(perc))

print(sm, temp_num)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))