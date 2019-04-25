a=int(input("Enter number:"))
d=[]
for i in range(2,a):
 if a%i==0:
  d.append(i)

print "Smallest diviser of input number:",d[0] 