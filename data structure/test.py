a= [1,1,0,1,1,1,0,1,1]
max=0
count=0
for i in range(0,len(a)):
    if (a[i]==1):
        count+=1
    else:
        count=0
    if max<count:
        max = count
print(max)