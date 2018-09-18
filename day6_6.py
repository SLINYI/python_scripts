#!/usr/bin/env python
def fibs(num):
     fib = [0,1]
     for i in range(num -2):
        fib.append(fib[-1] + fib[-2])
     print(fib)
fibs(5)