n=int(input())
arr=[]
for i in range(0,n):
 n1=int(input())
 arr.append(n1)
arr1=[]
for j in range(1,len(arr)):
 for k in range(1,len(arr)):
  if k+j==8:
   arr1.append(arr[k-1]+arr[j-1])
print(max(arr1))