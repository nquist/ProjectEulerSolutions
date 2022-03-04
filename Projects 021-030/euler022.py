# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 17:00:27 2022

@author: nquist
This solves project Euler problem 22. This finds the sum of all the name scores
from the file 'names.txt'. Each name score is calculated by finding the product
of position value of the name in the alphabetial list multiplied by the sum
of the value of each letter in the name.

Answer: 871198282
Execution Time: 0.02499 seconds
"""
import time
start = time.time()

list_sum = 0

f = open('names.txt', 'r')
names = f.readlines()
f.close()
names = names[0].replace('"', '').split(',')
names.sort()

for i in range(len(names)):
    char_sum = 0
    for j in names[i]:
        char_sum += ord(j)-64
    list_sum += (i+1)*char_sum    
    
print('The total name score of the file is %i' % list_sum)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

