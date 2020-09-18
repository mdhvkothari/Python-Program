arr=[5]
k = 1
j=k
i=0
result=0
while(j!=len(arr)+1):
    print(arr[i:j])
    if sum(arr[i:j])/float(k) > result:
        result = sum(arr[i:j])/float(k)
    j+=1
    i+=1
print(result)