#!/usr/bin/env python
import random,string,sys
def fun(x):
    pwd = ''
    all_choice = string.ascii_letters + string.digits
    x = int(sys.argv[1])

    for i in range(x):
        pwd += random.choice(all_choice)

    print(pwd)

