a= int(input("Enter number to names:"))
b= int(input("Enter number if you have first or last name then print= 2 or then type= 3:"))

if b==2:
 for i in range(0,a):
  b= input("Enter first name:")
  c= input("Enter last name:")
 x= len(b)
 y= len(c)
 char="."
 print b[0].upper()+char,c[0].upper()+c[1:].lower() 
 
elif b==3:
 for i in range(0,a):
  b= input("Enter first name:")
  c= input("Enter middle name:")
  d= input("Enter last name:")
 
 x= len(b)
 y= len(c)
 z= len(d)
 char="."
 print b[0].upper()+char,c[0].upper()+char,d[0].upper()+d[1:].lower()
