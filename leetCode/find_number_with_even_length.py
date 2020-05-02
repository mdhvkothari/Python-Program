nums =[555,901,482,1771]
count=0
for i in range(0,len(nums)):
    if len(str(nums[i])) %2 ==0:
        count+=1
print(count)
