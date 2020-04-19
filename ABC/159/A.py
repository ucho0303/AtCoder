n,m =map(int,input().split())
def fx(x) :
    ans = 0
    for i in range(1,x):
        ans += i
    return ans
print(fx(n) + fx(m))