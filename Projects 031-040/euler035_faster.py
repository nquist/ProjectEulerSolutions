# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 15:17:40 2022

@author: nquist
This solves project Euler problem 35. This finds number of circular primes
below one million.

Answer: 55
Execution Time: 401.79534 seconds
"""
import numpy as np
import time
start = time.time()


max_val = 1000000
full_set_list = set(range(3,max_val,2))
Primes = [2]

while min(full_set_list)<int(np.sqrt(max_val)):
    curr_val = min(full_set_list)
    Primes.append(curr_val)
    temp_set = set(range(curr_val*curr_val, max_val, 2*curr_val))
    temp_set.add(curr_val)
    full_set_list = set(full_set_list).difference(temp_set)
'''    
max_val = 1000000
full_set_list = list(range(3,max_val,2))
Primes = [2]

while min(full_set_list)<int(np.sqrt(max_val)):
    curr_val = min(full_set_list)
    Primes.append(curr_val)
    temp_set = list(range(curr_val*curr_val, max_val, 2*curr_val))
    temp_set.append(curr_val)
    full_set_list = full_set_list - temp_set
    '''

Primes = set(Primes[5:]).union(full_set_list)
#Primes = Primes[5:]

#Primes = Primes[5:] + list(full_set_list)
circ_Primes = set([2, 3, 5, 7, 11])

while len(Primes) > 0:
    circs = set([min(Primes)])
    str_val = str(min(Primes))
    #Primes.remove(min(Primes))
    #is_circ = True
    new_val = str_val +''
    for i in range(len(str_val)-1):
        new_val = new_val[1:] + new_val[0]
        circs.add(int(new_val))
    if circs.issubset(Primes):
        circ_Primes = circ_Primes.union(circs)
        Primes = Primes.difference(circs)
    else:
        Primes = Primes.difference(circs)
        
    #    if int(new_val) in Primes:
        #if (int(new_val) not in circs) and (int(new_val) in Primes):
     #       circs.add(int(new_val))
      #      Primes.remove(int(new_val))
       # else:
        #    is_circ = False 
    #if is_circ:
     #   circ_Primes = circ_Primes.union(circs)
    
        
print("The number of circular primes lower than one million is %i." % len(circ_Primes))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))


