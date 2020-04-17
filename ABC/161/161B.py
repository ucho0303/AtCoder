n,m= map(int,input().split())
a = list(map(int,input().split()))
x = sum(a)/4/m
ans = 0
for i in a:
    if i >= x :
        ans += 1
if ans >= m:
    print('Yes')
else:
    print('No')