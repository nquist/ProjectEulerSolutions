# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 19:55:18 2022

@author: nquist
This solves project Euler problem 14. This looks for the number lower than 
1 million that has the longest Collatz sequence.

Answer: 
Execution Time: 
    
    
    INCOMPLETE -- NO SOLUTION YET ------
"""
import time
start = time.time()

def num_even(num):
    return(num/2)
    
def num_odd(num):
    return((3*num)+1)
    
def Collatz_seq(num):
    curr_num = 1*num
    seq = [num]
    while curr_num > 1:
        if num%2 == 0:
            tmp = num_even(curr_num)
            seq.append(tmp)
            curr_num = 1*tmp
        else:
            tmp = num_odd(curr_num)
            seq.append(tmp)
            curr_num = 1*tmp

    return(seq)

coll_13 = Collatz_seq(13)
print(coll_13, len(coll_13))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))