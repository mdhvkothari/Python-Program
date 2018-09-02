# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 17:04:00 2018

@author: Madhav
"""

t=int(input())
for i in range(0,t):
    count=0
    n=int(input())
    while n!=1:
        if n==1:
            print(1)
        if n%2==0:
            n=n//2
            count=count+1
        else:
            n=(3*n)+1
            count=count+1
            
            
            
            
            
            
            
            
    print(count)