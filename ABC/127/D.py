n,m = map(int,input().split())
a = list(map(int,input().split()))
x = []
for i in range(m):
    x.append(list(map(int,input().split())))
x = sorted(x, key=lambda s:s[1], reverse=True)
y = []
for i in range(m):
    b,c = x[i][0],x[i][1]
    y += [c]*b
    if len(y) >= n:
        break
z = a+y
print(sum(sorted(z,reverse=True)[:n]))


