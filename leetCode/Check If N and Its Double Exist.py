arr=[3,1,7,11]
if 0 in arr and arr.count(0)>1:
    print(True)
        
for nums in arr:
    if nums != 0 and 2*nums in arr:
        print(True)
print(False)