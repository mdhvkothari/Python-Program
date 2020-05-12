n = 998
arr = []
while True:
    sum = 0
    if sum !=1:
        while n :
            rem = n%10
            sum = sum+rem*rem
            n = n//10
        n = sum
    if sum not in  arr:
        arr.append(sum)
    else:
        break
if 1 in arr:
    print(True)
else:
    print(False)
