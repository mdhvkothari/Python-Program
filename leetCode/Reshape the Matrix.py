nums = [[1,2],[3,4],[5,6]]
r = 1
c = 6
count=0
arr=[]
for i in range(0,len(nums)):
    for j in range(0,len(nums[i])):
        count+=1
        arr.append(nums[i][j])
if count<r*c:
    print(nums)
else:
    result =[]
    index=0
    for i in range(0,r):
        arr1=[]
        for j in range(0,c):
            arr1.append(arr[index])
            index+=1
        result.append(arr1)
    # index+=1
    print(result)