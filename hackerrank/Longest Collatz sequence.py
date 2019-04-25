# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 20:06:25 2018

@author: Madhav
"""

t=int(input("ente"))
for i in range(0,t):
    count=0
    n=int(input("aa"))
    while n!=1:
        if n==1:
            print(1)
        if n%2==0:
            n=n//2
            count=count+1
        else:
            n=(3*n)+1
            count=count+1
        print(n)
    print(count)