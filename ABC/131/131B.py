n,l = map(int,input().split())
a = []
b = []
for i in range(l,l+n) :
    a.append(abs(i))
    b.append(i)
x = min(a)
b.pop(a.index(x))
print(sum(b))


