arr = [17,18,5,4,6,1]
b = max(arr)
i=0
a=0
while(i<len(arr)-1):
    if b == arr[i]:
        for j in range(a,i):
            arr[j] = b
        a=i
    i+=1
    b = max(arr[a+1:])

arr[a] = -1
print(a)
print(arr[:a+1])




