letters = ["c","f","j"]
maxArr =[]
target = "g"
if target>=letters[-1]:
    print(letters[0])
l=0
r=len(letters)-1
while l<=r:
    mid=(l+r)//2
    if letters[mid]>target:
        r=mid
    else:
        l=mid+1
    if l==r:
        print(letters[l])