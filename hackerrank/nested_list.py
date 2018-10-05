arrayname=[]
arraynumber=[]
temp1=0
temp2=0
result=[]
for i in range(int(input())):
	name=raw_input()
	arrayname.append(name)
	number = float(input())
	arraynumber.append(number)

for i in range(0,len(arraynumber)):
	for j in range(0,len(arraynumber)-1):
		if arraynumber[j]>arraynumber[j+1]:
			temp1=arraynumber[j]
			temp2=arrayname[j]
			arraynumber[j]=arraynumber[j+1]
			arrayname[j]=arrayname[j+1]
			arraynumber[j+1]=temp1
			arrayname[j+1]=temp2


for i in arraynumber:
	if i not in result:
		result.append(i)
result.sort()
print(result)
count=0
final=[]
if len(result)>2:
	for i in range(0,len(arraynumber)):
		if result[1]==arraynumber[i]:
			final.append(arrayname[i])

else:
	for i in range(0,len(arrayname)):
		if result[-1]==arraynumber[i]:
			final.append(arrayname[i])
final.sort()
for i in final:
	print(i)

