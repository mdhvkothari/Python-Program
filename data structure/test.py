a=15
arr = []
i=2
while(i<a):
    flag = 0
    for j in range(2,i):
        if i%j == 0:
            flag = 1
    if flag == 0:
        arr.append(i)
    i = i+1
sum = 0
result = []
for i in range(0,len(arr)):
    sum = sum +arr[i]
    result.append(sum)
for j in range(0,len(arr)):
    if arr[j] in result:
        print(arr[j])