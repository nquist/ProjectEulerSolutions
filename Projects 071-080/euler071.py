# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 15:43:07 2022

@author: nquist
This solves project Euler problem 71. This finds the numerator of the proper
fraction just smaller than 3/7 for proper fractions with denomerators less than
1,000,000

Answer: 
Execution Time:  seconds


    IN PROGRESS ----- NOT COMPLETE
"""
import time
start = time.time()

curr_frac = 2/5
frac_upper = 3/7
#frac_lower = 2/5

for i in range(1000000, 9, -1):
    val = int(i*frac_upper)
    
    


end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))
