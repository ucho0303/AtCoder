mod =10**9+7
n,a,b = map(int,input().split())
ans = pow(2,n,mod)-1
def cmb(n,k):
    x,y = 1,1
    for i in range(k):
        x = x * (n-i) % mod
        y = y * (k-i) % mod
    return x * pow(y, mod-2, mod) % mod
ans -= cmb(n,a) + cmb(n,b)
print(ans%mod)