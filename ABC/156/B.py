n,k = map(int,input().split())
for i in range(10**10):
    if k**i > n :
        ans = i
        break
print(ans)