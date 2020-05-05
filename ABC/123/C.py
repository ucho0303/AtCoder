n = int(input())
a = []
for i in range(5):
    a.append(int(input()))
x = min(a)
ans = n//x + 5
print(ans)