nums =  [-2,1,-3,4,-1,2,1,-5,4]

#overAllSum
oSum = nums[0]

#current sum
cSum = nums[0]

for i in range(1,len(nums)):
    if cSum >= 0:
        cSum += nums[i]
    else:
        cSum = nums[i]
    
    oSum = max(cSum,oSum)
print(oSum)












