def check(string):
	try:
		float(string)
		return True
	except :
		return False
n= int(input())
for i in range(0,n):
	value=raw_input()
	if (value=='0'):
		print("False")
	else:
		print(check(value))