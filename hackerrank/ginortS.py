s=raw_input()
smaller=[]
larger=[]
odd=[]
even=[]
final=""

for i in range(0,len(s)):
	if (ord(s[i])>=97 and ord(s[i])<=122):
		smaller.append(s[i])
	elif (ord(s[i])>=65 and ord(s[i])<=90):
		larger.append(s[i])
	elif (ord(s[i])==48 or ord(s[i])==50 or ord(s[i])==52 or ord(s[i])==54 or ord(s[i])==56):
		even.append(int(s[i]))
	else:
		odd.append(int(s[i]))


for i in range(0,len(smaller)):
	for j in range(0,len(smaller)-1):
		if smaller[j]>smaller[j+1]:
			temp=smaller[j]
			smaller[j]=smaller[j+1]
			smaller[j+1]=temp

for i in range(0,len(larger)):
	for j in range(0,len(larger)-1):
		if larger[j]>larger[j+1]:
			temp=larger[j]
			larger[j]=larger[j+1]
			larger[j+1]=temp
even.sort()
odd.sort()

for i in range(0,len(larger)):
	smaller.append(larger[i])
for i in range(0,len(odd)):
	smaller.append(str(odd[i]))
for i in range(0,len(even)):
	smaller.append(str(even[i]))

for i in range(0,len(s)):
	final+=smaller[i]

print(final)









