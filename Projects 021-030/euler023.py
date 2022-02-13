# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 22:24:09 2022

@author: nquist
This solves project Euler problem 23. 

Answer: 4179871
Execution Time: 1140.55349 seconds
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
    for i in range(12, mx+1):
        divs = proper_divisors(i)
        if sum(divs) > i:
            abun_list.append(i)
            
    return abun_list

lst = find_abundant_nums(28111)
numbers = list(range(1, 28123))
for i in range(len(lst)):
    for j in range(len(lst)):
        sm = lst[i]+lst[j]
        if sm > 28123:
            break
        elif sm in numbers:
            numbers.remove(sm)

print('The sum of the sum of positive integers which cannot be written as the sum of ' +
      'two abundant numbers is %i.' % sum(numbers))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))
