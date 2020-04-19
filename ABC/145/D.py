mod = 10**9 + 7
x,y = map(int,input().split())
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result
if (x + y)%3 != 0 :
    print(0)
else :
    n = int((x + y)/3) 
    if x - n < 0 or y - n < 0:
        print(0)
    else:
        ans = cmb(n,x-n)
        print(ans%mod)
