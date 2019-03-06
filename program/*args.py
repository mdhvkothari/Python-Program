# *args is used for passing parameter if is any parameter is missing


def name(*args):
    if (len(args)==3):
        print "name:",args[0],"lastname:",args[1],"age:",args[2]
    elif (len(args)==2):
        print "name:",args[0],"lastname:",args[1]
    else:
        print "pass proper arguments"
# *args is tuple type so we can access like above
#we pass like this
list=["madhav","kothari",19]
name(*list)

list1 = ["madhav","kothari"]
name(*list1)


name("madhv")
