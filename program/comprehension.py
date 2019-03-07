#list comprehension

list = [3,1,4,1,2,5,1,2,2,2,4,3,6,9]
number = []
for i in list:
    if i%3==0:
        number.append(i)
print "this is without list comprehension",number

print "this is with list comprehension",[i for i in list if i%3==0]

#set comprehension

set = {x**2 for x in [1,2,3,5,2,5,5,6]} #{} is used as a set which remove repated value
print set

#generator comprehension
#this will generate on fly value
#() is used to create generator
gen = (i for i in range(100) if i%3==0 )
for item in gen:
    print item
