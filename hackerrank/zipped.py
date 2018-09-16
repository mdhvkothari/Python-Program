n,x=map(str, raw_input().split())
value=[]
for i in range(0,int(x)):
	array=list(map(str,raw_input().split()))
	value.append(array)

for i in range(0,int(n)):
	sum1=0
	for j in range(0,int(x)):
		sum1+=float(value[j][i])
	print(sum1/int(x))