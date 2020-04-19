n,k = map(int,input().split())
p = list(map(int,input().split()))
x = sum(p[:k])
ans = x
for i in range(k,n) :
    x += p[i] - p[i-k]
    if x > ans :
        ans = x
print((ans+k)/2)


