import re

t= int(input())

upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
number=["1","2","3","4","5","6","7","8","9","0"]

for i in range(0,t):
	count=0
	flag=0
	uppervalue=[]
	numbervalue=[]
	udi=raw_input()
	for i in range(0,len(udi)):
		for j in range(i+1,len(udi)):
			if udi[i]==udi[j]:
				flag=1
				count+=1
				break
	if flag==1:
		print("Invalid")
	a=re.search(r'^[a-zA-Z0-9]*$',udi)
	if  a:
		pass
	else:
		print("Invalid")
		count+=1

	if len(udi)==10:
		for i in range(0,len(upper)):
			for j in range(0,len(udi)):
				if upper[i]==udi[j]:
					uppervalue.append(udi[j])
		for i in range(0,len(number)):
			for j in range(0,len(udi)):
				if number[i]==udi[j]:
					numbervalue.append(udi[j])
		if count==0:
			if len(numbervalue)>=3 and len(uppervalue)>=2:
				print("Valid")
				