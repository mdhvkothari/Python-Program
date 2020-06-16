def find_gcd(x,y):
     while (y):
          x,y = y, x%y
     return x


N  = int(input())
if(N!=0 and  N!=1):

     A = list(map(int,input().split()))


     num1 = A[0]
     num2 = A[1]

     gcd = find_gcd(num1,num2)

     for i in range(2,N):
          gcd = find_gcd(gcd,A[i])





     mul = 1
     for i in range(0,N):
          mul = mul * A[i]

     fx = mul%(10^9+7)
     print(pow(fx,gcd))
else:
     print(0)