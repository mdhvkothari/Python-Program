arr =[3,3,1,0,2,0,1]
futher_reached = 0
len_arr = len(arr)-1
i = 0
while i<=futher_reached and futher_reached<len_arr:
    futher_reached = max(futher_reached,arr[i]+i)
    i +=1
    print(futher_reached)
if futher_reached>=len_arr:
    print("yes")
