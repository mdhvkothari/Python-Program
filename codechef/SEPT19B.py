T = int(input())
for i in range(T):
    N= int(input())
    arr=[0,1]
    for i in range(2,N+1):
        f = arr[i-2]+arr[i-1]
        arr.append(f)
    updateArr =[]
    if(N!=0):
        while(len(updateArr)!=1):
            updateArr =[]
            for i in range(0,len(arr)):
                if(i%2!=0):
                    updateArr.append(arr[i]%10);
            arr = updateArr
        print(arr[0])
