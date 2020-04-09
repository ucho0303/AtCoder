n = int(input())
ans = []
for i in range(1,int(n**0.5)+1):
    if n % i == 0:
        x = n/i
        ans.append(int(i + x -2))
print(min(ans))
