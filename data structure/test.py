a=[1,2,3,4]
result = []
for i in range(0,len(a)):
    sum=1
    for j in range(0,len(a)):
        if i!=j:
            sum = sum*a[j]
    result.append(sum)
print(result)   