# -*- coding: utf-8 -*-
"""
Created on Mon May  9 09:59:55 2022

@author: nquist
This solves project Euler problem 62. 

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube 
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are 
cube.

Answer: 127035954683
Execution Time: 0.01561 seconds
"""

import time
start = time.time()

def find_cube_str(num):
    val = num**3
    val_new = list(str(val))
    val_new.sort()
    return ''.join(val_new)

max_count = 5
loop = True
counter = 5
cube_dic = {}
while loop:
    num_string = find_cube_str(counter)
    if num_string in cube_dic:
        if len(cube_dic[num_string]) == (max_count - 1):
            loop = False
            small_val = min(cube_dic[num_string])
            print('The smallest cube is %i' % small_val**3)
        else:
            temp_list = cube_dic[num_string]
            temp_list.append(counter)
            cube_dic[num_string] = temp_list
    else:
        cube_dic[num_string] = [counter]
    counter += 1
    if counter > 10000:
        loop = False

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

