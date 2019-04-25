# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 21:55:02 2018

@author: Madhav
"""
x,y=input().split()
x=int(x)
e=float(y)
f=.5+float(x)
if x%5==0 and f<=e :
    
    print("%.2f"%(e-f))
else:
    print("%.2f"%e) 