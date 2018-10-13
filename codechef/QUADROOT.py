import math
A=int(input())
B=int(input())
C=int(input())
x1=(-B + math.sqrt((B*B) -4*A*C))/2*A
x2=(-B - math.sqrt((B*B) -4*A*C))/2*A
print(int(x1))
print(int(x2))
