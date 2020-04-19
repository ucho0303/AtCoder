n,k = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
j = 0
x = 0
for i in range(n):
    while j < n and x < k:
        x += a[j]
        j += 1
    if x < k:
        break
    ans += n-j+1
    x -= a[i]
print(ans)