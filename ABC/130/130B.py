n,x = map(int,input().split())
l = list(map(int,input().split()))
a =[0]
ans = n+1
for i in range(n):
    s = a[i] + l[i]
    if s > x:
        ans = i+1
        break
    else:
        a.append(s)
print(ans)
