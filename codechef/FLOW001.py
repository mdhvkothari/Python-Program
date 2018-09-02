# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 21:48:31 2018

@author: Madhav
"""

a=int(input("enter number:"))
for i in range(0,a):
    b,c=int(input("")).strip().split("")
    b,c=[int(b),int(c)]
    print(b+c)