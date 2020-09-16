a = int(input())
nums=[]
for i in range(0,a):
    num1=0
    b = int(input())
    while(b>0):
        a = b%10
        a = a-2
        num1 = num1*10 +a
        b = b//10
    num1 = str(num1)
    num1 = num1[::-1]
    num1 = int(num1)
    print(num1)