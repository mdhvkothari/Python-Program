a= int (input("Enter your age:"))
b= int(input("Enter your anuall salary:"))
if a<=80:
 print ""
 if b<=25000:
  print "You have not to pay tax"
 elif b<=500000 & b>250000:
  c= b*.05
  print "You have to pay",c,"rupees to government"
 elif b<=100000 & b>250000:
  c= b*.2
  print "You have to pay", c, "rupess to government"
 elif b>100000:
  c= b*.3
  print "You have to pay", c, "rupess to government" 
if a>80:
 if  b<=500000:
  print "you have not to pay tax"
 elif b>500000 & b<=1000000:
  c= b*.2
  print "You have to pay ",c, "rupess to govenment"
 elif b>1000000:
  c= b*.3
  print "You have to pay", c, "rupess to govenment" 


 
