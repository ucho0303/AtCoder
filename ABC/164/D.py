s = input()
n = len(s)
ans = 0
for i in range(n-4):
    for j in range(i,n):
        x = s[i:j]
        if int(x) % 2019 == 0:
            ans += 1
print(ans)