n = int(input())
a = []
for i in range(5):
    a.append(int(input()))
x = min(a)
ans = (n-1)//x + 5
print(ans)