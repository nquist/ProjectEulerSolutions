# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 16:25:59 2022

@author: nquist
This solves project Euler problem 21. This finds the sum of all the amicable
numbers under 10000.

An amicalbe pair is two numbers where the second number is the sum of the 
proper divisors of the first number and vice versa.

Answer: 31626
Execution Time: 0.15100 seconds
"""
import numpy as np
import time
start = time.time()

def proper_divisors(num):
    div_list = [1]
    num_root = np.sqrt(num)
    for i in range(2, int(round(num_root))+1):
        if num%i == 0:
            div_list.append(i)
            div_list.append(int(num/i))    
    return div_list


max_num = 10000
num_list = list(range(20, max_num))
pair_list = []
while len(num_list) > 0:
    num_div_sum = sum(proper_divisors(num_list[0]))
    if num_div_sum == 1 or num_div_sum < num_list[0] or num_div_sum > max_num or num_div_sum == num_list[0]:
        num_list.pop(0)
    else:
        pos_pair_sum = sum(proper_divisors(num_div_sum))
        if pos_pair_sum == num_list[0]:
            pair_list.append(num_div_sum+pos_pair_sum)
            num_list.remove(pos_pair_sum)
        num_list.pop(0)

print('The sum of the amicable pairs under 10,000 is %i.' % sum(pair_list))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

