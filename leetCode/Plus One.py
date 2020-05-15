
digits=[1,2,3]
num = 0
for i in range(0,len(digits)):
    num = num*10+digits[i]
    num = num+1
result = []
while(num):
    rem = num%10
    result.append(rem)
    num = num//10
print(result[::-1])