flag=0
a= int(input("Enter number to check:"))
for s in range (2, a):
 if a%s==0: 
  flag=1
  break
if flag==1:
 print "Number is not prime"
else:
 print "Number is a prime"