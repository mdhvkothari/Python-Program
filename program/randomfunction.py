# -*- coding: utf-8 -*-
"""
Created on Mon May  7 12:31:03 2018

@author: Madhav
"""

import random

print(random.randint(0,7))

list1=[1,4,2,'sdsjb','240',0]

print(random.choice(list1))

print(random.choices(list1,k=10))

a= list(range(1,53))

ace=random.sample(a,k=2)

print(ace)




coin=['H','T']

print(random.choice(coin))
