a = [3, 1, 2, 4, 5]

l = 0
r = len(a)-1
area = 0
while l<r:
    area = max(area, min(a[l],a[r]) * (r-l))
    if a[l]<a[r]:
        l+=1
    else:
        r-=1
    

    

