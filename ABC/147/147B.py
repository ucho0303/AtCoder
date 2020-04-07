s = input()
a = len(s)
b = int(a/2)
ans = 0
for i in range(b) :
    if s[i] != s[-i-1] :
        ans += 1
print(ans)

