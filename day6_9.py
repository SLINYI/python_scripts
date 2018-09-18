#!/usr/bin/env python
import string,random
pwd = ''
all_choice = string.ascii_letters + string.digits
num = int(input('please input number'))
for i in range(num):
    pwd += random.choice(all_choice)

print(pwd)