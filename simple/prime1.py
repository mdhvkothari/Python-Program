a= int(input("Enter number to start:"))
b= int(input("Enter number to end:"))
for i in range (a,b):
 flag=0
 if i==0:
  i=i+1
 for s in range (2,i):
  if i%s==0:
   flag=1
 if flag==0:
  print i