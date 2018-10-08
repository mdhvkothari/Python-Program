from itertools import groupby

a=raw_input()

for i,j in groupby(a):
	print ('{},{}'.format(len(list(j)),i))