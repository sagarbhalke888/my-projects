import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)],int)
s=numpy.sum(A,axis=0)
p=numpy.prod(s,axis=0)
print(p)
