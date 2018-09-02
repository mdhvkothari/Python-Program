# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:07:46 2018

@author: Madhav
"""

class employee:
    def __init__ (self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    
a= employee("Madhav","Kothari",60000)
print(a.first)
print(a.last)
print(a.pay)
    

        