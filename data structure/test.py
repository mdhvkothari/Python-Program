a= "23"
a = a.strip()
arr = list(a.split(" "))
negative = False
try:
    if int(arr[0]):
        if "-" in arr[0]:
            negative = True
        if int(arr[0]) >0 and int(arr[0]) <(2**31 -1):
            print(2**31)
        elif int(arr[0]) <0  and int(arr[0]) < (2**31 -1):
            print(-2**31)
        else:
            print(arr[0])
except:
    print(0)



