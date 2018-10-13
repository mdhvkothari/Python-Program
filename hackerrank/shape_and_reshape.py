import numpy

numbers = list(map(int,raw_input().strip().split(' ')))

array=numpy.array(numbers)
print(numpy.reshape(numbers,(3,3)))
