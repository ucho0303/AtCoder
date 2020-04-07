n = int(input())
x = list(map(int,input().split()))
ans = 0
for i in range(n-2) :
    if x[i] <= x[i+1] <= x[i+2] :
        ans += 1
    elif x[i] >= x[i+1] >= x[i+2] :
        ans += 1
print(ans)
