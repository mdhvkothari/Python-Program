a = list(map(int,input().split()))
for i in range(0,len(a)):
    if(a[i]==0):
        a.append(0)
        a.remove(a[i])
print(a)