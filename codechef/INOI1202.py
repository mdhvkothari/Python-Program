N= int(input())
n = list(map(int,input().split()))
a=[]
result=[]
for i in range(N):
    a.append(i+1)
sum=0
for i in range(len(a)):
    if(a[i]+n[i]>sum):
        sum = a[i]+n[i]

result.append(sum)
for i in range(0,len(a)-1):
    a.append(0)
    a[-1] = a[0]
    a.pop(0)
    sum=0
    for i in range(len(a)):
         if(a[i]+n[i]>sum):
            sum = a[i]+n[i]
    result.append(sum)
for i in range(len(result)):
    print(result[i],end=" ")
