N = int(input())
S = []
T = []
ans=[]
for i in range(N):
    one,two = input().split()
    S.append(int(one))
    T.append(int(two))
    ans.append(abs(int(one)-int(two)))
index = ans.index(max(ans))
if(S[index]>T[index]):
    player = 1
else:
    player = 2

print(player,"",ans[index])
