names = ["wano","wano","wano","wano"]
count=[0,0,0,0]
for i in range(0,len(names)):
    number=0
    positon=0
    intial = i
    for j in range(i,len(names)):
        if names[i] == names[j]:
            number+=1
            positon = j
    temp = intial
    print(positon)
print(count)
reslut = []
for i in range(0,len(count)):
    if count[i]>1:
        add = "("+str(count[i])+")"
        names[i] = names[i]+add
        reslut.append(names[i])
    else:
        reslut.append(names[i])
print(reslut)
