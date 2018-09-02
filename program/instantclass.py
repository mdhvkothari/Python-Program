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
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
a= employee("Madhav","Kothari",60000)
b= employee("Madv","Kthari",600000)
print(a.first)
print(a.last)
print(a.pay)
print(a.fullname())
print(b.fullname())
print(employee.fullname(a))
print(employee.fullname(b))    

        