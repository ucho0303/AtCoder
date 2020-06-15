n = int(input())
a = list(map(int,input().split()))
a.sort()
if n == 1:
    print(1)
else:
    ans = n
    if a[0] % a[1] == 0:
        ans -= 1
    for i in range(1,n):
        for j in range(i):
            if a[i] % a[j] == 0:
                ans -= 1
                break
    print(ans)
