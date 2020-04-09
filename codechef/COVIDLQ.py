T = int(input())
if (T>=1 or T<=100):
    print(T)
    while (T>0):
        N = int(input())
        if (T>=1 or T<=100):
            A = list(map(int,input().split()))
            if A is 1 or 0:
                position = []
                for i in range(0,len(A)):
                    if A[i]==1:
                        position.append(i+1)            
                distance = False
                for j in range(0,len(position)-1):
                    if (abs(position[j]-position[j+1])>3):
                        distance = True
                    else:
                        distance = False
                if (distance == True):
                    print("Yes")
                else:
                    print("No")

                T = T-1

else:
    print("no")


