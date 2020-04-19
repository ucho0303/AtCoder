import bisect
n = int(input())
l = list(map(int,input().split()))
l = sorted(l)
ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        x = bisect.bisect_left(l, l[i] + l[j], j+1)
        ans += x -j -1
print(ans)
