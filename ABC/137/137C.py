n = int(input())
a = [''.join(sorted(input())) for i in range(n)]
ans = 0
count = 0
a.sort()
for i in range(1,n) :
    if a[i] == a[i-1] :
        count += 1
        ans += count
    else :
        count = 0
print(ans)






