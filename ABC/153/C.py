n,k = map(int,input().split())
h = list(map(int,input().split()))
h.sort()
if k == 0:
    ans = h
else:
    ans = h[:-k]
print(sum(ans))
