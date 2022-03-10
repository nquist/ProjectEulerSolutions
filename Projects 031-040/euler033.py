# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 19:16:51 2022

@author: nquist
This solves project Euler problem 33. 

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is 
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than 
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.

Answer: 100
Execution Time: 0.01425 seconds
"""
import time
start = time.time()

def new_frac(num, denom):
    if num[0] in denom:
        denom = denom.replace(num[0], '')
        if len(denom) == 0: denom = num[0]
        num = num[1]
        return num, denom
    elif num[1] in denom:
        denom = denom.replace(num[1], '')
        if len(denom) == 0: denom = num[1]
        num = num[0]
        return num, denom
    else:
        return num, denom

frac_list = []
for i in range(11, 100):
    if i%10 !=0:
        for j in range(i+1, 100):
            if j%10 != 0:
                temp = set(list(str(i))).intersection(set(list(str(j))))
                if len(temp) == 1:
                    num, denom = new_frac(str(i), str(j))
                    if i/j == int(num)/int(denom):
                        frac_list.append([num, denom])
num = 1
denom = 1
for i in frac_list:
    num = num*int(i[0])
    denom = denom*int(i[1])

counter = 1*num
while counter > 1:
    if num%counter == 0 and denom%counter == 0:
        num = num//counter
        denom = denom//counter
    counter -= 1

print('The denomenator is %i' % denom)
                    

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))
