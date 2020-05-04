a= [0,0,1,1,1,2,2,3,3,4]
i=0
for j in range(0,len(a)):
    if a[i] != a[j]:
        i +=1
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
    
print(i+1)
