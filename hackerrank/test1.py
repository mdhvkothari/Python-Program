n=int(input())
count=0
while (n!=0):
	b=n%10
	count+=1
	n=n//10
	if (count>3):
		break
if (count>3):
	print ("More than 3 digits")
else:
	print (count)