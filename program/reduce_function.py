#reduce function is pass a function till the end of the list

from functools import reduce

def add(a,b):
    return a+b
#it will first sum if 1 and 2 then 3 and 3 then 6 and 4 then 10 and 5
result = reduce(add,[1,2,3,4,5])
print result
