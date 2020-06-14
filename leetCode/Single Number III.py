class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dict = {}
        result= []
        for num in nums:
            if num in dict:
                dict[num] +=1
            else:
                dict[num] = 1
        for i in dict:
            if dict[i] == 1:
                result.append(i)
        return result