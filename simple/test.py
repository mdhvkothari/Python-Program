# import itertools

# n = int(input())
# arr = list(map(int,input().split()))
# # s = 24

# flag = 0
# result = list(itertools.combinations(arr,3))

# for i in range(0,len(result)):
#     if sum(result[i]) == s:
#         print(*list(result[i]))
#         falg = 1
# if flag == 0:
#     print("no")


# import itertools
# def main():

#  # Write code here 
#     N = int(input())
#     Ai = list(map(int,input().split()))
#     S = int(input())
#     flag = 0
#     result = list(itertools.combinations(Ai,3))
#     for i in range(0,len(result)):
#         if sum(result[i]) == S:
#             print(*list(result[i]))
#             flag = 1
#     if flag==0:
#         print('No Triplet Found')
# main()
# resultSum = -200
# for i in range(1,6):
#     for w in range(1, len(arr)+1):
#         for i in range(len(arr)-w+1):
#             yield arr[i:i+w]

# result = 0
# for i in range(0,len(arr)):
#     a = sum(arr[i:])
#     b = sum(arr[:-i])
#     if result<a:
#         result = a
#     if result<b:
#         result = b
# print(result)
dic = {'a':10,'b':9,'c':12}
dic1 = {}
val = sorted(dic.values(),reverse = True)
for i in range(0,len(val)):
    a = list(dic.keys())[list(dic.values()).index(val[i])]
    dic1[a] = val[i]
print(dic1)
    