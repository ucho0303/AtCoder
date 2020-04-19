n = int(input())
a = input()
ans = 1
for i in range(n-1) :
    if a[i] == a[i+1] :
        pass
    else :
        ans += 1
print(ans)
