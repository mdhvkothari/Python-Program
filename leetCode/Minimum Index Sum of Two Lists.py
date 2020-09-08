class Solution(object):
    def findRestaurant(self, list1, list2):
        dict1 = {}
        dict2 = {}
        
        for i1, v1 in enumerate(list1):
            dict1[v1] = i1
        for i2, v2 in enumerate(list2):
            dict2[v2] = i2
        
        result = []
        minIndexSum = 1000000
        for k in dict1:
            if k in dict2:
                if dict1[k] + dict2[k] < minIndexSum:
                    minIndexSum = dict1[k] + dict2[k]
                    result = [k]
                elif dict1[k] + dict2[k] == minIndexSum:
                    result.append(k)
                    
        return result