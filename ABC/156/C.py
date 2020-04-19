n = int(input())
a = list(map(int,input().split()))
ans = 10000000000000
for i in range(101):
    x = 0
    for j in range(n):
        x += (i - a[j])**2
    if ans >= x:
        ans = x
print(ans)


