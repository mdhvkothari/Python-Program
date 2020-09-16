arr=["S"
,"SS"
,"SSE"
,"SSEC"
,"SSE"
,"SS"
,"S"]
t = int(input())
for i in range(0,t):
    n = int(input())
    if n<=7:
        result=[]
        for j in range(0,len(arr[n-1])):
            result.append(ord(arr[n-1][j]))
        print(*result)
    else:
        result=[]
        n = n%7
        for j in range(0,len(arr[n-1])):
            result.append(ord(arr[n-1][j]))
        print(*result)