num= int(input("Enter your amount"))
b=50000
if (num<=b):
 if (num>=2000):
  print "Sorry atm don't have 2000 note if u want to continue then press 1"
 a= int(input("Enter number 1")
if (a==1):
 num= num%500
 c= num/500
 num= num%100
 d= num/100
 print "you got", c, "notes of 500", "you got" , d, "notes of 100"
else: 
 print "hard luck "