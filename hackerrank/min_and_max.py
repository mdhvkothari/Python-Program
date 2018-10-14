import numpy

n,m=raw_input().split()

array1=[]
for i in range(0,int(n)):
    elements=list(map(int,raw_input().strip().split(' ')))
    array1.append(elements)
    
mainarray=numpy.array(array1)
print(numpy.max(numpy.min(mainarray,axis=1),axis=0)