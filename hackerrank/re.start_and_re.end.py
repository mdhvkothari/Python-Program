s=raw_input()
k=raw_input()
b=len(k)
count=0
for i in range(0,len(s)):
	if s[i:b]==k:
		count+=1
		print(i,b-1)
	b+=1
if count==0:
	print((-1,-1))


	
