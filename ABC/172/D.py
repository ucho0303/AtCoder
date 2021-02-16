import sympy
n = int(input())
ans = 0
for i in range(n+1):
    x = sympy.divisors(i)
    ans += i*len(x)
print(ans)
