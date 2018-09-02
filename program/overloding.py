# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 13:10:56 2018

@author: Madhav
"""

class hello:
    def sayhello(self,name=None):
        if name is not None:
            print ("Hello",name)
        else:
            print("hello")
a=hello()
a.sayhello()
a.sayhello("Mdhv")
