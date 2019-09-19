T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    age = arr[0:3]
    money = arr[3:]
    if(age[0]==age[1] and age[0]==age[2]):
        if(money[0]==money[1] and  money[0]==money[2]):
            print("FAIR")
        else:
            print("NOT FAIR")

    for i in range(len(age)-1,0,-1):
        swap  = False
        for j in range(i):
            if (age[j]>age[j+1]):
                swap = True
                age[j],age[j+1] = age[j+1],age[j]
                money[j],money[j+1] = money[j+1],money[j]
        if(swap==False):
            break
    if(money[0]<money[1] and money[0]<money[2] and money[1]<money[2] ):
        print("FAIR")
    else:
        print("NOT FAIR")
