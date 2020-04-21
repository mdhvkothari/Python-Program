def divide(a,b):
    print (a/b)

#if we want not to change in divide function but we want to to update that one then we use decorater
def update(function):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return function(a,b)
    return inner

div = update(divide)
div(1,4)