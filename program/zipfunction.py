# -*- coding: utf-8 -*-
"""
Created on Sun May  6 12:13:41 2018

@author: Madhav
"""

a=['name','sirname','age']
b=['madhav','kothari','18']
for a,b in zip(a,b):
    print ('your name {0} it is {1}'.format(a,b))
    
    
def function(a,*b):
    print(a)
    for j in b:
        print(j)
    
    return;

function(10,20,20       )