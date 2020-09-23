a = "abca"
for i in range(0,len(a)):
    s = a[0:i]+a[i+1:len(a)]
    if s == s[::-1]:
        print("yes")