from collections import deque
n,m,k = map(int,input().split())
a = deque(map(int,input().split()))
b = deque(map(int,input().split()))
cnt = 0
ans = 0
for i in range(n+m):
    if len(a) == len(b) == 0:
        break
    elif len(a) == 0 or a[0] >= b[0]:
        cnt += b[0]
        b.popleft()
        if cnt > k:
            break
    elif len(b) == 0 or a[0] < b[0]:
        cnt += a[0]
        a.popleft()
        if cnt > k:
            break
    ans += 1
print(ans)


