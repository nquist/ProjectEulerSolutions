# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 15:30:02 2022

@author: nquist
This solves project Euler problem 25. It finds the index of the first number
in the Fibonacci sequence that has 1000 digits.

Answer: 4782
Execution Time: 0.05000 seconds
"""

import time
start = time.time()

n_2 = 1
count = 2
Fib_sum = 1

while len(str(Fib_sum)) < 1000:
    temp = 1*Fib_sum
    Fib_sum += n_2
    n_2 = temp*1
    count += 1

print("The %i is the %ith number in the Fibonacci sequence that is larger than 1,000 digit." % (Fib_sum, count))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))


