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

length = 1
val = 1


def find_rec_cycle(num):
    leng = 1
    if num < 10:
        string = list(str(1/num)[2:])
    elif num < 100:
        string = list(str(1/num)[3:])
    else:
        string = list(str(1/num)[4:])
    print(string)
    for i in range(0, 10):
        counter = string.count(str(i))
        if counter > 1:
            pos_of_first = string.find(str(i))
            for i in range(counter+1):
                pos_of_next = string[pos_of_first+1:].find(str(i))
                diff = pos_of_next-pos_of_first
                if string[pos_of_first:pos_of_next] == string[pos_of_next:pos_of_next+diff]:
                    return(diff)
    
    return leng
    
for i in range(1, 11):
    if len(str(1/i)) > 18:
        temp_length = find_rec_cycle(i)
        if temp_length > length:
            length = 1*temp_length
            val = 1*i
        

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

