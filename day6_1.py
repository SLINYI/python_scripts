#!/usr/bin/env python
try:
    s = int(input("num:"))
except TypeError as e:
    print(e,"please input number type")