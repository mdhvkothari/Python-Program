a=[1,11,1]
b=int(input("Enter length of arry:"))

for i in range(0,b):
 a[i]=int(input("Enter arry values:"))

for i in range(0,b):
 print a[i]

 c=a[-1]
 

print c

sum=0
for i in range(0,b):
 if c<0:
  sum=sum+a[i]

print sum

  else:
   print "you are not enter negative value" 
  