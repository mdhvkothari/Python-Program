l=842
r= 888
result= 0
for i in range(l,r+1):
    num = i
    count=0
    while(num>0):
        rem = num%2
        num = num//2
        if rem == 1:
            count+=1 
    if count == 2:
        result +=1
    if count>2:
        flag=0
        for i in range(2,count):
            if count%i ==0:
                flag = 1
                break
        if flag==0:
            result+=1
        


print(result)