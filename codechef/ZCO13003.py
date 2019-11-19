l=list(map(int,input().split()))
N=l[0]
K=l[1]

hardness=list(map(int,input().split()))

count = 0
for i in range(N):
    for j in range(i,N):
        if i!=j:
            if hardness[i]+hardness[j]<K:
                count = count+1

print(int(count))