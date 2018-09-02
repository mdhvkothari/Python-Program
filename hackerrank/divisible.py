a=100
count=0
n1=1
n2=2
number=[]
while n2<a:
	n=n1+n2
	n1=n2
	n2=n
	count+=1
	if n1%2==0:
		number.append(n1)
print(sum(number))