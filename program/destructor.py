# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 22:00:40 2018

@author: Madhav
"""

class destructor:
    count=0
    def __init__(self,first,last):
        destructor.count+=1
        self.__fist=first
        self.__lst=last

    def __del__(self):
        destructor.count-=1
        
x=destructor("madhav","Kothari")
print(destructor.count)
y=destructor("madv","Kothari")
print(destructor.count)        
z=destructor("madha","Kothari")
print(destructor.count)        
