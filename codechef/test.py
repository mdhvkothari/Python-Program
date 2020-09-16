n = int(input())
n = str(n)
nums=[]
for i in range(1,len(n)+1):
    nums.append(n[0:i])


flag=0
for i in range(0,len(nums)):
    if int(nums[i])%(len(nums)-i) != 0:
        
        flag=1
        break
if flag == 0:
    print("Yes")
else:
    print("No")
