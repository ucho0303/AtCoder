n = int(input())
a = []
ans = 0
for i in range(n):
    a.append(tuple(map(int,input().split())))
for i in range(n-1):
    for j in range(i+1,n):
        ans += ((a[i][0] - a[j][0])**2 + (a[i][1] - a[j][1])**2)**0.5
print(ans*2/n)