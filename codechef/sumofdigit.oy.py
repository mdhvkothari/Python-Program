# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 21:19:56 2018

@author: Madhav
"""

t=int(input())
 
for i in range(t):
    n=int(input())
    sum=0
    while n > 0:
        rem=n%10
        n=n//10
        sum+=rem
    print(sum)  
    
 