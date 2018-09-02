a=int(input("Enter number:"))
b=[]
for i in range(2,a+1):
    for j in range(2,a+1):
        d=i**j
        b.append(d)
c=set(b)   
print(len(c))
      