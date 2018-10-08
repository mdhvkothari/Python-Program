import re

t= int(input())
for i in range(0,t):
	string=raw_input()
	ans=True
	try:
		re.compile(string)
	except :
		ans= False
	print(ans)