n = int(input())
ans = 0
m = 10
while n >= m :
    ans += n//m
    m *= 5
if n%2 == 0:
    print(ans)
else :
    print(0)