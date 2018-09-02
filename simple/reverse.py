a= int(input("Enter number for reverse:"))
y=0
while(a!=0):
 b= a%10  #a=123 b=3  b=2 b=1
 a= a/10  #a=12 a=10 a=0
 y=y*10+b #y=3 y=32
print (y)