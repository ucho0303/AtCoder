n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
x = sum(b)
for i in range(n) :
    if a[i] >= b[i] :
        a[i] -= b[i]
        b[i] = 0
    else :
        b[i] -= a[i]
        a[i] = 0
        if a[i+1] >= b[i] :
            a[i+1] -= b[i]
            b[i] = 0
        else :
            b[i] -= a[i+1]
            a[i+1] = 0
y = sum(b)
print(x-y)