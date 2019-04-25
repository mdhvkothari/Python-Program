# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 17:36:00 2018

@author: Madhav
"""

n=int(input())
a=[]
count=0
count1=0
a=list(map(int,input().strip().split(" ")))
for i in a:
    if i%2==0:
        count=count+1
    else:
        count1=count1+1
if count>count1:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
        