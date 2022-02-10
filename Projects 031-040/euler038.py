# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 17:14:23 2022

@author: nquist
This solves project Euler problem 38. This finds the largest 1 to 9 pandigital
9-digit number that can be formed as the concatenated product of an integer with
(1, 2, ...., n) where n > 1?

Answer: 932718654
Execution Time: 0.02843 seconds
"""

import time
start = time.time()

#multipliers = list(range(2,10))
pans = {1:123456789}

for i in range(3, 10000):
    lst = [char for char in str(i)]
    lst_set = set(lst)
    if (len(lst) == len(lst_set)) and ('0' not in lst_set):
        for j in range(2,10):
           prod = str(j*i)
           temp_list = {char for char in prod}
           if (len(lst_set.intersection(temp_list)) != 0) or ('0' in temp_list):
               break
           else:
               lst_set = lst_set.union(temp_list)
               if len(lst_set) == 9:
                   string = ''
                   for k in range(1, j+1):
                       string += str(k*i)
                   pans[i]= int(string)

print('The largest 1 to 9 pandigital number that is formed from a ' + 
      'concatenated product is %i.' % pans[max(pans)])                   

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

