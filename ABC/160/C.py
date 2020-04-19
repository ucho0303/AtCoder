k,n = map(int,input().split())
a = list(map(int,input().split()))
x = [k - a[-1] + a[0]]*n
for i in range(n-1):
    x[i] = a[i+1] - a[i]
print(sum(x)-max(x))