T = int(input())
while (T>0):
    N = int(input())
    A = list(map(int,input().split()))
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





