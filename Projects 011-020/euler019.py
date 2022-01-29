# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 13:42:32 2022

@author: nquist
This solves project Euler problem 19. This finds the number of Sundays that fell
on the first of the month in the twentieth century.

Answer: 171
Execution Time: 0.00300 seconds
"""

import time
start = time.time()

months_norm = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
months_leap = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

start_day = (1 + 365)%7 # 1 Jan 1900 was a Monday plus a full year to find the day of the
# week for 1 Jan 1901
curr_day = 1*start_day
sun_days = 0

for j in range(1901, 2001):
    if j != 1901:
        curr_day = (curr_day+months_norm[12])%7
        if curr_day == 0: sun_days +=1
    if j%4 == 0:
        for i in range(1, 12):
            curr_day = (curr_day+months_leap[i])%7
            if curr_day == 0: sun_days +=1
    else:
        for i in range(1, 12):
            curr_day = (curr_day+months_norm[i])%7
            if curr_day == 0: sun_days +=1
    
print('There are %i first days of the month that fall on sundays between 1 Jan 1901 and 31 Dec 2000.' %sun_days)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))