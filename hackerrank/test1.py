t=int(input())
for i in range(0,t):
	s=raw_input()
	length=[]
	distinct=[]
	for i in s:
		if i not in distinct:
			distinct.append(i)
	if len(distinct)<3:
		print "Dynamic"
	else:
		for i in range(0,len(distinct)):
			count=0
			for j in range(0,len(s)):
				if s[j]==distinct[i]:
					count+=1
			length.append(count)
		length.sort()
		i=0
		flag=0
		while (i!=len(length)): 
			if	length[i]==length[i-1]+length[i-2]:
				flag=1
			else:
				flag=0
			i+=1
		if flag==1:
			print "Dynamic"
		else:
			print "Not"


