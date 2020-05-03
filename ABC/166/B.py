n,k = map(int,input().split())
d = []
a = []
for i in range(k):
    d.append(int(input()))
    a += list(map(int,input().split()))
x = [0]*n
for num in a:
    x[num-1] += 1
print(x.count(0))