# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 23:45:05 2022

@author: nquist
This solves project Euler problem 59. 

Answer: 
Execution Time:  seconds


    IN PROGRESS ----- NOT COMPLETE
"""

import time
start = time.time()

f = open('p059_cipher.txt', 'r')
vals = f.readlines()[0].split(',')

word_list = []
for i in range(97, 123):
    for j in range(97, 123):
        for k in range(97, 123):
            words = ''
            for l in range(0, 5):
                words += chr(int(vals[3*l])^i)+chr(int(vals[3*l+1])^j)+chr(int(vals[3*l+2])^k)
            word_list.append(words)



end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))