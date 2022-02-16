# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 13:42:05 2022

@author: nquist
This solves project Euler problem 45. This finds the next number that is both
a Triangle, Pentagonal and Hexagonal number after 40755. The Triangle, pentagonal
and hexagonal numbers can be calculated using.

T(n) = n(n+1)/2
P(n) = n(3n-1)/2
H(n) = n(2n-1)

Answer: 1533776805
Execution Time: 0.15205 seconds
"""

import time
start = time.time()

def calc_T(num):
    calc = num*(num+1)/2
    return int(calc)

def calc_P(num):
    calc = num*(3*num-1)/2
    return int(calc)

def calc_H(num):
    calc = num*(2*num-1)
    return int(calc)

T = [280, calc_T(280)]
P = [160, calc_P(160)]
H = [144, calc_H(144)]
found = False

while not found:
    if (H[1] - P[1]) > 0 and (H[1] - T[1]) > 0:
        while H[1] > P[1]:
            P[0] = P[0] + 1
            P[1] = calc_P(P[0])
        while H[1] > T[1]:
            T[0] = T[0] + 1
            T[1] = calc_T(T[0])
    elif (H[1] == P[1]) and (H[1] == T[1]):
        print('%i is the next triangle number (num %i) that is also ' % (H[1], T[0]) +
              'a pentagonal (num %i) and hexagonal (num %i) number.' % (H[0], P[0]))
        found = True
    else:
        H[0] = H[0] + 1
        H[1] = calc_H(H[0])

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))
