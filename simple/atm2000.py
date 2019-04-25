amount= int(input("enter your amount to withdrow"))
balance =int(input("enter your balance amount"))
if amount<=balance: 
 a= amount/2000
 amount= amount%2000
 b= amount/500
 amount= amount%500
 c= amount/100 
 print "You got" ,a, "note of 2000", "you got", b, "note of 500", "you got" ,c ,"note of 100"
else :
 print "Atm don't have 2000 note if u want to comtinue press 1"
 
 
 