# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:12:29 2020

@author: nquis
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
        