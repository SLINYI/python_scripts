#!/usr/bin/env python
import string,random
str_all = string.ascii_letters + string.digits
num = int(input("please enter number"))
pass_a = ''
for i in range(num):
    pass_a += random.choice(str_all)
print(pass_a)
