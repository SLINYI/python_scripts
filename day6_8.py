#!/usr/bin/env python
import os,sys
def fun(path):
    isdir,isfile,join = os.path.isdir,os.path.isfile,os.path.join
    lsdir = os.listdie(path)
    dirs = [i for i in lsdir if isdir(join(path,i))]
    files = [i for i in lsdir if isfile(join(path, i))]
    if dirs:
        for d in dirs:
            fun(join(path,d))
    if files:
        for f in files:
            print(join(path,))
fun('/home')