n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(n) :
    ans += a[i]*int(sum(a[i+1:]))
print(ans)
