N=int(input())
c=list(map(int,input().split()))
t=list(map(int,input().split()))
type1_c=1000000
type2_c=1000000
type3_c=1000000

for i in range(0,N):

	if t[i]==1:
		type1_c=min(c[i],type1_c)
	elif t[i]==2:
		type2_c=min(c[i],type2_c)
	elif t[i]==3:
		type3_c=min(c[i],type3_c)		

if (type3_c>(type1_c+type2_c)):
	print (type1_c+type2_c)
else:
	print (type3_c)