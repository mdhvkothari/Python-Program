# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 19:45:42 2018

@author: Madhav
"""

t=int(input())
for i in range(0,t):
    a,b,c,d=input().split()
    a,b,c,d=[int(a),int(b),int(c),int(d)]
    if a*b==c*d or a*c==b*d or a*d==b*c:
        print("yes")
    else:
        print("no")