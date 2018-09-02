a= int(input("enter number:"))
for i in range(0,a):
	b= int(input("enter seat number:"))
	if b%6==0 or (b-1)%6==0:
		print("WS")
	else :
		if b%3==0 or (b-1)%3==0:
			print("AS")
		else:
			print("MS") 