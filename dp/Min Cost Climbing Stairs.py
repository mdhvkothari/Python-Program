cost = [1,100,1,1,1,100,1,1,100,1]

arr = [cost[0],cost[1]]
n = len(cost)
for i in range(2,n):
    arr.append(cost[i]+min(arr[i-1],arr[i-2]))

print(min(arr[n-1],arr[n-2]))





