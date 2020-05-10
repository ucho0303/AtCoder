s = input()
n = len(s)
l = ['A','C','G','T']
ans = 0
a = 0
for i in range(n):
    if s[i] in l:
        a += 1
    else:
        a = 0
    ans = max(ans,a)
print(ans)
