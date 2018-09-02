# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 21:24:11 2018

@author: Madhav
"""
class parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def mul(self):
        print(self.a*self.b)
        
class child(parent):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def mul(self):
        print(self.a*self.b*self.c)

x=parent(5,4)
x.mul()

y=child(5,5,5)
y.mul()         
        
        