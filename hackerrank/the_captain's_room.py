from collections import Counter
k=int(input())
rooms=list(map(int,raw_input().strip().split(' ')))
cnt=Counter(rooms)
for k,v in cnt.iteritems():
	if v==1:
		print k

