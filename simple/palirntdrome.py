a= int(input("Enter number:"))
z=a
y=0
while(a!=0):
 b= a%10
 a= a/10
 y= y*10+b
print y
if (z==y):
 print "Number is palientdome"
else:
 print "Number is not palientdome"