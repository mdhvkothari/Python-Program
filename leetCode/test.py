string = "The quick brown fox jumped over the lazy dog"
arr = string.split()
for i in range(0,len(arr)):
    a = "a"*(i+1)
    if arr[i][0] in "AEIOUaeiou":
        arr[i] = arr[i]+"ma"+a
    else:
        left = arr[i][1:]
        arr[i] = left+arr[i][0]+"ma"+a
        
print(arr)












