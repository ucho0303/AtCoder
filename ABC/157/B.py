whith1 = list(map(int,input().split()))
whith2 = list(map(int,input().split()))
whith3 = list(map(int,input().split()))
b = whith1 + whith2 + whith3
n = int(input())
num = []
for i in range(n):
    x = int(input())
    if x in b :
        b = [0 if i == x else i for i in b]
if b[0] == b[1] == b[2] or b[3] == b[4] == b[5] == 0 or b[6] == b[7] == b[8] == 0:
    print('Yes')
elif b[0] == b[3] == b[6] or b[1] == b[4] == b[7] == 0 or b[2] == b[5] == b[8] == 0:
    print('Yes')
elif b[0] == b[4] == b[8] or b[2] == b[4] == b[6] == 0 or b[6] == b[7] == b[8] == 0:
    print('Yes')
else :
    print('No')