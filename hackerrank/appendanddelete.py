a= ['a','a','a','a','a','a','a','a','a','a']
b=['a','a','a','a','a']
c=[]
f=[]
g=[]
number = int(input())
alen =  len(a)
blen = len(b)
if len(a)<len(b):
	print("No")

else:
	if len(a)!=len(b):
		index = -1
		while (alen!=blen):
			d=a.pop(index)
			c.append(d)
			blen+=1
			index= index-1

		for i in range(0,len(a)):
			if a[i]!=b[i]:
				f.append(a[i:])
				g.append(b[i:])
				break

		if (len(c)+len(f[0])+len(g[0])<=number):
			print("Yes")
		else:
			 print("No")
	else:
		print("Yes")



