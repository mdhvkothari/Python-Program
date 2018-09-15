s=raw_input()
array=[]
index=[]
a=[]




for i in range(0,len(s)):
	if s[i] not in array:
		array.append(s[i])
		index.append(i)
value=[]
for i in range(0,len(array)):
	count=0
	for j in range(0,len(s)):
		if array[i]==s[j]:
			count+=1
	value.append(count)
for i in range(0,len(array)):
	for j in range(0,len(array)-1):
		if  value[j]<value[j+1]:
			temp=value[j]
			temp1=array[j]
			value[j]=value[j+1]
			array[j]=array[j+1]
			value[j+1]=temp
			array[j+1]=temp1
finalarray=[]
finalarray=array
finalvlaue=[]
finalvlaue=value
print(finalarray)
print(finalvlaue)

for i in range(0,len(finalarray)-1):
	if finalvlaue[i]==finalvlaue[i+1]:
		if finalarray[i]>finalarray[i+1]:
			temp2=finalarray[i]
			finalarray[i]=finalarray[i+1]
			finalarray[i+1]=temp2
if finalvlaue[0]==1 and finalvlaue[1]==1 and finalvlaue[2]==1:
	for i in range(0,len(s)):
	a.append(s[i])

	for i in range(0,len(a)):
		for j in range(0,len(a)-1):
			if a[j]>a[j+1]:
				temp2=a[j]
				a[j]=a[j+1]
				a[j+1]=temp2



for i in range(0,3):
	if finalvlaue[0]==1 and finalvlaue[1]==1 and finalvlaue[2]==1:
		print a[i],finalvlaue[i]
	else:
		print finalarray[i],finalvlaue[i]


			





