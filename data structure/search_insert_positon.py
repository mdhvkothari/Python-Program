a=[1,5,7,8]
key = 0
if key in a :
    for i in range(0,len(a)):
        if (key ==a[i]):
            print(i)
else:
    index =0
    while(len(a)>index and  a[index]<key):
        index += 1
    
    print(index)