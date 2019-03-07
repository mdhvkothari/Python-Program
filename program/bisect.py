import bisect

#it will give us the index at which we should insert the element if and only if list is sorted

number = 5

list= [1,2,3,4,6,7,8]
print bisect.bisect(list,number)
#insort will insert number at the position
bisect.insort(list,number)
