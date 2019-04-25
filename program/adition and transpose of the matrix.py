# -*- coding: utf-8 -*-
"""
Created on Mon May  7 18:54:51 2018

@author: Madhav
"""
#addition
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

b=[[1,2,3],
   [4,5,6],
   [7,8,9]]

c=[[0,0,0],
   [0,0,0],
   [0,0,0]]


for i in range(0,len(a)):
    for j in range(0,len(b)):
        c[i][j]=a[i][j]+b[i][j]
        
print(c)

#transpose
d= [[0,0,0],
   [0,0,0],
   [0,0,0]]

for i in range(0,len(a)):
    for j in range(0,len(a)):
        d[i][j]=c[j][i]



print(d)
