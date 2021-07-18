name = "saeed"
typed = "ssaaedd"

dic1={}
dic2={}

for i in name:
    if i in dic1:
        dic1[i]+=1
    else:
        dic1[i] = 1

for i in typed :
    if i in dic2:
        dic2[i]+=1
    else:
        dic2[i] = 1
print(dic1)
print(dic2)
flag = 0
for i in dic1:
    if dic1[i] != dic2[i] and dic1[i]>dic2[i]:
        flag = 1

if flag==1:
    print("Flase")