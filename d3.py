#!/usr/bin/env python
import os,sys
def aa(path):
    if os.path.isfile(path):
        os.mknod(path)
    else:
        os.mkdir(path)
aa('/home/sl')