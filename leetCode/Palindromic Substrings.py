string = "ababa"
count=0
for i in range(0,len(string)):
    for j in range(1,len(string)+1):
        if len(string[i:j]) >0:
            if string[i:j] == string[i:j][::-1]:
                count+=1
print(count)
