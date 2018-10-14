import numpy as np 
n,m = list(map(int,raw_input().split()))

a1=np.array(input().split() for _ in range(n))
a2=np.array(input().split() for _ in range(n))

print(a1+a2)
print(a1-a2)
print(a1*a2)
print(a1/a2)
print(a1%a2)
print(a1**a2)







