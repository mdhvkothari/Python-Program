n=int(input())
value=[]
for i in range(0,n):
	bio = list(map(str,raw_input().strip().split(' ')))
	value.append(bio)
for i in range(0,len(value)):
	for j in range(0,len(value)-1):
		if value[j][2]>value[j+1][2]:
			temp = value[j]
			value[j]=value[j+1]
			value[j+1]=temp
for i in range(0,len(value)):
	if value[i][3]=="M":
		print "Mr. "+value[i][0]+" "+value[i][1]
	else:
		print "Ms. "+value[i][0]+" "+value[i][1]