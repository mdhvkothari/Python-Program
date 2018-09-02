t=int(input())
for i in range(0,t):
    n= int(input())
    y=0
    while(n!=0):
        b= n%10  
        n= n/10  
        y=y*10+b 
    print (y)