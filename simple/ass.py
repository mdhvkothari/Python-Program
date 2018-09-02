a=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
temp=0
b=int(input("Enter how number to assend:"))

for i in range(0,b):
 a[i]=int(input("Enter number to assend:"))



for i in range(0,b-1):
 for j in range(0,b-1):
  if a[i]>a[i+1]:
   temp=a[i]
   a[i]=a[i+1]
   a[i+1]=temp
   
   print a