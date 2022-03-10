# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 13:00:11 2022

@author: nquist
This solves project Euler problem 39. 

If p is the perimeter of a right angle triangle with integral length sides, 
{a, b, c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

Answer: 840
Execution Time: 0.27086 seconds
"""
import numpy as np
import time
start = time.time()

def find_squares(max_val):
    squares_set = {1}
    counter = 2
    curr_val = 1
    while curr_val < max_val:
        curr_val = counter**2
        if curr_val <= max_val:
            squares_set.add(curr_val)
        counter +=1
    
    return squares_set

squares_set = find_squares(996003)
squares_list = list(squares_set)
squares_list.sort()

combo_list = []
p_dic = {}
for i in range(len(squares_list)-1):
    for j in range(i+1, len(squares_list)):
        side_sum = squares_list[i] + squares_list[j]
        if side_sum in squares_set:
            p = int(np.sqrt(squares_list[i])+np.sqrt(squares_list[j])+np.sqrt(side_sum))
            if p < 1000:
                combo_list.append({np.sqrt(squares_list[i]), np.sqrt(squares_list[j]), np.sqrt(side_sum)})
                if p in p_dic:
                    p_dic[p] = p_dic[p] + 1
                else:
                    p_dic[p] = 1

max_key = max(p_dic, key=p_dic.get)

print('The perimeter with the most solutions is %i' % max_key)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

