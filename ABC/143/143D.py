n = int(input())
x = sorted(list(map(int,input().split())),reverse=True)
ans = 0
for i in range(n-2) :
    for j in range(i+1,n-1) :
        for k in range(j+1,n) :
            if i < j+i :
                ans += 1
            else :
                break
print(ans)

