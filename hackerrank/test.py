a=[1,2,3,4,5]
b=[6,1,2]
c=[]
d=[]
for i in range(0,len(b)):
	a.append(b[i])

print(a)

for j in range(0,len(a)):
	for k in range(j,len(a)-1):

		if a[k+1]==a[j]:
			c.append(j)
			c.append(k+1)		

print(c)
z=a[:]
for i in c:
	a.remove(z[i])

print(a)