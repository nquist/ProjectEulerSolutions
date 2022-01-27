# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 13:42:32 2022

@author: nquist
This solves project Euler problem 19. This finds the number of Sundays that fell
on the first of the month in the twentieth century.

Answer: 
Execution Time:  seconds


    IN PROGRESS ----- NOT COMPLETE
"""

import time
start = time.time()

months_norm = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
months_leap = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

start_day = 1 # 1 Jan 1900 was a Monday
curr_day = 1*start_day

for i in range(1, 12):
    curr_day = (curr_day+months_norm[i])%7
    print('For %i month the start day was %i' % (i+1, curr_day))


end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))