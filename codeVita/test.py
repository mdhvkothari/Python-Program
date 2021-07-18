a = [1,3,5,2,4,6,7]
count=0
i=0
while(i<len(a)):
    if (a[i]!=i+1):
        while(a[i]!=i+1):
            temp  = a[a[i]-1]
            a[a[i]-1] = a[i]
            a[i]  = temp
            print(a)
            count+=1
    i+=1
