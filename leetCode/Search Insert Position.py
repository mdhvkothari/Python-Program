class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for i in range(0,len(nums)):
                if nums[i] == target:
                    return i
        else:
            index=0
            while(len(nums)>index and nums[index]<target):
                index +=1
            return index