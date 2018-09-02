a = [6 ,5 ,2 ,3 ,5 ,2 ,2 ,1 ,1 ,5 ,1 ,3 ,3 ,3 ,5]
a.sort()
print(a)
d=[]
for i in a:
	if i not in d:
		d.append(i)
print(d)
paires=[]
for j in range(0,len(d)):
	count =0
	for k in range(0,len(a)):
		if d[j]==a[k]:
			count +=1

	if count>1:
		pair=count//2
		paires.append(pair)

print(sum(paires))