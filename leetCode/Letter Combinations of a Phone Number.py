digits = "23"
arr=[0,1,"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
required = []
digitlen = len(digits)
while(len(required)<digitlen):
    rem = int(digits)%10
    digits = int(digits)/10
    required.insert(0,arr[rem])

result=[""]

for i in range(0,digitlen):
    temp_list=[]
    for ch in required[i]:
        for str in result:
            temp_list.append(str+ch)
            print(temp_list)
    result = temp_list
print(sorted(result))
