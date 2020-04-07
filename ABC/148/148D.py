n = int(input())
a = list(map(int,input().split()))
x = 1 
ans = 0
for i in range(n) :
    if a[i] != x :
        ans += 1
    else :
        x += 1
if x == 1 :
    print(-1)
else :
    print(ans)

