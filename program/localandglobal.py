# -*- coding: utf-8 -*-
"""
Created on Tue May 15 18:34:15 2018

@author: Madhav
"""

money=1000
def addmoney():
    global money
    money=money+1
    print(money)
print(money)
addmoney()

def overridind(list1):
    list1=[1,2,3]
    print(list1)
l=[4,5,6]
overridind(l)
