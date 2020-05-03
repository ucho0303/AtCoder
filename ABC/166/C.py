n,m = map(int,input().split())
h = list(map(int,input().split()))
x = []
ans = [0]*n
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    if h[a] > h[b]:
        ans[b] += 1
    elif h[a] < h[b]:
        ans[a] += 1
    else:
        ans[b] += 1
        ans[a] += 1
print(ans.count(0))

