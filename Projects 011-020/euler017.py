# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 00:09:02 2022

@author: nquist
This solves project Euler problem 17. This finds the number of letters used in
the numbers from 1 to 1000 inclusive.

Answer:
Execution Time:  seconds


    INCOMPLE---- HAVE NOT FINISHED SOLUTION
"""

import time
start = time.time()

ones = { 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',
           8:'eight', 9:'nine'}
teens = { 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
         16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
tens = {20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy',
        80:'eighty', 90:'ninety'}

def ones_change(num):
    num_str = str(num)
    
    if num_str[-1] !=0:
        return(ones[int(num_str[-1])], num_str[:-1] + '0')
    else:
        return('', num_str)

def conv_num(num):
    num_str = str(num)
    num_word = ''
    
    temp_str, num_str = ones_change(num_str)
    
    num_word = num_word + temp_str
    
    #if len()
    
    print(num_str)
    return num_word

print(conv_num(7))
print(conv_num(23))
print(conv_num(135))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))