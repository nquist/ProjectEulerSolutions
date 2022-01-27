# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 00:09:02 2022

@author: nquist
This solves project Euler problem 17. This finds the number of letters used in
the numbers from 1 to 1000 inclusive.

Answer: 21124
Execution Time: 0.00500 seconds
"""

import time
start = time.time()

ones = { 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',
           8:'eight', 9:'nine'}
teens = { 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
         16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
tens = {20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy',
        80:'eighty', 90:'ninety'}

def ones_change(num_str):    
    if num_str[-1] !='0':
        return(ones[int(num_str[-1])])
    else:
        return('')

def conv_num(num):
    num_str = str(num)
    num_word = ''
    
    if len(num_str) == 3:
        num_word = ones[int(num_str[0])] + 'hundred'
        if int(num_str[1:]) > 0:
            num_word = num_word + 'and'
    
    if len(num_str) >=2 and int(num_str[-2:]) > 9:
        if int(num_str[-2]) == 1:
            ten = int(num_str[-2:])
            num_word = num_word + teens[ten]
            num_str = num_str[:-1] +'0'
        else:
            ten = int(num_str[-2])*10
            num_word = num_word + tens[ten]
    
    temp_str = ones_change(num_str)
    num_word = num_word + temp_str

    return num_word

chars = 0
for i in range(1, 1000):
    string = conv_num(i)
    chars += len(string)

chars += len('onethousand')
print('The number of characters needed to write out the numbers from 1 to 1000 is %i' % chars)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))