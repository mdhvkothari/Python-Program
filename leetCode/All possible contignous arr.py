arr=[1,2,3,4]
permutation=[]
index=0
for i in range(0,len(arr)):
    index=i
    for j in range(0,i):
        while(index!=len(arr)+1):
            print(arr[j:index])
            index+=1
            j+=1
    