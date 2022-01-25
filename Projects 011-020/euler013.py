# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 12:36:27 2022

@author: nquist

This solves project Euler problem 13. This looks for the first ten digits of 
100 fifty diget numbers in the text file.

In order to keep all the digets and add them together, I broke each number into
five 10 diget strings and then added each group of ten diget numbers and made
sure to keep track of the carry over value. 

Total sum: 5537376230390876637302048746832985971773659831892672
Answer: 5537376230
Execution Time: 0.00199 seconds
"""
import time
start = time.time()

lines = []

f = open('problem013.txt', 'r')
sum_value = []

for line in f.readlines():
    l = line.strip()
    lines.append([l[:10], l[10:20], l[20:30], l[30:40], l[40:]])

carry_over = 0
for i in range(5):
    sm = 0 + carry_over
    for j in range(100):
        sm += int(lines[j][4-i])
    if len(str(sm))>10:
        sum_value = [str(sm)[-10:]] + sum_value
        carry_over = int(str(sm)[:-10])
    
sum_value = [str(carry_over)] + sum_value
total_sum = sum_value[0] + sum_value[1] + sum_value[2] + sum_value[3] + sum_value[4] + sum_value[5]
print('The total sum is ' + total_sum + ' and the first ten digets are ' + total_sum[:10] +'.')

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))