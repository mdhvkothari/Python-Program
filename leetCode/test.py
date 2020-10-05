arr=[1,2,3]
index=0
count=0
for i in range(0,len(arr)):
    index=i
    for j in range(0,i):
        while(index!=len(arr)+1):
            arr1=arr[j:index]
            index+=1
            j+=1
            mul=1
            for k in range(0,len(arr1)):
                mul = mul*arr1[k]
            if mul<0:
                count+=1
print(count)