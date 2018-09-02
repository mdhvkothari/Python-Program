x= str(input("Enter spell:"))
z= str(input("Enter alphabate to check:"))
y= len(x)
count=0
for i in range (0,y):
 if x[i]== z:
  count =count+1
if count==0:
 print "No match found"
else: 
 print "Alphabate a comes:", count, "times"
 
