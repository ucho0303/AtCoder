n,k = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for m in a :
    if m >= k :
        ans += 1
print(ans)