area = 10000000
arr =[]
for i in range(1,area+1):
    inter = []
    for j in range(1,area+1):
        if i*j == area:
            if i-j >=0:
                inter.append(i)
                inter.append(j)
    if len(inter)>0:
        arr.append(inter)
print(arr)
min = arr[0][0]-arr[0][1]
index = 0
for i in range(0,len(arr)):
    if arr[i][0] - arr[i][1] <min:
        min = arr[i][0] - arr[i][1]
        index = i
print(arr[index])