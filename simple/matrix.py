a=[[2,1,3],[5,2,3],[2,5,8]]
b=[[2,1,3],[5,2,3],[2,5,8]]
d=[[1,1,1],[1,1,1],[1,1,1]]

for i in range(len(a)):
 for k in range(len(b)):
  d[i][k]= a[i][k]+b[i][k]

for x in d:
 print x