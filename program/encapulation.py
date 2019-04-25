# -*- coding: utf-8 -*-
"""
Created on Mon May  7 17:58:37 2018

@author: Madhav
"""

class encaplutation:
    def __init__(self,a,b,c):
        self.public = a
        self._protected = b
        self.__private  = c
        
a= encaplutation(11,25,25)
print(a.public)
print(a._protected)
print(a.__private)
        
        