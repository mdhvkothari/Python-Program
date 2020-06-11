arr = [-2,1,-3,4,-1,2,1,-5,4]
dp = [0 for i in range(len(arr))]
dp[0] = arr[0]
for i in range(1,len(arr)):
    dp[i] = max(dp[i-1]+arr[i],arr[i])
    print(dp[i])
    
