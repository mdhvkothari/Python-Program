# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 21:49:07 2018

@author: Madhav
"""

n=int(input())
b=[]
for i in range(0,n):
	n1=int(input())
	b.append(n1)
c=b.sort()
for  i in range(0,len(b)):
	print(b[i])