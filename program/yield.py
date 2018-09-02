            # -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 21:49:56 2018

@author: Madhav
"""

def reverse(data):
    yield data[::-1]

for i in reverse('golf'):
    print(i)
