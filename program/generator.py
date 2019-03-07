#generator is  used to genetrate a value only once for eg- if we wants to print 10 lakh number
#then it will take time and increase my ram so generator is used to generate such a long number
#basically it is used to save the ram space

def gen(n):
    for i in range(n):
        yield i
#it will create an object and we can use this space which will used to genetrate 100000 numbers
#now we can use this space for another work
print(gen(100000))

#for printing
#we can use anywhere in program
for i in gen(1000):
    print i


#how can we itrate a string
string = "mdhv"
itr = iter(string)
print next(itr) #this will give the first value that is m
print next(itr)
print next(itr)
print next(itr)
#after 4 this will give error
print next(itr)
