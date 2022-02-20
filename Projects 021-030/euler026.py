# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 21:35:06 2022

@author: nquist
This solves project Euler problem 26. 

Answer: 
Execution Time:  seconds


    IN PROGRESS ----- NOT COMPLETE
"""

import time
start = time.time()

def find_rec_cycle(num):
    string = str(1/num)[2:]
    for i in range(0, 10):
        counter = string.count(str(i))
        if counter > 1:
            pos_of_first = string.find(str(i))
            for i in range(counter+1):
                pos_of_next = string[pos_of_first+1:].find(str(i))
                diff = pos_of_next-pos_of_first
                if string[pos_of_first:pos_of_next] == string[pos_of_next:pos_of_next+diff]:
                    return(diff)
    
    return 'No'
    
'''
lst = []
for i in range(2, 102):
    lst.append(1/i)
    print(i, len(str(10/i)))'''
    
for i in range(11, 20):
    val = find_rec_cycle(i)
    if val == 'No':
        print('%.10f doesn\'t repeat.' % (1/i))
    else:
        print(val)
        print(1/i)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

