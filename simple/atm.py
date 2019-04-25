a= int(input("Enter your atm password:"))
if (a==1234): 
 print "Procced"
else:
 print "*****Wrong password*****"
b= int(input("Enter amount of money to widhrow:"))
if (b<=30000):
 c= b/2000
 b= b%2000
 d= b/500
 b= b%500
 e= b/100
 print "You got", c, "note of 2000:", "You got", d, "note of 500:", "You got", e, "note of 100:" 