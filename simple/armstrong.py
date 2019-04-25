a=int(input("Enter number to check armstrong:"))
z=a
c=0
while(a!=0):
 r=a%10
 a=a/10
 c=c+(r*r*r)

if c==z:
 print "Input number is armstrong"
else:
 print"Input number is not armstrong"