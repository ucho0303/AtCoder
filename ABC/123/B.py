a = []
for i in range(5):
    a.append(input())
ans = 0
a.sort(key = lambda x: x[-1])
flag = True
for s in a:
    if s[-1] == '0' and flag:
        ans += int(s)
    elif flag:
        ans += int(s)
        flag = False
    else:
        x = int(s[-1])
        ans += int(s) + 10 -x
print(ans)
