n = 13
arr = [5,5,2,4,1,5,9,8,6,3,8,9,1]
dp = []

for i in range(0,n+1):
    dp.append(0)
dp[n] = 1
for i in range(n-1,-1,-1):
    for j in range(1,arr[i]+1):
        if i+j < len(dp):
            dp[i] += dp[i+j]


print(dp[0])