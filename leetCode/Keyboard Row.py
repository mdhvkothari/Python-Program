words=["Hello", "Alaska", "Dad", "Peace"]
arr=[]
one = "qwertyuiop"
two = "asdfghjkl"
three= "zxcvbnm"
for i in range(0,len(words)):
    string=""
    for j in range(0,len(words[i])):
        if words[i][j] in one:
            string += "1"
        elif words[i][j] in two:
            string +="2"
        elif words[i][j] in three:
            string +="3"
    arr.append(string)
result = []
for i in range(0,len(arr)):
    flag= 0
    for j in range(0,len(arr[i])-1):
        if arr[i][j] != arr[i][j+1]:
            flag = 1
            break
    if flag==0:
        result.append(words[i])
print(result)