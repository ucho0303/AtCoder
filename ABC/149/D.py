n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = list(input())
ans = 0
for i in range(k,n) :
    if t[i] == t[i-k] :
        t[i] = 'x'
for i in range(n) :
    if t[i] == 'r' :
        ans += p
    elif t[i] == 's' :
        ans += r 
    elif t[i] == 'p' :
        ans += s
print(ans)