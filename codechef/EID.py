t = int(input())
for i in range(0,t):
	n=int(input())
	v=list(map(int,input().split()))
	a=max(v)
	for i in range(0,n):
		for j in range(i+1,n):

			if (abs(v[i]-v[j])<a):
				a=abs(v[i]-v[j])
	print (a)

