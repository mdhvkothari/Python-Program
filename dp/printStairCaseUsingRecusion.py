#lets suppose user can jump 3 in one time

def printStairCase(n,s):
    if n==0:
        print(s)
        return
    if n <0:
        return

    printStairCase(n-1,s+"1")
    printStairCase(n-2,s+"2")
    # printStairCase(n-3,s+"3")

printStairCase(3,"")


    