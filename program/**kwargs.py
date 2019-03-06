# **kwargs is user for passing when arguments have key ane valve like dictionary


def student(**kwargs):
    for key,value in kwargs.items():
        print key,value




dictionary = {"madhav":19,"rahul":17,"bikesh":22}

student(**dictionary)
