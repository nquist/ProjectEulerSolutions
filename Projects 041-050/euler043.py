# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 19:46:42 2022

@author: nquist
This solves project Euler problem 43. This finds the sum of the pandigital numbers
that satisfy the condition that, assuming the number is d_1 d_2 d_3 d_4 d_5 d_6 d_7 d_8 d_9 d_10,
then 

d_2 d_3 d_4 is divisible by 2
d_3 d_4 d_5 is divisible by 3
d_4 d_5 d_6 is divisible by 5
d_5 d_6 d_7 is divisible by 7
d_6 d_7 d_8 is divisible by 11
d_7 d_8 d_9 is divisible by 13
d_8 d_9 d_10 is divisible by 17

Answer: 16695334890
Execution Time: 19.66131 seconds
"""
import itertools
import time
start = time.time()

divisors = [2, 3, 5, 7, 11, 13, 17]

def all_pandigitals(num):
    perms = itertools.permutations(range(0, num+1))
    perms_list = []
    for vals in perms:
        string = ''
        for j in range(len(vals)):
            string += str(vals[j])
        perms_list.append(string)
    
    return perms_list

pans_09 = all_pandigitals(9)
pans_divis = []
for j in pans_09:
    append = True
    for k in range(len(divisors)):
        if int(j[k+1:k+4])%divisors[k] != 0:
            #print('%s is not divsabile by %i.' % (j[k+1:k+4], divisors[k]))
            append = False
            break
    if append: pans_divis.append(int(j))

print('The sum of the pandigital numbers 0-9 that satisfy this condition is %i' % sum(pans_divis))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))


