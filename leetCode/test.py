n = 7
term =4
arr=[]
i=2
j=2
while(len(arr)!=n):
        falg=0
        for j in range(2,i):
            if i%j == 0:
                falg =1
            j+=1
        if falg != 1:
            arr.append(i)
        i+=1
for i in range(0,len(arr)-1):
    print(term+arr[i])
    term = term + arr[i]