A = [1,2,2,3]
flag = 0
for i in range(0,len(A)-1):
    if A[i] <= A[i+1]:
        pass
    else:
        flag = 1
        break
flag1=0
for i in range(0,len(A)-1):
    if A[i] >= A[i+1]:
        pass
    else:
        flag1 = 1
        break
if flag==0 or flag1==0 or (flag==0 and flag==0):
    print(True)
else:
    print(False)
                
# inc = dec = True
#         for i in range(0,len(A)-1):
#             if A[i]>A[i+1]:
#                 inc = False
#             if A[i]<A[i+1]:
#                 dec = False
#         return inc or dec