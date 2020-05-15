a=2
arr=[0,1]
for i in range(2,a+2):
    element = arr[i-1]+arr[i-2]
    print(element)
    arr.append(element)
print(arr[-1])