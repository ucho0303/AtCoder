n,q = map(int,input().split())
s = input()
l = []
for i in range(q):
    l.append(tuple(map(int,input().split())))
x = [0]*n
a = 0
flag = False
for i in range(n):
    if s[i] == 'A':
        flag = True
    elif s[i] == 'C' and flag:
        a += 1
        flag = False
    else:
        flag = False
    x[i] = a
for i in range(q):
    print(x[l[i][1]-1]-x[l[i][0]-1])