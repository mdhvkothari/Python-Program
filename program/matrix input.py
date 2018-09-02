a= [[0,0,0],
    [0,0,0],
    [0,0,0]]


for i  in range(0,len(a)):
    for j in range(0,len(a)):
        a[i][j]=int(input("Enter number:"))

print (a)
#conversion if 3D in 1D
b=[0,0,0,0,0,0,0,0,0]
count=0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        b[count]=a[i][j]
        # condition
        if b[count]%7==0:
            b[count]="Hello"
        count += 1
#conversion of 1D into 3D
print (b)
o=0
for i in range(0,3):
    for j in range(0,3):
        a[i][j]=b[o]
        o+=1
print (a)
