a,b,c,d = map(int,input().split())
for i in range(1000):
    c -= b
    if c <= 0:
        print('Yes')
        break
    a -= d
    if a <= 0:
        print('No')
        break
