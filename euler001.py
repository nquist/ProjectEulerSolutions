# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:08:04 2020

@author: nquis
This code solves Project Euler problem 1. The funtion finds the sum of all the
multilpes of 3 and 5 that are below the given number (num). In this case, we 
want the sum of the numbers below 1000.
"""

def sum3s_5s(num):
    sm = 0
    fives = (num-1)//5
    threes = (num-1)//3
    fifteens = (num-1)//15
    print(fives, threes)
    sm += (fives*(fives+1)/2)*5
    print(sm)
    sm += (threes*(threes+1)/2)*3
    sm -= (fifteens*(fifteens+1)/2)*15
    
    return sm

print(sum3s_5s(1000))