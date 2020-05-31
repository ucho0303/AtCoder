n = int(input())
a = list(map(int,input().split()))
x = 1
for num in a:
    x *= num
    if x > 10**18:
        x = -1
        break
if 0 in a:
    x = 0
print(x)