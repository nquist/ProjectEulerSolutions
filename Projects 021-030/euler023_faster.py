# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:05:40 2022

@author: nquist
This solves project Euler problem 23. 

Answer: 4179871
Execution Time: 10.52426 seconds
"""
import numpy as np
import time
start = time.time()

def find_abundant_nums(mx):
    abun_dic = dict.fromkeys(range(2,mx+1), 1)
    for i in abun_dic:
        #if i == 1:
        for k in [i*n for n in range(2, int(mx/i)+1)]:
            if i != k: abun_dic[k] += i
    return [j for j in abun_dic if abun_dic[j]>j]


lst = find_abundant_nums(28123)
abun_sums = set() # This is what eventually cut my time, using set instead of list
for i in range(len(lst)):
    for j in range(i, len(lst)):
        sm = lst[i]+lst[j]
        if sm > 28123:
            break
        else:
            abun_sums.add(sm)

non_abun_sum = sum([ p for p in range(28123) if p not in abun_sums])

print('The sum of the sum of positive integers which cannot be written as the sum of ' +
      'two abundant numbers is %i.' % non_abun_sum)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

