n=int(input("Enter number:"))
for i in range(0,n):
 for j in range(0,n):
  if i==j :
   print "1", sep=" "
  else:
   print "0", sep=" "

