n = int(input())
x = list(map(int,input().split()))
ans = 1
b = x[0]
for i in range(1,n):
    if x[i] < b:
        ans += 1
        b = x[i]
print(ans)
