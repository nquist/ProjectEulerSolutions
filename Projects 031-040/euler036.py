# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 19:18:38 2022

@author: nquist
This solves project Euler problem 36. This finds the sum of all the numbers less
than one million that are palindromic in both base 10 and base 2.

Answer: 872187
[585585, 73737, 39993, 53235, 53835, 32223, 9009, 7447, 15351, 585, 313, 717, 99, 33, 9, 5, 7, 3, 1]
Execution Time: 0.01296 seconds
"""
import itertools
import time
start = time.time()

pals = []
max_binary = '11110100000000101111'
max_len = len(max_binary)//2 + len(max_binary)%2

def mirror_convert(string):
    full_bin = string + string[::-1]
    full_int_even = int(full_bin, 2)
    full_bin = string + string[-2::-1]
    full_int_odd = int(full_bin, 2)
    return str(full_int_even), str(full_int_odd)

def check_bin(int_str):
    for i in range(len(int_str)//2):
        rev_str = int_str[::-1]
        if rev_str[i] != int_str[i]:
            return False      
    return True

def viab_first(length):
    first_half_list = []
    for x in itertools.product(range(2), repeat=length-1):
        string = '1'
        for i in range(len(x)):
            string += str(x[i])
        first_half_list.append(string)
    
    return first_half_list

for i in range(max_len, 0, -1):
    curr_start = viab_first(i)    
    for j in range(0, len(curr_start)):
        ev, od = mirror_convert(curr_start[j])
        if check_bin(ev):
            pals.append(int(ev))
        if check_bin(od):
            pals.append(int(od))

print('The sum is %i.' % sum(pals))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

