num= int (input("Enter number to check:"))
a=0
b=1
for i in range (0,num):
 c=a+b
 a=b
 b=c
 print c