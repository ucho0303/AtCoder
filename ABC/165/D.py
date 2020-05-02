a,b,n = map(int,input().split())
ans = 0
if b > n :
    x = n
    ans = (a*x)//b - a*(x//b)
elif b == n :
    x = n-1
    ans = (a*x)//b - a*(x//b)
else:
    x = b-1
    ans = (a*x)//b - a*(x//b)
print(ans)