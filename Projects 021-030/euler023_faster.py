# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:05:40 2022

@author: nquist
This solves project Euler problem 23. 

Answer: 4179871
Execution Time:  seconds
"""
import numpy as np
import time
start = time.time()

def proper_divisors(num):
    lst = [1]
    for i in range(2, int(np.sqrt(num))+1):
        if num%i == 0:
            lst.append(i)
            lst.append(num//i)
    
    return list(set(lst))

def find_abundant_nums(mx):
    abun_list = []
    tws = list(range(12, mx, 2))
    threes = list(range(12, mx, 3))
    starting_list = list(set(tws+threes))
    for i in range(len(starting_list)):
        divs = proper_divisors(starting_list[i])
        if sum(divs) > starting_list[i]:
            abun_list.append(starting_list[i])
    return abun_list

lst = find_abundant_nums(28111)
abun_sums = []
'''numbers = list(range(1, 28123))'''
'''for i in range(len(lst)):
    for j in range(len(lst)):
        sm = lst[i]+lst[j]
        if sm > 28123:
            break
        elif sm not in abun_sums:
            abun_sums.append(sm)'''

'''
print('The sum of the sum of positive integers which cannot be written as the sum of' +
      'two abundant numbers is %i.' % sum(numbers))
'''
#print(abun_sums)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

