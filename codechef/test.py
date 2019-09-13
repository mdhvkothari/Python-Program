T = int(input())
for i in range(T):
    N= int(input())
    arr=[]
    n1 = 0
    n2 = 1
    count = 0

    while count < N:
        arr.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


    updateArr =[]
    if(N!=0):
        while(len(updateArr)!=1):
            updateArr =[]
            for i in range(0,len(arr)):
                if(i%2!=0):
                    updateArr.append(arr[i]%10);
            arr = updateArr
        print(arr[0])
