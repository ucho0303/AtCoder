import math
a,b,h,m = map(int,input().split())
h *= 5
h += m/12
s = abs(h-m)
coss = math.cos(math.radians(s*6))
print((a**2 + b**2 - 2*a*b*coss)**(0.5))
