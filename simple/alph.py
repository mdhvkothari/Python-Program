c=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
a= input("Enter spell:")
b= int(input("Enter how many alphabate to find:"))

x= len(a)
for i in range (0,b):
 count=0
 c= input("Enter alphabate to find:")
 for s in range (0,x):
  if  (a[s] == c):
   count=count+1
 if count==0: 
  print ("no alphabate")
 else :
  print (count)


 