T = int(input())
N= int(input())
arr=[]
n1 = 0
n2 = 1
count = 0

if N == 1:
   print(n1)

else:
   while count < N:
       arr.append(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

for i in range(0,N):
    arr[i] = arr[i]%10

updateArr =[]
if(N!=0):
    while(len(updateArr)!=1):
        updateArr =[]

        for i in range(0,len(arr)):
            if(i%2!=0):
                updateArr.append(arr[i]);
        arr = updateArr

    print(arr[0])
