n,a,b = map(int,input().split())
c = a + b
ans = (n//c)*a
d = n%c
if d >= a:
    ans += a
else :
    ans += d
print(ans)