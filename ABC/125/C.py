from fractions import gcd
n = int(input())
a = list(map(int,input().split()))
l = [0]
r = [0]
for i in range(n):
    l.append(gcd(l[i],a[i]))
    r.append(gcd(r[i],a[-i-1]))
r = r[::-1]
ans = 0
for i in range(n):
    ans = max(ans,gcd(l[i],r[i+1]))
print(ans)
