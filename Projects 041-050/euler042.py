# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 14:44:22 2022

@author: nquist
This solves project Euler problem 42. This calculates the value of each word
in p042_words.txt by summing the value of each character (where a = 1, b = 2, ....).
It then finds how many of these words have sums that are triagle numbers.

Answer: 162
Execution Time: 0.00600 seconds
"""
import numpy as np
import time
start = time.time()


def tri_nums(max_value):
    n_term = -0.5 + 0.5*np.sqrt(1+8*max_value)
    tri_list = []
    for i in range(1, int(n_term)+1):
        tri_list.append(int(0.5*i*(i+1)))
    return tri_list

f = open('p042_words.txt', 'r')
txt = f.readline()
txt = txt.replace('"', '').lower()
txt_lst = txt.split(',')
max_length = 0

for i in txt_lst:
    if len(i) > max_length:
        max_length = 1*len(i)
        
max_tri = 26*max_length
tri_list = tri_nums(max_tri)
word_count = 0

for i in txt_lst:
    word_sum = sum([ord(char)-96 for char in i])
    if word_sum in tri_list:
        word_count += 1
 
print('The number of words that are triangle words %i.' % word_count)
    
end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

