a="456madh56av"
b=list(a)

c=[]
for i in range(0,len(b)):
    if b[i].isnumeric():
        c.append(b[i])
print (c)
sum=0
for j in range(0,len(c)):
    sum=sum+int(c[j])
    print (sum)
    
    

        