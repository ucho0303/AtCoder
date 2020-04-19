n,x,y = map(int,input().split())
ans = [0]*n
for i in range(1,n):
    for j in range(i+1,n+1):
        z = min(j-i, abs(x-i)+abs(j-y)+1, abs(y-i)+abs(j-x)+1)
        ans[z] += 1
for i in range(1,n):
    print(ans[i])