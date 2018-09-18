#!/usr/bin/env python
import sys
def isNum(s):
    for i in s:
        if i in '0123456789':
            pass
        else:
            print('not is number')
            break
    else:
        print('mi is number')

isNum(sys.argv[1])