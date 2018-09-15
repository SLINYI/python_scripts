#!/usr/bin/env python
import getpass
user = input("name:")
password = getpass.getpass("please password:")

if user == "kil" and password == "123":
    print("ok")