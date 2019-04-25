a= int(input("Enter number of star:"))
k=2*a-2 #for number of space

for i in range(0,a):  #outer loop for handle number of rows
 for j in range(0,k): #inner loop for handle number of spaces

  print "",

 k=k-2 # decrement of k in every loop


 for j in range(0,i+1):
  print "*",

 print"\r"


