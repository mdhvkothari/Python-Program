# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 22:13:34 2018

@author: Madhav
"""

#t=int(input())
#for i in range(0,t):
#n,k=input().strip().split(' ')
'''n,k=[int(n),int(k)]
num=int(input())
arr = [int(x) for x in str(num)]
b=0
f=k
arr1=[]
for j in arr:
    d=arr[b:f]
    e=1
    print(d)
    if len(d)==f:
        for k in range(0,f):
            e=e*d[k]
            print(e)
        arr1.append(e)
    b=b+1
    f=f+1'''
            

'''t=int(input())
for i in range(0,t):
    f=[]
    n,k=input().strip().split(' ')
    n,k=[int(n),int(k)]

    num=int(input())
    a= [int(x) for x in str(num)]
    b=0
    c=k
    for i in a:
        d=a[b:c]
        e=1
        if len(d)==5:
            for j in range(0,len(d)):
                e=e*d[j]
            f.append(e)
        
        b=b+1
        c=c+1
    print(max(f))'''
    
'''n=int(input())    
score=list(map(int,input().strip().split(' ')))
ma=0
mi=0
a1=score[0]
b1=score[0]
for j in range(0,len(score)-1):
    if a1<score[j+1]:
        a1=score[j+1]
        ma=ma+1
for k in range(0,len(score)-1):        
    if b1>score[k+1]:
        b1=score[k+1]
        mi=mi+1    
print(ma)
print(mi)'''

'''n=int(input())
b=[]
a=[]

for i in range(0,n):
    a=list(map(int,input().strip().split(' ')))
    b.append(a[i])
print(b)'''
'''a=[8,8,8,8]
c=[]
for i in range(0,len(a)-1):
    for j in range(0,len(a)-1):
        b=a[j+1]-a[i]
        c.append(b)
print(max(c))'''


'''a="ABCDCDC"
b="CDC"
count=0
for i in range(0,len(a)):
    if a[i:i+len(b)]==b:
        count=+1
print(count)'''

'''n=int(input())
diff=[]
a=0
flag=0
arr=list(map(int,input().strip().split(' ')))
for i in range(0,len(arr)):
    for j in range(0,len(arr)-1):
        if arr[i]+arr[j+1]==n:
            break
            print(i,j-1)'''

'''a="aaabccdd"
c=list(a)
b=[]
print(c)
for i in a:
    if b and b[-1]==i :
        b.pop()
    else:
        b.append(i)
print(b)'''

'''a=[20,  19,18,16,14,15,14,13,11]
count=0
for i in range(0,len(a)-1):
    if a[i]>a[i+1]:
        
        count=count+1
if count==1:
     print("YES")
else:
    print("NO")'''
        
'''n,k=input().split(' ')
n,k=int(n),int(k)
c=list(map(int,input().strip().split(' ')))
b=int(input())
c.pop(k)
if (sum(c)//2-b)<=b:
       print("Bon Appetit")
else:
       print(b-sum(c)//2)'''
       
       
'''input()
count = [0]*6
for t in map(int,input().strip().split()):
    count[t] += 1
    print(count)
print(count.index(max(count)))'''

'''n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
ar.sort()
count=0
for i in range(0,len(ar)-1):
    
    if ar[i]==ar[(i//2)+1]:
        count=count+1
print(count)'''        

'''n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
height = list(map(int, input().strip().split(' ')))        
c=max(height)
if c>k:
    print(c-k)
else:
    print(0)'''
    
'''    
n=int(input())
s=str(input())
up=0
total=0
pre=0
for i in range(0,len(s)):
    if s[i]=="U":
        up=up+1
        
    else:
        up=up-1
        
    if up==0 and s[i]=="U":
        total=total+1
print(total)'''

'''q=int(input())
for i in range(0,q):
    q1=list(map(int,input().strip().split(' ')))
    mou1 = abs(q1[2]-q1[1])
    mou2= abs(q1[2]-q1[0])
    if mou2>mou1:
        print("Cat B")
    elif mou2<mou1:
        print("Cat A")
    else:
        print("Mouse C")'''
    
'''n=int(input())
a=list(map(int,input().strip().split(' ')))
a.sort()
ans=0
for i in range(0,len(a)-1):
    for j in range(0,len(a)-1):
        if abs(a[j]-a[i])<=1:
            ans=max(ans,j-i+1)
        
print(ans)'''

'''t=int(input())
for i in range(0,t):
    n,k = map(int,input().strip().split(' '))
    no=0
    stu=list(map(int,input().strip().split(' ')))
    for j in range(0,len(stu)):
        if stu[j]<=0:
            no=no+1
    if no<k:
        print("YES")
    else:
        print("NO")
'''
    
'''t=int(input())
for i in range(0,t):
    n=int(input())
    if n == 0:
        h = 1
    elif n % 2 == 0:
        h = 2 ** ((n//2) + 1) - 1
    elif n % 2 == 1:
        h = 2 ** ((n + 3)//2) - 2
    print(h)'''
    
'''i,j,k = list(map(int,input().strip().split(' '))) 
count=0  
for x in range(i,j+1):
    if (x-int(str(x)[::-1]))%k==0:
        count=count+1
print(count)'''

'''rating=[84,92,61,50,95]
employee=[]
for i in range(0,len(rating)):
    if rating[i]>=90:
        employee.append(rating[i])
b=sum(employee)/2
a=str(b)
v=a.split('.')
if len(v[1])==1:
    print('{:.2f}'.format(b))
else:
    d=int(v[1][1:])
    if v[1][1]<5:
        print(v[0]+"."+v[1][0]+v[1][1])
    else:
        print(v[0]+"."+v[1][0]+(v[1][1]+1))'''

'''n=int(input())
a=str(input())
b=list(a*n)
c=""
for i in range(0,n):
    c=c+b[i]
d=list(c)
count=0
for j in range(0,len(d)):
    if d[j]=="a":
        count=count+1
        
print(count)'''

'''values=[[3,4,5,1],[33,6,1,2]]

v=values[0][0]

for i in range(0, len(values)):
    for j in range(0,len(values[i])):
        if v<values[i][j]:
            v=values[i][j]
            
print(v)'''



    

       
                


