n,k = map(int,input().split())
if k >= n:
    print(min(n,abs(n-k)))
else :
    x = n//k
    n -= k*x
    print(min(n,abs(n-k)))