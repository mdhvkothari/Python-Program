A = "apple apple"
B = "banana"
A = A.split(" ")
B = B.split(" ")
result =[]

for i in range(0,len(A)):
    count=0
    for j in range(0,len(A)):
        if A[i] == A[j]:
            count+=1
    if count==1:
        if A[i] not in B:
            result.append(A[i])

for i in range(0,len(B)):
    count=0
    for j in range(0,len(B)):
        if B[i] == B[j]:
            count+=1
    if count==1:
        if B[i] not in A:
            result.append(B[i])
print(result)