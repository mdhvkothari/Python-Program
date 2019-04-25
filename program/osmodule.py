# -*- coding: utf-8 -*-
"""
Created on Mon May  7 15:42:13 2018

@author: Madhav
"""

import os

print(os.getcwd())

os.chdir('E:/project/code')

print(os.getcwd())

f=open("file.txt",'w')
f.write("madhav \n")
f.close()

f=open("file.txt",'r')
print(f.read())
f.close()

f=open("file.txt",'a')
f.write("madhav kothari")
f.close()

f=open("file.txt",'r')
print(f.read())
f.close()
