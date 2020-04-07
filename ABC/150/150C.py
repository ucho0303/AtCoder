n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))

import itertools
a = tuple(i for i in range(1,n+1))
x = list(itertools.permutations(a))
#print(x)
px = x.index(p)
qx = x.index(q)
print(abs(px-qx))




