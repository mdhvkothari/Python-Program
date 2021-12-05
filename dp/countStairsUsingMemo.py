

def countStair(n,arr):
    if n==0:
        return 1 
    elif n<0:
        return 0
    
    if arr[n] > 0:
        return arr[n]

    a1 = countStair(n-1,arr)
    a2 = countStair(n-2,arr)
    a3 = countStair(n-3,arr)
    cp = a1+a2+a3
    arr[n] = cp
    return cp


print(countStair(10,[0 for _ in range(0,11)]))
