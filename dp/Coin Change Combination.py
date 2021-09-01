coins = [2,3,5,6]
target = 10


dp = []


for i in range(0,target+1):
    dp.append(0)

dp[0] = 1


for i in coins:
    for j in range(i,len(dp)):
        dp[j] += dp[j-i]
        

print(dp[target]) 





