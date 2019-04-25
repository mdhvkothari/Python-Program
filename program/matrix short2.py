a=[[2,1],
   [3,4]]

b=[]

for i in range(0,len(a)):
    b=b+a[i]

print (b)

temp=0
for i in range(0,len(b)-1):
    for j in range(0,len(b)-1):
        if (b[j]>b[j+1]):
            b[j]=temp
            b[j]=a[j+1]
            b[j+1]=temp
print (b)
