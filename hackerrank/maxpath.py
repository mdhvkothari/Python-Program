a=int(input())
array=[]
for i in range(0,a):
	
	name = str(input())
	grade = float(input())
	array.append([name,grade])
array.sort(key = lambda x: x[1])
print(array)