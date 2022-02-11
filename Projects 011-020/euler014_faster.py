# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 19:55:18 2022

@author: nquist
This solves project Euler problem 14. This looks for the number lower than 
1 million that has the longest Collatz sequence.

Answer: 837799 (chain of 525)
Execution Time: 5.06631 seconds
"""
import time
start = time.time()

def num_even(num):
    val = num/2
    return(val)
    
def num_odd(num):
    val = (3*num+1)/2
    return(val)
    
def Collatz_seq(dic, num):
    curr_num = 1*num
    seq = [num]
    while curr_num > 1:
        if curr_num in dic:
            return seq
        else:
            if curr_num%2 == 0:
                tmp = num_even(curr_num)
                seq.append(tmp)
                curr_num = 1*tmp
            else:
                tmp = num_odd(curr_num)
                seq.append(tmp*2)
                seq.append(tmp)
                curr_num = 1*tmp

    return(seq)

top_range = 999999
dic = {}
for i in range(top_range, 0, -1):
    if i not in dic:
        curr_list = Collatz_seq(dic, i)
        if curr_list[-1] != 1:
            off_set = dic[curr_list[-1]]-1
        else:
            off_set = 0
        for j in range(len(curr_list)):
            if curr_list[j] <= top_range:
                dic[curr_list[j]] = len(curr_list)-j+off_set

#print(dic)
max_chain = max(dic.values())
max_key = max(dic, key=dic.get)
print(max_chain)
print(max_key)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))