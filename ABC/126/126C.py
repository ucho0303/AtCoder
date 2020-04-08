n,k = map(int,input().split())
ans = 0
for i in range(1,n+1):
    for j in range(1000):
        x = i*2**j
        if x >= k:
            ans += 1/n/(2**j)
            break
print(ans)