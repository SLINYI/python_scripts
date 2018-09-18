#!/usr/bin/env python
def fun1():
    s = int(input('please input number'))
    print(s)
try:
    fun1()
except TypeError as e:
    print(e,"error please input number")