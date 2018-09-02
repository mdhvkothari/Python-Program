# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 19:26:43 2018

@author: Madhav
"""

t=int(input())
for i in range(0,t):
    n,k=input().split()
    n,k=[int(n),int(k)]
    s=str(input("S"))
    a,b=0,0
    for j in s:
        if j.isupper():
            a=a+1
        elif j.islower():
            b=b+1
    if b>=n-k and a<n-k:
        print("chef")
    elif a>=n-k and b<n-k:
        print("brother")
    elif a>=n-k and b>=n-k:
        print("both")
    else:
        print("none")
            