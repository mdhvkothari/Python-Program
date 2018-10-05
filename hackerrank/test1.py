a=[20,-50,-50,20,51]
lis=[]
a.sort()
for i in a:
	if i not in lis:
		lis.append(i)
print(lis)