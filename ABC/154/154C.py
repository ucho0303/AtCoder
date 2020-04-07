n = int(input())
a = list(map(int,input().split()))
a.sort()
ans = 'YES'
for i in range(1,n):
    if a[i-1] == a[i] :
        ans = 'NO'
        break
print(ans)