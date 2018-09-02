a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
array=[]


for i in range(0,len(a)):
	count=0
	while (a[i]!=1):
		if a[i]%2==0:
			a[i]=a[i]//2
		else:
			a[i]=(a[i]*3+1)
		count+=1
		
	array.append(count)
print(array)

for k in range(0,len(array)):
	if max(array)==array[k]:
		print(k+1)
	
print(max(array))