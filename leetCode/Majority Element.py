
nums=[2,2,1,1,1,1,1,2,2]
dict={}
for char in nums:
    if char not in dict:
        dict[char] = 1
    else:
        dict[char] = dict[char]+1
for char in dict:
    if dict[char] > len(nums)//2:
        print(char)
        break