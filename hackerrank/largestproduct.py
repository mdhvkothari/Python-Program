a="3675356291"
b=[]
large=5
for i in range(0,6):
	b.append(a[i:large])
	large+=1
print(b)
numbers =[]
for i in range(0,len(b)):
	for j in range(0,len(b[i])):
		f=int(b[i])%10
		b[i]=int(b[i])/10
		numbers.append(f)
print(numbers)
final=[]
g=0
f=5

for i in range(0,6):
    mul=1
    for k in range(g,f):
		mul=mul*numbers[k]
    g=f
    f=f+5
    final.append(mul)

print(max(final))