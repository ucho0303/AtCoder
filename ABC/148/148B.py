n =int(input())
t,s = map(str,input().split())
ans = ''
for i in range(n):
    ans += t[i] + s[i]
print(ans)