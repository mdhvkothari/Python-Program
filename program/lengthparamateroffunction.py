# -*- coding: utf-8 -*-
"""
Created on Sun May  6 12:46:12 2018

@author: Madhav
"""

def function(a,*b):
    print(a)
    
    for j in b:
        print(j)
        
    return;

function(10,20,30)
function(10)