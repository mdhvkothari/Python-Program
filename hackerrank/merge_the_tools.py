s= raw_input()
k = int(input())
l=0
arr = []
for i in range(0,len(s),k):
	arr.append(s[i:k])
	l=k
	k=k+l
	
for j in range(0,len(arr)):
	word = arr[j]
	final = ''
	for k in range(0,len(word)):
		if word[k] not in final:
			final = final+word[k]
	print(final)
