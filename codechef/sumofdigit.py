# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 21:19:56 2018

@author: Madhav
"""

n = int(input("entr number"))
c=[]
for i in range(0,n):
    t=int(input("entr nunbr prime:"))
    c.append(t)
    for i in range(0,len(c)):
        f=[]
        flag=0
        for j in range(2,c[i]):
            if c[i]%j==0:
                flag=1
                break
            if flag==1:
                print()
            elif flag==0:
                f.append(j)
                print(f)

    