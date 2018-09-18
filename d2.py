#!/usr/bin/env python
import sys
def dir_a(path):
    dir_s = open(path,'r')
    dir_d = open(path +'_bak','w')
    while True:
        da = dir_s.read()
        if not da:
            break
            dir_d.write(da)
    dir_s.close
    dir_d.close
dir_a(sys.argv[1])