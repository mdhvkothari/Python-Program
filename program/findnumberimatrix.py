a=[[2,1],
   [2,4]]

b=[0,0,0,0]

counter=0
for i in range(0,len(a)):
    for j in range(0,2):
        b[counter]=a[i][j]
        counter +=1
print (b)

a=0

al=len(b)

while al>0:
    count=0
    le=b[z]
    for k in range(0,len(b)):
        if le==b[k]:

            count +=1
    al-=1
    z+=1
    print (count)
