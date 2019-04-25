# -*- coding: utf-8 -*-
"""
Created on Sun May  6 23:06:19 2018

@author: Madhav
"""

def selection(list):
    for i in range(0,len(list)):
        for j in range(0,len(list)-1):
            mn=list[j]
            if mn>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
                
                
a=[8,5,1,2,8,0]
selection(a)
print(a)