# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 21:35:06 2022

@author: nquist
This solves project Euler problem 26. 

Answer: 
Execution Time:  seconds


    IN PROGRESS ----- NOT COMPLETE
"""

import time
start = time.time()

lst = []
for i in range(2, 102):
    lst.append(1/i)
    print(i, len(str(10/i)))


end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

