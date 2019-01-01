a=[1,2,3,4,5]
n=len(a)
j=n
item=10
index=3
n=n+1
while(j>=index):
	a[j]=a[j+1]
	j=j-1

a[index]=item

print(a)