n = int(input())
a = list(map(int ,input().split()))
b = list(map(int ,input().split()))
c = list(map(int ,input().split()))
ans = b[a[0]-1]
for i in range(1,n) :
    ans += b[a[i]-1]
    #print(ans)
    if a[i] - a[i-1] == 1 :
        ans += c[a[i-1]-1]
        #print(ans)
print(ans)

