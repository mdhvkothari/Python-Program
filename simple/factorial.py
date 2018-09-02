x= int(input("Enter number to get factorial:"))
y=1
if x<0:
 print "Invalid number"
else:
 for i in range (1,x+1):
  y=y*i
 print "Factorial of this number is:",y