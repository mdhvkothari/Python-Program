# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:45:19 2018

@author: Madhav
"""

class employee:
    increment=1.07 #class variable
    def __init__ (self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    
    def payincrease(self):
        self.pay=int(self.pay * self.increment) #we use self here so that we can increase value of increment anywhere

emp1=employee("Madhav","kothari",600000)
emp2=employee("Madhv","kthari",6000000)
#give increase amount of pay
emp1.payincrease()
print(emp1.pay)
#let's change the valuse of increment
employee.increment=1.04
print(employee.increment)
emp1.payincrease()  
print(emp1.pay)
        