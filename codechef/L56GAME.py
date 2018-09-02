# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 20:11:58 2018

@author: Madhav
"""

t=int(input())
d=0
for i in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    for j in a:
        if j%2!=0:
            d=d+1
    if d%2!=0:
        if len(a)==1:
            print(1)
        else:
            print(2)
    else:
        print(1)
    