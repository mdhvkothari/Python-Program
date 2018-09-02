a=[1,2,3]
b=[]
c= int(input("Enter number:"))
temp=0
for j in range(0,3):
	for i in range(0,2):
		temp=a[i+1]
		a[i+1]=a[i]
		a[i]=a[-1]
		a[-1]=temp


print(a)

