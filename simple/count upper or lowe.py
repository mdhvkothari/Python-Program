
a=input("Enter string to check upper and lower cases::")
b=0
c=0
for i in a:
   if (i.isupper()):
       b=b+1
   elif (i.islower()):
       c=c+1
   else:
       pass
   
print (c)
print (b)    
    
    