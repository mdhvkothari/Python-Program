l=list(map(int,input().split()))
N=l[0]
K=l[1]
element=list(map(int,input().split()))

count = 0
for i in range(N):
    for j in range(i,N):
        if i!=j:
            if (abs(element[i]-element[j]>=K)):
                count = count+1
            if(abs(element[j]-element[i]>=K)):
                count = count+1
        

print(count)