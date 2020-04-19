import math
a,b,x = map(int,input().split())
s = a*a*b
if x*2 < s :
    ans = 90 - math.degrees(math.atan(2*x/(a*b*b)))
elif x == s :
    ans = 0
else :
    ans = 90 - math.degrees(math.atan(a**3/(s-x)/2))
print(ans)
