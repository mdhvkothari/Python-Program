a =[2,0,2,1,1,0]
for i in range(0,len(a)):
    for j in range(i,len(a)):
        if a[i]>a[j]:
            a[i],a[j] = a[j],a[i]
print(a)



