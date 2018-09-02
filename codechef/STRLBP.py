# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 22:54:58 2018

@author: Madhav
"""

for i in range(int(input())):
    s=input()
    error=0
    if s[0]!=s[7]:
        error=error+1
    for j in range(0,len(s)-1):
        if s[i]!=s[i+1]:
            error=error+1
    if error>2:
        print("non-uniform")
    else:
        print("uniform")
        
            
        