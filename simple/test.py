a = ['G','O','D']
b = a[::-1]

for i in range(0,len(a)):
    arr=a[i]
    rev=b[i]
    for j in range(0,len(a)):
        if(i!=j):
            arr = arr+a[j]
            rev =rev+b[j]
    print(arr)
    print(rev)
