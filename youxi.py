#!/usr/bin/env python
import random
all_1 = ["石头","剪刀","布"]
all_bijiao = ["石头","剪刀"],["剪刀","布"],["布","石头"]
prompt = """(0)石头
(1)剪刀
(2)布
请选择（0/1/2）:"""
cwin = 0
pwin = 0
while cwin <2 and pwin < 2:
    index = int(input(prompt))
    while index >= 3:
        index = int(input(prompt))
    pl = all_1[index]
    computer = random.choice(all_1)
    print("pl:%s,computer:%s" %(pl,computer))
    if pl == computer:
        print("\033[32;40;1m ping\033[0m")
    elif [pl,computer] in all_bijiao:
        #print("\033[32;40;1m mi ying le\033[0m")
        pwin += 1
    else:
        #print("\033[32;40;1m mi shu le \033[0m")
        cwin += 1
if pwin == 2:
    print("mi ying le ")
else:
    print("mi shu le ")