from collections import deque
n,m = map(int,input().split())
l = [list() for i in range(n+1)]
ans = [0]*(n+1)
x = deque()
for i in range(m):
    a,b = map(int,input().split())
    if a == 1 :
        x.append(b)
        ans[b] = 1 
    elif b == 1:
        x.append(a)
        ans[a] = 1
    else:
        l[a] += [b]
        l[b] += [a]
while len(x) > 0:
    y = x.popleft()
    for num in l[y] :
        if ans[num] == 0:
            x.append(num)
            ans[num] = y
ans = ans[2:]
if 0 in ans :
    print('No')
else:
    print('Yes')
    for answer in ans:
        print(answer)

