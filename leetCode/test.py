nums = [-1,-2,-3]
n = 3
max= 0
for i in range(0,len(nums)):
    list1 = nums[i:n]
    num=1
    n+=1
    if len(list1)==3:
        print(list1)
        for j in range(0,len(list1)):
            num = num*list1[j]
    if num>max:
        max= num

print(max)