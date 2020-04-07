a,b,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = min(A) + min(B) 
for i in range(m) :
    X = list(map(int,input().split()))
    y = A[X[0]-1] + B[X[1]-1] - X[2]
    if y <= ans :
        ans = y
print(ans)

