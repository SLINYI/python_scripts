#!/usr/bin/env python
l1 = [1,2]
for i in range(6):
    l1.append(l1[-1] + l1[-2])
print(l1)