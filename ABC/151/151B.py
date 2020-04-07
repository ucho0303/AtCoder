n,k,m = map(int,input().split())
a = list(map(int,input().split()))
ans = -1
for i in range(k+1):
    if (sum(a)+i)/n >= m:
        ans = i
        break
print(ans)