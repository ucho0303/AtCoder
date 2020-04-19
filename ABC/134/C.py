n = int(input())
a = [int(input()) for i in range(n)]
x = max(a)
m = a.index(x)
a.remove(x)
y = max(a)
for i in range(n) :
    if i == m :
        print(y)
    else :
        print(x)
