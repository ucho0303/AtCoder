n,d = map(int,input().split())
x = [0]*n
for i in range(n) :
    x[i] = list(map(int,input().split()))
ans = 0
for i in range(n) :
    for j in range(i+1,n) :
        a = 0
        for k in range(d) :
            a += (x[i][k] - x[j][k])**2
        a = a**0.5
        if int(a) == a :
            ans += 1
print(ans)

