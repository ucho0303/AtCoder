def cmb(n,k,mod):
    x,y = 1,1
    for i in range(k):
        x = x * (n-i) % mod
        y = y * (k-i) % mod
    return x * pow(y, mod-2, mod) % mod



