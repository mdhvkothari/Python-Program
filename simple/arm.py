a= int(input("Enter number:"))
su=0
while (a!=0):
 b=a%10
 su=su+b*b*b
 a=a/10
print su
if (su==a) :
 print "Your number is armstrong"
else:
 print "Your number is not armstrong"
 