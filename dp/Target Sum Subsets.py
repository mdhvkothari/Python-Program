arr = [5,4,2,3,1,7]
target = 10


dp = []
for i in range(0,len(arr)+1):
    tempArr  = []
    for j in range(0,target+1):
        tempArr.append(None)
    dp.append(tempArr)

for i in range(0,len(dp)):
    for j in range(0,len(dp[0])):
        if i == 0 and j == 0:
            dp[i][j] = True
        elif i == 0:
            dp[i][j] = False
        elif j == 0:
            dp[i][j] = True
        else:
            if dp[i-1][j] == True:
                dp[i][j] = True
            else:
                val = arr[i-1]
                if j >= val:
                    if dp[i-1][j-val] == True:
                        dp[i][j] =True

print(dp[len(arr)][target])



