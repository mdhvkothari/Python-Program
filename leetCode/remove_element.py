a= [3,2,2,3,1]
b=2
i=0
print(set(a))
while b in a:
    a.remove(b)
print(a)
# while(i<len(a)):
#     if a[i] == b:
#         a.remove(a[i])
#         print(a)
#     i+=1
# print(a)