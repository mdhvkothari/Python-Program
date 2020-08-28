num =[-1,0,0,0,0,3,3]
distinct = sorted(list(set(num)))
print(distinct)
for i in range(0,len(distinct)):
    num[i] = distinct[i]
del num[len(distinct):]
print(num)