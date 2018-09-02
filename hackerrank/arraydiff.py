a=[4,6,5,3,3,1]
count = 0
for i in range(0,len(a)-1):
	for j in range(0,len(a)-1):
		if (a[i]-a[j])<=1:
			print(a[i],a[j])
			count = count+1

print(count)
