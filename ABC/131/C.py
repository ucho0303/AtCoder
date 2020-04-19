import math
a,b,c,d = map(int,input().split())
x = b//c + b//d - b//(c*d//math.gcd(c,d))
y = (a-1)//c + (a-1)//d - (a-1)//(c*d//math.gcd(c,d))
print(b-(a-1)-x+y)
