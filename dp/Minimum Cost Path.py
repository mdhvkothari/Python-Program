arr = [[1,23,40],[0,30,50],[36,12,10]]

dp = []


for i in range(0,len(arr)):
    temp = []
    for j in range(0,len(arr[i])):
        temp.append(0)
    dp.append(temp)



for i in range(len(dp)-1,-1,-1):
    for j in range(len(dp[0])-1,-1,-1):
        if i == len(dp) - 1 and j == len(dp[0]) - 1:
            dp[i][j] = arr[i][j]
        elif i == len(dp) - 1:
            dp[i][j] = dp[i][j+1] + arr[i][j]
        elif  j == len(dp[0])-1:
            dp[i][j] = dp[i+1][j] +arr[i][j]
        else:
            dp[i][j] = min(dp[i][j+1]+arr[i][j] ,dp[i+1][j]+arr[i][j])

print(dp[0][0])
