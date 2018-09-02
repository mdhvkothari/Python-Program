# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 23:09:25 2018

@author: Madhav
"""
t=int(input())
for i in range(0,t):
    n=int(input())
    a=list(map(int,input().strip().split(' ')))
    b=list(map(int,input().strip().split(' ')))
    if (len(a)==n or len(b)==n):
        f=sum(a)-max(a)
        g=sum(b)-max(b)
        if f>g:
            print("Bob")
        elif g>f:
            print("Alice")
        else:
            print("Draw")
    
    