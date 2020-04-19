n,m = map(int,input().split())
a = list(map(int,input().split()))
x = sum(a)
ans = n - x
if ans >= 0:
    print(ans)
else :
    print(-1)