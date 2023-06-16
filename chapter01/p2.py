#!/usr/bin/python3

# author = Lokesh
# This program lists the content of a directory.

import os

directory = '/home/l0ksh'

contents = os.listdir(directory)
print(type(contents))

for item in contents:
    print(item)
