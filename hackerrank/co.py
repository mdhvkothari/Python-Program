# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 17:19:49 2018

@author: Madhav
"""

for _ in range (input()):
    c=input()
    main=0
    maxnum=1
    for x in range (1,c+1):
        temp=0
        T=x
        while True :
            if x%2 ==0 :
                x=x/2
            else :
                x=3*x+1
            temp=temp+1
            if x==1:
                if temp == main and T>maxnum :
                    maxnum=T
                elif temp>main :
                    main=temp
                    maxnum=T
                break

    print (maxnum)