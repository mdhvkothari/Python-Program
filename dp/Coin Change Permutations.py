coins = [2,3,5,6]
target = 10

dp = []
for i in range(0,target+1):
    dp.append(0)

dp[0] = 1



for i in range(1,len(dp)):
    for coin in coins:
        if i >= coin:
            dp[i] += dp[i-coin]


print(dp[target])



