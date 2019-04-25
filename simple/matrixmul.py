a=[[2,1,3],[2,1,3],[2,1,3]]
b=[[2,1,3],[2,1,3],[2,1,3]]
c=[[1,1,1],[1,1,1],[1,1,1]]

for i in range(len(a)):
 for j in range(len(b[0])):
  for l in range(len(b)):

   c[i][j] +=a[i][l]*b[l][i]

for x in c :
 print x