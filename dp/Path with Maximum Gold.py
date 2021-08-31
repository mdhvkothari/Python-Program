arr = [[1,2,9,2],[7,0,1,6],[4,6,5,0],[8,3,4,5]]


dp = []

for i in range(0,len(arr)):
    tempArr = []
    for j in range(0,len(arr[i])):
        tempArr.append(0)
    dp.append(tempArr)


#in this we are fill dp arr first column and row in a reverse order


for i in range(len(arr[0])-1,-1,-1):
    for j  in range(len(arr)-1,-1,-1):
        if i == len(arr[0])-1:
            dp[j][i] = arr[j][i]
        elif j == len(arr)-1:
            dp[j][i] = arr[j][i] + max(dp[j][i+1],dp[j-1][i+1])
        elif j == 0: 
            dp[j][i] = arr[j][i] + max(dp[j][i+1],dp[j+1][i+1])
        else:
            dp[j][i] = arr[j][i] + max(dp[j][i+1],max(dp[j+1][i+1],dp[j-1][i+1]))


finalVal = []

for i in range(0,len(dp)):
    for j in range(0,len(dp[i])):
        if j == 0:
            finalVal.append(dp[i][j])
print(max(finalVal))
