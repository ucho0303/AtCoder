n  = int(input())
a = list(map(int,input().split()))
ans = 0
mn = 0
for i in range(n):
    if a[i] < 0:
        mn += 1
        a[i] = abs(a[i])
    ans += a[i]
if 0 in a or mn%2 == 0:
    print(ans)
else:
    print(ans - 2*min(a))
