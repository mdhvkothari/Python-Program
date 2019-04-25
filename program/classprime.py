# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 18:03:44 2018

@author: Madhav
"""

class prime:
    flag=0
    def __init__(self,a):
        self.a=a
    def calculate(self):
        for i in range(2,self.a):
            if self.a%i==0:
                prime.flag=1
        if prime.flag==1:
            print("number is not prime")
        else:
            print("number is prime")
            
x=prime(11)
x.calculate()


