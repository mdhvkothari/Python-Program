arr = [7,1,5,3,6,4]

minPointer = arr[0]
maxProfit = 0


for i in range(0,len(arr)-1):
    # if arr[i+1] < minPointer:
    #     minPointer = arr[i+1]
    minPointer = min(minPointer,arr[i+1])
    
    # if arr[i+1] - minPointer > maxProfit:
    #     maxProfit = arr[i+1] - minPointer
    maxProfit = max(maxProfit,arr[i+1] - minPointer)
print(maxProfit)