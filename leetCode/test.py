name = "xnhtq"
typed = "xhhttqq"
dict1={}
dict2={}
for i in range(0,len(name)):
    if name[i] in dict1:
        dict1[name[i]] +=1
    else:
        dict1[name[i]] = 1

for i in range(0,len(typed)):
    if typed[i] in dict2:
        dict2[typed[i]] +=1
    else:
        dict2[typed[i]] = 1
print(dict1)
print(dict2)
for i in dict2:
    if dict2[i] < dict1[i]:
        print(False)
