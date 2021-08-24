T=int(input())
for i in range(0,T):
	k,n=raw_input().split()
	value=list(map(int,raw_input().strip().split(' ')))
	impress=[]
	i=0
	a=int(n)
	while (a!=len(value)):
		x=value[i:a]
		impress.append(sum(x))
		i+=1
		a+=1

print(max(impress))