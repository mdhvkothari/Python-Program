a=[2,6]
b=[24,36]
c=[]
for i in range(a[-1],b[0]+1):
	for j in range(0,len(a)):
		if i%a[j]==0:
			c.append(i)

print(c)