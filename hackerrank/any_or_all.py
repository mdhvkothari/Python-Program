n=int(input())
array=list(map(str,raw_input().split()))
if all(int(i)>=0 for i in array):
    if any(value==value[::-1] for value in array):
        print "True"
    else:
        print "False"
else:
    print "False"