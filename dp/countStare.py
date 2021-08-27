# in this we can cover 3 stare at a time se we have to find the all steps taken
#solution = we can sum all the possible stare cover in a given positon
# so we are storing all the values into an arr and return arrlast position



def fiboTab(a,arr):
    arr[0] = 1

    for i in range(1,a+1):
        if i == 1:
            arr[i] = arr[i-1]
        elif i == 2:
            arr[i] = arr[i-1] + arr[i-2]
        else:
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

    return arr[a]



arr = []
a = 10
for i in range(0,a+1):
    arr.append(0)


print(fiboTab(a,arr))



        



