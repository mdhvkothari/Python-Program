a=[2]
b=[20,30,12]
c=[]
a.sort()
b.sort()
for i in range(a[-1],b[0]+1):
	for j in range(0,len(a)):
		if i%a[j]==0:
			c.append(i)

print(c)
d=[]
for i in c:
	if i not in d:
		d.append(i)
print(d)
final = []
for k in range(0,len(b)):
	for l in range(0,len(d)):
		if b[k]%d[l]==0:
			final.append(d[k])
print(final)
