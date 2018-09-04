S=raw_input()
a=[]
for o in range(0,len(S)):
	a.append(S[o])
vowel=['A','E','I','O','U']
other=['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
c_vowel=0
c_other=0
count_vowel=0
count_other=0
#for vowel
for i in range(0,len(a)):
	for j in range(0,len(vowel)):
		if a[i]==vowel[j]:
			c_vowel=i
			while(c_vowel<len(a)+1):
				d_vowel=a[i:c_vowel]
				c_vowel=c_vowel+1
				if (len(d_vowel)>0):
					count_vowel+=1


#for consonent

for k in range(0,len(a)):
	for l in range(0,len(other)):
		if a[k]==other[l]:
			c_other=k
			while(c_other<len(a)+1):
				d_other=a[k:c_other]
				c_other=c_other+1
				if(len(d_other)>0):
					count_other+=1
if(count_vowel>count_other):
	print 'Kevin',count_vowel 
elif(count_other>count_vowel):
	print 'Stuart',count_other
else:
	print('Draw') 