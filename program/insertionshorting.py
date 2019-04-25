# -*- coding: utf-8 -*-
"""
Created on Sun May  6 22:56:33 2018

@author: Madhav
"""

def insertion(list):
    for index in range(1,len(list)):
        value=list[index]
        i= index-1
        while i>=0:
            if value<list[i]:
                list[i+1]=list[i]
                list[i]=value
                i=i-1
            else:
                break
a=[3,5,4,12,8,1,0]            
print(insertion(a))
print(a)