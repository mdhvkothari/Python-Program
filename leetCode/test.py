a= [3,2,2,3,1]
b=1
i=0
while(i<len(a)):
    if a[i] == b:
        a.remove(a[i])
        print(a)
    i+=1
print(a)