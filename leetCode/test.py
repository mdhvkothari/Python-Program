n = int(input())
arr = list(map(int,input().strip().split()))
d = {}
for i in arr:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1
for i in d:
    if d[i]%2!=0:
        print(i)
        break

