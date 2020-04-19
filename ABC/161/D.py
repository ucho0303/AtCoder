from collections import deque
k = int(input())
a = deque()
for i in range(1,10):
    a.append(i)
ans = []
for i in range(k):
    x = a.popleft()
    ans.append(x)
    y = x%10
    if y != 0:
        a.append(10*x + y - 1)
    a.append(10*x + y)
    if y != 9:
        a.append(x*10 + y + 1)
print(ans[k-1])