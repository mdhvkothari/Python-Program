a=[1,2,3,2,1]
b=[3,2,1,2,1]
arr1=[]
arr2=[]

if a ==b:
    print(len(a))

for i in range(0,len(a)):
    index=i
    for j in range(0,i):
        while(index!=len(a)+1):
            arr1.append(a[j:index])
            index+=1
            j+=1

for i in range(0,len(b)):
    index=i
    for j in range(0,i):
        while(index!=len(b)+1):
            arr2.append(b[j:index])
            index+=1
            j+=1

print(arr1)
print(arr2)
length =0
for i in arr1:
    if i in arr2:
        if length<len(i):
            length = len(i)

    # for j in range(0,len(arr2)):
    #     if i!=j:
            
print(length)