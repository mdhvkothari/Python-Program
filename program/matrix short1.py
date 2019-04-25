a=[[2,1],
   [3,4]]

b=[0,0,0,0]

counter=0
for i in range(0,len(a)):
    for j in range(0,2):
        b[counter]=a[i][j]
        counter +=1
print (b)

temp=0
for i in range(0,len(b)-1):
    for j in range(0,len(b)-1):
        if b[j] >b[j+1]:
            b[j]=temp
            b[j]=a[j+1]
            b[j+1]=temp
print (b)
o=0
for i in range(0,2):
    for j in range(0,2):
        a[i][j]=b[o]
        o+=1
print (a)
