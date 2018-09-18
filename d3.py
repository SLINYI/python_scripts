#!/usr/bin/env python
def dir_a(path):
    dir_b = open(path,'r')
    dir_c = open('/home/dir-aa','w')
    while True:
        da = dir_b.read()
        if not da:
            break
        dir_c.write(da)
    dir_b.close()
    dir_c.close()

dir_a('/etc/hosts')