n,m = raw_input().split()
a=[]
for i in range(0,int(n)):
	number = list(map(int, raw_input().split()))
	a.append(number)
k=int(input())
for i in range(0,len(a)):
	for j in range(0,len(a)-1):

		if a[j][k]==a[j+1][k]:
			if a[j][k-1]>a[j+1][k-1]:
				temp=a[j]
				a[j]=a[j+1]
				a[j+1]=temp
		else:

			if a[j][k]>a[j+1][k]:
				temp=a[j]
				a[j]=a[j+1]
				a[j+1]=temp
for i in range(0,len(a)):
	print(' '.join(map(str,a[i])))