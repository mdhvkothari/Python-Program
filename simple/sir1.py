a= int(input("Enter number of people:"))
glass=100


for i in range (0,a): 
 c=float(input("Enter time of entry:"))
 glass=glass-1
print "Now we have",glass ,"glasses left"


b= int(input("Enter number of exit people:"))
for j in range (0,b):
 e=float(input("Enter time of exit:"))
if (b<=a):
 d=glass+b
 print "Now we have", d ,"glasses left"
else :
 print "Enter number is not valid"