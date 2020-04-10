n = int(input())
ans = [0]*(n)
a = [0,0]
for i in range(n-1):
    b = list(map(int,input().split()))
    if b[0] in a or b[1] in a:
        ans[i+1] = ans[i] + 1
    else :
        ans[i+1] = 1
    a = b
    if ans[0] < ans[i+1]:
        ans[0] = ans[i+1]
for i in range(n):
    print(ans[i])
