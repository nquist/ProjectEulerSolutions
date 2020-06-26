# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:12:29 2020

@author: nquist

This code solves Project Euler problem 4. The function test_pal is used to test
if a number is a palindrome. find_pal loops over all numbers starting with 
the number just under the max number (input) to zero and calculates the 
products between that number and all the numbers less than or equal to it and 
then checks that it is a palindrome. If the quotient is a palindrome is larger
that the current largest palindrome it is saved. After the loops, the largest 
number is returned.   In this case, the max number is 1000
"""

def test_pal(num):
    nstr = str(num)
    for i in range(len(nstr)//2):
        if nstr[i] != nstr[-(i+1)]:
            return False
    return True

def find_pal(mx_num):
    a = mx_num-1
    val = False
    holder = 0
    for j in range(a, 0, -1):
        for i in range(j, 0, -1):
            val = test_pal(i*j)
            if val and i*j > holder:
                holder = i*j
    return holder

print(find_pal(1000))