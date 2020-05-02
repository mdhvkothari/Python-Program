a=[1,2,3,0,0,0]
b=[2,5,6]
n=3
j=0
for i in range(n,len(a)):
    a[i] = b[j]
    j+=1
print(a)