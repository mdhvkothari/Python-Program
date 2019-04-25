# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 20:57:34 2018

@author: Madhav
"""

a=93.675
d=str(a)
b=d.split('.')
f=str(b[1][0])+"."+str(b[1:])
if int(b[1][1])<5:
        print(b[0]+"."+b[1][0]+b[1][1])
else:
        print(b[0]+"."+b[1][0]+str((int(b[1][1])+1)))