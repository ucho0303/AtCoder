n = int(input())
w = list(map(int,input().split()))
A = w[0]
a = 1
B = 0
b = 1
for i in range(n-1):
    if A >= B:
        B += w[-b]
        b += 1
    else:
        A += w[a]
        a += 1
print(abs(A-B))
