a,b = map(int,input().split())
ans = -1
for i in range(20000):
    x = int(i*0.08)
    y = int(i*0.1)
    if a == x and b == y:
        ans = i
        break
print(ans)
        