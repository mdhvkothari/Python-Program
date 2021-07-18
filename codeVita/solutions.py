#Question : B 


from itertools import permutations

T = int(input())
N = int(input())

arr = list(map(int,input().strip().split(' ')))


allValues = permutations(arr)
allPossible  = []
for i in list(allValues):
    allPossible.append(list(i))
flag = 0
for i in range(0,len(allPossible)):
    count = 0
    for j in range(0,len(allPossible[i])-1):
        if (allPossible[i][j] + allPossible[i][j+1])%3!=0:
            count+=1
    if count == len(arr)-1:
        flag = 1

if flag ==1:
    print("Yes")
else:
    print("No")









